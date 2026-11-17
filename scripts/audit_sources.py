from pathlib import Path
import hashlib,json
import numpy as np
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
def audit():
    prices=pd.read_csv(ROOT/'data/processed/prices.csv',index_col='Date');rows=[]
    for ticker in prices.columns:
        p=ROOT/f'data/raw/{ticker}_monthly.json';j=json.loads(p.read_text())['chart']['result'][0]
        months=pd.to_datetime(j['timestamp'],unit='s',utc=True).tz_convert('America/New_York').tz_localize(None).to_period('M').to_timestamp('M').strftime('%Y-%m-%d')
        raw=pd.Series(j['indicators']['adjclose'][0]['adjclose'],index=months)
        aligned=raw.reindex(prices.index);delta=float(np.max(np.abs(aligned.to_numpy()-prices[ticker].to_numpy())))
        if aligned.isna().any() or delta>1e-6:raise ValueError(f'{ticker} source reconciliation failed: {delta}')
        rows.append({'ticker':ticker,'observations':len(prices),'max_absolute_difference':delta,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
    inventory=json.loads((ROOT/'docs/recovery-inventory.json').read_text())
    for item in inventory:
        p=ROOT/item['copy']
        if hashlib.sha256(p.read_bytes()).hexdigest()!=item['sha256']:raise ValueError(f'Recovered copy changed: {p}')
    return {'prices':rows,'recovered_files_verified':len(inventory)}
if __name__=='__main__':
    result=audit();(ROOT/'outputs/source-audit.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
