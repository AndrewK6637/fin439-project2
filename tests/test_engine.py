import copy,json
import numpy as np
import pandas as pd
import pytest
from src.data import load_prices,monthly_returns,estimates,ROOT
from src.engine import *
from src.signal import evaluate_signal,effective_reserve
from src.workflow import load_config,run,stress_cases,stop_decision

@pytest.fixture
def cfg():return load_config()

def test_manual_two_asset_variance(cfg):
    mu=np.array([.05,.08]);cov=np.array([[.06**2,.25*.06*.16],[.25*.06*.16,.16**2]])
    r=metrics([.4,.6],mu,cov,cfg)
    assert r['expected_return']==pytest.approx(.068)
    # 0.16*0.0036 + 0.36*0.0256 + 2*0.4*0.6*0.0024 = 0.010944
    assert r['variance']==pytest.approx(.010944)
    assert r['volatility']==pytest.approx(.104613574)

def test_equal_inverse():
    assert equal_weight(4)==pytest.approx([.25]*4)
    assert inverse_volatility(np.diag([.01,.04]))==pytest.approx([2/3,1/3])

def test_returns_and_annualization():
    r=pd.DataFrame({'A':[.01,.03]*6,'B':[.02,.04]*6})
    mu,cov=estimates(r)
    assert mu==pytest.approx([.24,.36])
    assert cov==pytest.approx(np.full((2,2),12*.0012/11))

def test_realized_drift_not_monthly_rebalance():
    r=pd.DataFrame([[1.,0.],[0.,1.]])
    assert realized_returns(r,[.5,.5])==pytest.approx([.5,1/3])

def test_return_calculation_no_fill():
    frame=pd.DataFrame({'A':[100*1.01**i for i in range(15)]},index=pd.date_range('2025-01-31',periods=15,freq='ME'))
    ret,w=monthly_returns(frame);assert ret.A.to_numpy()==pytest.approx(np.full(14,.01));assert not w
    frame.iloc[5]=np.nan;ret,w=monthly_returns(frame)
    assert len(ret)==12 and w and pd.Timestamp('2025-06-30') not in ret.index and pd.Timestamp('2025-07-31') not in ret.index

def test_missing_month_not_bridged(tmp_path):
    f=pd.DataFrame({'Date':pd.date_range('2024-01-31',periods=16,freq='ME'),'A':np.arange(100,116)}).drop(5)
    path=tmp_path/'p.csv';f.to_csv(path,index=False);prices=load_prices(path)
    assert prices.loc['2024-06-30'].isna().all()
    r,w=monthly_returns(prices);assert w and len(r)==13

@pytest.mark.parametrize('values',[[0,1],[-1,1],[np.inf,1]])
def test_bad_prices(tmp_path,values):
    path=tmp_path/'p.csv';pd.DataFrame({'Date':['2024-01-31','2024-02-29'],'A':values}).to_csv(path,index=False)
    with pytest.raises(ValueError):load_prices(path)

@pytest.mark.parametrize('cov',[[[1,2],[0,1]],[[1,2],[2,1]],[[1,np.nan],[np.nan,1]]])
def test_bad_covariance(cov):
    with pytest.raises(ValueError):validate([.1,.2],cov)

def test_optimizer_constraints(cfg):
    mu=np.array([.03,.04,.05,.10]);cov=np.diag([.01,.03,.05,.15])**2
    c=copy.deepcopy(cfg);c['max_weight']=.6
    result=optimize(mu,cov,c,.03);assert result['success']
    w=np.array(result['weights']);assert w.sum()==pytest.approx(1);assert min(w)>=-1e-7;assert max(w)<=.6+1e-7
    assert w[0]>=.03-1e-7 and w@mu>=.055-1e-7
    assert not result['verified']['failed']

def test_known_two_asset_minimum(cfg):
    c=copy.deepcopy(cfg);c['cpi_assumption']=0;c['real_return_objective']=0
    r=optimize(np.array([.1,.1]),np.diag([.01,.04]),c,0)
    assert r['success'] and r['weights']==pytest.approx([.8,.2],abs=1e-5)

@pytest.mark.parametrize('kind',['bounds','return','risk','reserve'])
def test_infeasible(cfg,kind):
    c=copy.deepcopy(cfg);floor=.03
    if kind=='bounds':c['max_weight']=.2
    if kind=='return':c['cpi_assumption']=.5
    if kind=='risk':c['risk_limit']=.000001
    if kind=='reserve':floor=1.1
    r=optimize(np.array([.03,.04,.05,.10]),np.diag([.01,.03,.05,.15])**2,c,floor)
    assert not r['success'] and r['weights'] is None

def test_actual_turnover_unknown(cfg):
    r=metrics([.25]*4,[.01]*4,np.eye(4)*.01,cfg)
    assert r['turnover'] is None and r['net_first_year_return'] is None

def test_turnover_cost_units(cfg):
    c=copy.deepcopy(cfg);c['current_weights']=[.5,.5,0,0];c['trading_cost_bps']=50
    r=metrics([.25]*4,[.10]*4,np.eye(4)*.01,c)
    assert r['turnover']==.5;assert r['trading_cost']==pytest.approx(.005);assert r['net_first_year_return']==pytest.approx(.095)

def test_rule_fail_and_unknown(cfg):
    r=rules([0,0,.4,.6],[.04]*4,np.eye(4)*.01,cfg,.03)
    assert r['mandate_status']=='Fail' and 'BIL reserve floor' in r['failed']
    assert 'Numeric volatility cap' in r['unknown']

def test_signal_cutoff_and_transform():
    s=evaluate_signal('2026-11-02');assert s['status']=='Pass' and s['cutoff']=='2026-11-01'
    assert s['observation_date']<=s['cutoff']
    assert s['yoy']==pytest.approx(s['value']/s['prior_value']-1)
    assert evaluate_signal('2026-11-03')['status']=='Not Known'

def test_signal_policy(cfg):
    assert effective_reserve(cfg,{'status':'Pass','yoy':.04})==.05
    assert effective_reserve(cfg,{'status':'Pass','yoy':.02})==.03
    assert effective_reserve(cfg,{'status':'Not Known','yoy':None})==.03

def test_signal_rejects_wrong_vintage(tmp_path):
    path=tmp_path/'x.csv';path.write_text('date,CPIAUCSL\n2026-01-01,100')
    path.with_suffix('.meta.json').write_text(json.dumps({'vintage':'2099-01-01','url':'https://alfred.stlouisfed.org/test'}))
    assert evaluate_signal('2026-11-02',path)['status']=='Not Known'

def test_end_to_end_and_stresses():
    r=run();assert len(r['portfolios'])==3 and len(r['stress'])==4
    assert r['decision']['recommendation']=='Reject'
    assert r['portfolios']['Constrained']['compliance']['mandate_status']=='Not Known'
    assert r['holdout']['train_end']<r['holdout']['evaluation_start']
    assert r['as_of']>r['price_end']

def test_stop_on_invalid_signal(cfg):
    d=stop_decision({'success':True},{'status':'Not Known'},[],cfg,[])
    assert d['status']=='Fail' and d['recommendation']=='Reject'

def test_stop_on_stability(cfg):
    d=stop_decision({'success':True},{'status':'Pass'},[],cfg,[{'success':True,'largest_weight_change':.3}])
    assert d['status']=='Fail'

def test_recovered_lab15_estimates():
    old=json.loads((ROOT/'recovered/Lab15/project2_results.json').read_text())
    ret,_=monthly_returns(load_prices());mu,cov=estimates(ret)
    expected=old['all_months']['estimates']['sleeves']
    assert mu==pytest.approx([expected[t][0] for t in ['BIL','IEF','LQD','VT']])
    assert np.sqrt(np.diag(cov))==pytest.approx([expected[t][1] for t in ['BIL','IEF','LQD','VT']])


def test_explicit_return_override():
    from src.workflow import run,load_config
    c=load_config();c['mean_overrides']={'VT':.08}
    r=run(c)
    assert r['mean_estimates'][-1]==.08
