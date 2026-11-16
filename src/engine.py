"""Portfolio arithmetic, constraints and verified numerical optimization."""
import numpy as np
from scipy.optimize import minimize

TOL=1e-7

def validate(mu,cov):
    mu=np.asarray(mu,float);cov=np.asarray(cov,float)
    if cov.shape!=(len(mu),len(mu)) or not np.isfinite(mu).all() or not np.isfinite(cov).all():raise ValueError('Invalid estimate dimensions or nonfinite values.')
    if not np.allclose(cov,cov.T,atol=1e-12) or np.linalg.eigvalsh(cov).min() < -1e-10:raise ValueError('Covariance must be symmetric positive semidefinite.')
    return mu,cov

def equal_weight(n):
    if n<1:raise ValueError('Empty universe.')
    return np.ones(n)/n

def inverse_volatility(cov):
    vol=np.sqrt(np.diag(cov))
    if np.any(vol<=0):raise ValueError('Inverse volatility requires positive volatilities.')
    inverse=1/vol;return inverse/inverse.sum()

def turnover(weights,current):
    if current is None:return None
    current=np.asarray(current,float)
    if current.shape!=np.asarray(weights).shape or np.any(current<0) or not np.isclose(current.sum(),1):raise ValueError('Current weights must be a fully invested long-only vector.')
    return float(np.abs(np.asarray(weights)-current).sum()/2)

def metrics(weights,mu,cov,config):
    mu,cov=validate(mu,cov);w=np.asarray(weights,float)
    if w.shape!=mu.shape or not np.isfinite(w).all():raise ValueError('Invalid weights.')
    variance=float(w@cov@w);gross=float(w@mu)
    turn=turnover(w,config.get('current_weights'))
    # Cost per dollar bought or sold. One-way turnover counts only one side.
    trade_cost=None if turn is None else 2*turn*config['trading_cost_bps']/10000
    ongoing=config['ongoing_cost_bps']/10000
    return {'weights':w.tolist(),'expected_return':gross,'variance':variance,'volatility':float(np.sqrt(max(0,variance))),
      'net_return_before_trade_cost':gross-ongoing,'turnover':turn,'trading_cost':trade_cost,
      'net_first_year_return':None if trade_cost is None else gross-ongoing-trade_cost,
      'estimated_excess_return_over_bil':gross-float(mu[0]),'estimated_sharpe_bil_proxy':None if variance<=0 else (gross-mu[0])/np.sqrt(variance)}

def rules(weights,mu,cov,config,reserve_floor):
    m=metrics(weights,mu,cov,config);w=np.asarray(weights);target=config['cpi_assumption']+config['real_return_objective']
    result={'Weights sum to 100%':bool(abs(w.sum()-1)<=TOL),'Long only':bool(np.all(w>=-TOL)),
      'Position bounds':bool(np.all(w<=config['max_weight']+TOL) and np.all(w>=config['min_weight']-TOL)),
      'BIL reserve floor':bool(w[0]>=reserve_floor-TOL),
      'Liquidity >= mandate minimum (course fund classification)':bool(w.sum()>=config['liquidity_min']-TOL),
      'Direct nonexempt issuer <=5% (all allowed funds exempt)':True,
      'Illustrative return hurdle':bool(m['net_return_before_trade_cost']-(m['trading_cost'] or 0)>=target-TOL),
      'Numeric volatility cap':None if config['risk_limit'] is None else bool(m['volatility']<=config['risk_limit']+TOL),
      'Actual annual turnover <=20%':None if m['turnover'] is None else bool(m['turnover']<=config['annual_turnover_max']+TOL),
      'BIL reserve proxy approved':True if config['reserve_proxy_confirmed'] else None,
      'Realized rolling-five-year CPI+3% after costs':None}
    failed=[k for k,v in result.items() if v is False];unknown=[k for k,v in result.items() if v is None]
    return {'rules':result,'failed':failed,'unknown':unknown,'mandate_status':'Fail' if failed else 'Not Known' if unknown else 'Pass',
      'testable_constraints':'Fail' if failed else 'Pass'}

def optimize(mu,cov,config,reserve_floor):
    mu,cov=validate(mu,cov);n=len(mu);lower=np.full(n,config['min_weight']);lower[0]=max(lower[0],reserve_floor)
    upper=np.full(n,config['max_weight'])
    if np.any(lower>upper) or lower.sum()>1+TOL or upper.sum()<1-TOL:
        return {'success':False,'message':'Infeasible allocation bounds','weights':None}
    target=config['cpi_assumption']+config['real_return_objective']+config['ongoing_cost_bps']/10000
    def cost(w):
        turn=turnover(w,config.get('current_weights'));return 0 if turn is None else 2*turn*config['trading_cost_bps']/10000
    constraints=[{'type':'eq','fun':lambda w:w.sum()-1},{'type':'ineq','fun':lambda w:float(w@mu)-cost(w)-target}]
    if config['risk_limit'] is not None:constraints.append({'type':'ineq','fun':lambda w:config['risk_limit']**2-float(w@cov@w)})
    if config.get('current_weights') is not None:constraints.append({'type':'ineq','fun':lambda w:config['annual_turnover_max']-turnover(w,config['current_weights'])})
    x0=lower+(1-lower.sum())*(upper-lower)/(upper-lower).sum() if (upper-lower).sum()>0 else lower
    res=minimize(lambda w:float(w@cov@w)*10000,x0,method='SLSQP',bounds=list(zip(lower,upper)),constraints=constraints,options={'ftol':1e-11,'maxiter':1000})
    verified=rules(res.x,mu,cov,config,reserve_floor)
    success=bool(res.success and not verified['failed'])
    return {'success':success,'message':str(res.message),'weights':res.x.tolist() if success else None,'iterations':int(res.nit),'verified':verified}

def realized_returns(returns,weights):
    # Drift between annual rebalances; weights reset after every twelve monthly observations.
    w=np.asarray(weights,float);current=w.copy();out=[]
    for i,row in enumerate(returns.to_numpy()):
        if i%12==0:current=w.copy()
        value=float(current@row);out.append(value);current=current*(1+row)/(1+value)
    return np.asarray(out)
