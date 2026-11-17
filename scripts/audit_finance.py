"""Independent plain-Python financial reconciliation; does not use NumPy covariance."""
import csv,json,math,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from src.workflow import run
rows=list(csv.DictReader((ROOT/'data/processed/prices.csv').open()))
tickers=['BIL','IEF','LQD','VT']
returns=[[float(rows[i][t])/float(rows[i-1][t])-1 for t in tickers] for i in range(1,len(rows))]
n=len(returns);mean=[sum(x[j] for x in returns)/n for j in range(4)]
cov=[[12*sum((x[j]-mean[j])*(x[k]-mean[k]) for x in returns)/(n-1) for k in range(4)] for j in range(4)]
r=run();out={'method':'Python CSV, scalar sums, sample denominator n-1; no production estimator or NumPy covariance','observations':n,'portfolios':{}}
for name,p in {**r['portfolios'],'Benchmark':r['benchmark']}.items():
 w=p['weights'];mu=sum(w[j]*mean[j]*12 for j in range(4));var=sum(w[j]*cov[j][k]*w[k] for j in range(4) for k in range(4));vol=math.sqrt(var)
 assert abs(mu-p['expected_return'])<1e-12 and abs(vol-p['volatility'])<1e-12
 out['portfolios'][name]={'annual_mean':mu,'variance':var,'volatility':vol,'return_absolute_error':abs(mu-p['expected_return']),'volatility_absolute_error':abs(vol-p['volatility']),'weight_sum':sum(w)}
out['manual_examples']={'two_successive_10pct_returns_compounded':.21,'two_asset_return':.068,'two_asset_variance':.010944,'two_asset_volatility':math.sqrt(.010944),'20pct_turnover_50bps_per_side_cost':.002,'annual_excess_6pct_divided_by_20pct_volatility':.3}
(ROOT/'outputs/audit-independent-finance.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
