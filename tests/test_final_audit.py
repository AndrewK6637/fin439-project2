"""Adversarial audit fixtures and independent arithmetic, not copies of production math."""
import copy,hashlib,json,math
from pathlib import Path
import numpy as np
import pandas as pd
import pytest
from src.data import load_prices,monthly_returns,estimates,ROOT
from src.engine import metrics,realized_returns,optimize,inverse_volatility,validate,rules
from src.signal import evaluate_signal
from src.workflow import run,load_config

def vintage(tmp_path,values,**changes):
    p=tmp_path/'signal.csv';p.write_text('date,CPIAUCSL\n'+values)
    meta={'vintage':'2026-11-01','url':'https://alfred.stlouisfed.org/graph/alfredgraph.csv?id=CPIAUCSL&vintage_date=2026-11-01','sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
    meta.update(changes);p.with_suffix('.meta.json').write_text(json.dumps(meta));return p

@pytest.mark.parametrize('values',['2025-09-01,100\n2026-08-01,110\n2026-09-01,.','2025-09-01,100\n2026-09-01,-1','2025-09-01,100\n2026-09-01,inf','2025-09-01,.\n2026-09-01,110','2025-09-01,100\n2026-11-02,110'])
def test_signal_invalid_latest_and_prior(tmp_path,values):
    assert evaluate_signal('2026-11-02',vintage(tmp_path,values))['status']=='Not Known'

@pytest.mark.parametrize('change',[{'sha256':''},{'url':'https://alfred.stlouisfed.org.evil.example/graph?id=CPIAUCSL&vintage_date=2026-11-01'},{'url':'https://alfred.stlouisfed.org/graph?id=OTHER&vintage_date=2026-11-01'},{'url':'https://alfred.stlouisfed.org/graph?id=CPIAUCSL&vintage_date=2026-11-02'}])
def test_signal_provenance_rejection(tmp_path,change):
    assert evaluate_signal('2026-11-02',vintage(tmp_path,'2025-09-01,100\n2026-09-01,110',**change))['status']=='Not Known'

def test_independent_signal_fixture(tmp_path):
    s=evaluate_signal('2026-11-02',vintage(tmp_path,'2025-09-01,100\n2026-09-01,110'))
    assert s['status']=='Pass' and s['yoy']==pytest.approx(.1)

def test_stale_signal(tmp_path):
    assert evaluate_signal('2026-11-02',vintage(tmp_path,'2024-01-01,100\n2025-01-01,110'))['status']=='Not Known'

@pytest.mark.parametrize('body',['Date,A\n','Date,A\n2025-01-31,100\n2025-01-31,101','Date,A\n,100\n2025-02-28,101'])
def test_empty_duplicate_missing_dates(tmp_path,body):
    p=tmp_path/'p.csv';p.write_text(body)
    with pytest.raises((ValueError,TypeError)):load_prices(p)

def test_empty_estimates():
    with pytest.raises(ValueError):estimates(pd.DataFrame())

def test_empty_expected_returns():
    with pytest.raises(ValueError):validate([],np.empty((0,0)))

@pytest.mark.parametrize('cov',[np.zeros((2,2)),np.array([[np.nan,0],[0,1]])])
def test_invalid_inverse_volatility(cov):
    with pytest.raises(ValueError):inverse_volatility(cov)

def test_singular_covariance_valid():
    c=load_config();c['real_return_objective']=0;c['cpi_assumption']=0
    r=optimize([.1,.1],[[.01,.01],[.01,.01]],c,0)
    assert r['success'] and sum(r['weights'])==pytest.approx(1)
    m=metrics([.5,.5],[.1,.1],np.zeros((2,2)),c)
    assert m['volatility']==0 and m['estimated_sharpe_bil_proxy'] is None

def test_fixed_bounds_solver():
    c=load_config();c['min_weight']=.25;c['max_weight']=.25;c['real_return_objective']=0;c['cpi_assumption']=0
    r=optimize([.1]*4,np.eye(4)*.01,c,.03)
    assert r['success'] and r['weights']==pytest.approx([.25]*4)

def test_compounding_and_sharpe_units():
    c=load_config();r=realized_returns(pd.DataFrame([[.1],[.1]]),[1])
    assert math.prod(1+x for x in r)-1==pytest.approx(.21) # not .20
    m=metrics([0,1],[.02,.08],np.diag([.0001,.04]),c)
    assert m['estimated_sharpe_bil_proxy']==pytest.approx(.3)

def test_actual_turnover_not_certified_by_one_rebalance():
    c=load_config();c['current_weights']=[1,0,0,0]
    r=rules([1,0,0,0],[.1]*4,np.eye(4)*.01,c,.03)
    assert r['rules']['Single-rebalance turnover approximation <=20%'] is True
    assert r['rules']['Actual annual turnover <=20% (trade ledger required)'] is None

def test_invalid_universe():
    c=load_config();c['funds'][0]='INVALID'
    with pytest.raises(ValueError,match='universe'):run(c)

def test_extreme_negative_returns():
    c=load_config();c['mean_overrides']={t:-.99 for t in c['funds']}
    assert run(c)['solver']['success'] is False

def test_holdout_does_not_use_present_holdings():
    a=run();c=load_config();c['current_weights']=[0,0,0,1]
    b=run(c)
    assert b['holdout']['results']==a['holdout']['results']

def test_cost_control_has_measured_sensitivity():
    c=load_config();c['trading_cost_bps']=10;a=run(c)
    c['trading_cost_bps']=50;b=run(c)
    x=a['stress'][2]['transition_cost_sensitivity'];y=b['stress'][2]['transition_cost_sensitivity']
    assert y['at_sidebar_bps']==pytest.approx(5*x['at_sidebar_bps']) and x['at_sidebar_bps']>0

def test_stale_price_stop(monkeypatch):
    import src.workflow as w
    c=load_config();c['max_price_age_days']=1
    r=w.run(c);assert r['decision']['status']=='Fail' and any('freshness' in x for x in r['warnings'])

def test_unavailable_signal_stop(monkeypatch):
    import src.workflow as w
    monkeypatch.setattr(w,'evaluate_signal',lambda _: {'status':'Not Known','yoy':None})
    assert w.run()['decision']['status']=='Fail'

def test_independent_all_portfolios_from_raw_prices():
    # Plain Python sums/sample covariance; no production estimates function used.
    prices=load_prices();columns=[prices[t].tolist() for t in prices.columns]
    returns=[[column[i]/column[i-1]-1 for column in columns] for i in range(1,len(columns[0]))]
    means=[sum(row[j] for row in returns)/len(returns) for j in range(4)]
    cov=[[sum((row[j]-means[j])*(row[k]-means[k]) for row in returns)/(len(returns)-1)*12 for k in range(4)] for j in range(4)]
    r=run()
    for p in list(r['portfolios'].values())+[r['benchmark']]:
        w=p['weights'];expected=sum(w[j]*means[j]*12 for j in range(4))
        var=sum(w[j]*w[k]*cov[j][k] for j in range(4) for k in range(4))
        assert p['expected_return']==pytest.approx(expected,abs=1e-12)
        assert p['variance']==pytest.approx(var,abs=1e-12)


def test_unknown_mandate_fails_authorization_without_false_rule_failure():
    r=run()['portfolios']['Constrained']['compliance']
    assert r['mandate_status']=='Not Known' and not r['failed']
    assert r['authorization_gate']=='Fail' and r['authorization_reasons']
