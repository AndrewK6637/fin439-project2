"""Single workflow reused by CLI, dashboard, and reports."""
import copy,json
import numpy as np
import pandas as pd
from .data import ROOT,load_prices,monthly_returns,estimates,snapshot_metadata
from .signal import evaluate_signal,effective_reserve
from .engine import metrics,rules,optimize,equal_weight,inverse_volatility,realized_returns

def load_config():return json.loads((ROOT/'config/mandate.json').read_text())

def stress_cases(returns,mu,cov,config,floor,base_weights):
    cases=[]
    for name in ['VT return estimate minus 1 percentage point','Last 36 monthly observations','Trading cost 50 bps per side','Maximum fund weight 70%']:
        c=copy.deepcopy(config);m=mu.copy();s=cov.copy();f=floor
        if name.startswith('VT'):m[-1]-=.01
        elif name.startswith('Last'):m,s=estimates(returns,36)
        elif name.startswith('Trading'):
            c['trading_cost_bps']=50
            # Explicit hypothetical transition from baseline candidate; not actual holdings.
            c['current_weights']=base_weights
        else:c['max_weight']=min(c['max_weight'],.70)
        result=optimize(m,s,c,f)
        row={'scenario':name,'success':result['success'],'message':result['message'],'weights':result['weights'],'assumption':'Scenario, not a new client mandate'}
        if result['success']:
            row.update(metrics(result['weights'],m,s,c));row['largest_weight_change']=float(np.max(np.abs(np.array(result['weights'])-base_weights)))
            row['mandate']=rules(result['weights'],m,s,c,f)
            if name.startswith('Trading'):
                transition_turnover=.5*float(np.abs(np.array(base_weights)-equal_weight(len(mu))).sum())
                row['cost_of_baseline_to_equal_weight']=2*transition_turnover*.005
                row['transition_cost_sensitivity']={'hypothetical_one_way_turnover':transition_turnover,
                    'at_sidebar_bps':2*transition_turnover*config['trading_cost_bps']/10000,
                    'at_stress_50bps':2*transition_turnover*.005,
                    'note':'Baseline-to-equal-weight illustration only; not a recommended trade or actual holdings.'}
        cases.append(row)
    return cases

def stop_decision(solver,signal,warnings,config,stress):
    failed=[];unknown=[]
    if not solver['success']:failed.append('Optimization failed or is infeasible')
    if signal['status']!='Pass':failed.append('Point-in-time signal unavailable or invalid')
    failed.extend(warnings)
    if any(not s['success'] for s in stress):failed.append('At least one required stress scenario is infeasible')
    if any(s.get('largest_weight_change',0)>config['max_weight_instability'] for s in stress):failed.append('Scenario weight instability exceeds analyst 20-percentage-point stop rule')
    if config['risk_limit'] is None:unknown.append('Cedar numeric risk limit not documented')
    if config.get('current_weights') is None:unknown.append('Actual holdings/trades unavailable; turnover and transition costs unverified')
    if not config['reserve_proxy_confirmed']:unknown.append('BIL reserve-proxy acceptance not confirmed')
    if not config['signal_confirmed']:unknown.append('Student selected CPI fallback; personal source-value checks and final evidence review remain incomplete')
    unknown.extend(['Cedar benchmark approval not recovered','Forward CPI and cost assumptions not client-confirmed','Realized rolling-five-year real objective is not established by an arithmetic estimate'])
    status='Fail' if failed else 'Not Known' if unknown else 'Pass'
    # Reject deployment when evidence is insufficient; no automatic favorable recommendation.
    return {'status':status,'failed':failed,'unknown':unknown,'recommendation':'Reject' if status!='Pass' else 'Pilot',
      'committee_ask':'Reject deployment pending resolution of the listed failures and unknowns; retain the app for analytical review.' if status!='Pass' else 'Authorize a monitored pilot only.',
      'new_process_allocation_range':'0%-0% pending evidence clearance' if status!='Pass' else '0%-5% pilot, subject to committee authorization'}

def run(config=None):
    c=copy.deepcopy(config or load_config());prices=load_prices();
    if list(prices.columns)!=c['funds']:raise ValueError('Price universe differs from recovered mandate.')
    prices=prices.loc[prices.index<pd.Timestamp(c['decision_date'])]
    returns,warnings=monthly_returns(prices);mu,cov=estimates(returns,c['estimation_months'])
    overrides=c.get('mean_overrides',{})
    for ticker,value in overrides.items():
        if ticker not in c['funds'] or not np.isfinite(value):raise ValueError('Invalid expected-return override')
        mu[c['funds'].index(ticker)]=float(value)
    if (pd.Timestamp(c['decision_date'])-prices.index[-1]).days>c['max_price_age_days']:warnings.append('Prices exceed analyst freshness threshold')
    for item in snapshot_metadata():
        if pd.Timestamp(item['downloaded_at_utc']).tz_localize(None)>=pd.Timestamp(c['decision_date']):warnings.append('Price snapshot was retrieved after decision date; historical availability not established');break
    signal=evaluate_signal(c['decision_date']);floor=effective_reserve(c,signal);solution=optimize(mu,cov,c,floor)
    choices={'Equal weight':equal_weight(len(mu)),'Inverse volatility':inverse_volatility(cov)}
    if solution['success']:choices['Constrained']=solution['weights']
    portfolios={name:{**metrics(w,mu,cov,c),'compliance':rules(w,mu,cov,c,floor)} for name,w in choices.items()}
    benchmark=metrics(c['benchmark'],mu,cov,c)
    for item in portfolios.values():item['estimated_return_vs_benchmark']=item['expected_return']-benchmark['expected_return']
    stress=stress_cases(returns,mu,cov,c,floor,solution['weights']) if solution['success'] else []
    decision=stop_decision(solution,signal,warnings,c,stress)
    # Chronological diagnostic re-estimates on training only; uses revised price snapshot.
    train,test=returns.iloc[:-12],returns.iloc[-12:];tm,tc=estimates(train)
    historical_config=copy.deepcopy(c);historical_config['current_weights']=None
    historical_solution=optimize(tm,tc,historical_config,c['reserve_min'])
    holdout={'label':'Chronological holdout diagnostic using a later downloaded adjusted-price snapshot; NOT a point-in-time implementable backtest. Signal not applied retrospectively.',
      'train_end':str(train.index[-1].date()),'evaluation_start':str(test.index[0].date()),'evaluation_end':str(test.index[-1].date()),'constrained_solver_status':historical_solution['message'],'results':{}}
    historical_choices={'Equal weight':equal_weight(len(mu)),'Inverse volatility':inverse_volatility(tc),'Benchmark':c['benchmark']}
    if historical_solution['success']:historical_choices['Constrained']=historical_solution['weights']
    for name,w in historical_choices.items():
        rr=realized_returns(test,w);holdout['results'][name]={'weights':list(w),'realized_gross_return':float(np.prod(1+rr)-1),'realized_volatility':float(np.std(rr,ddof=1)*np.sqrt(12))}
    return {'config':c,'as_of':c['decision_date'],'price_end':str(prices.index[-1].date()),'estimate_start':str(returns.tail(c['estimation_months']).index[0].date()),
      'observations':len(returns.tail(c['estimation_months'])),'mean_estimates':mu.tolist(),'covariance':cov.tolist(),'signal':signal,'effective_reserve_floor':floor,
      'portfolios':portfolios,'benchmark':benchmark,'solver':solution,'stress':stress,'decision':decision,'warnings':warnings,'holdout':holdout}

def comparison(result):
    return [{'Portfolio':name,**{t:f'{w:.2%}' for t,w in zip(result['config']['funds'],p['weights'])},
      'Annual mean estimate':f"{p['expected_return']:.2%}",'Annual volatility':f"{p['volatility']:.2%}",
      'Mandate':p['compliance']['mandate_status'],'Authorization gate':p['compliance']['authorization_gate'],
      'Mean vs benchmark':f"{p['estimated_return_vs_benchmark']*100:+.2f} pp",'Failed rules':'; '.join(p['compliance']['failed']) or 'None among testable rules',
      'Unknown rules':'; '.join(p['compliance']['unknown'])} for name,p in result['portfolios'].items()]

if __name__=='__main__':
    result=run();(ROOT/'outputs/results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(comparison(result),indent=2));print(json.dumps(result['decision'],indent=2))
