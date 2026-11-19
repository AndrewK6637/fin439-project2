"""Lab 17's previous-calendar-day ALFRED admission rule."""
import json
import hashlib
import numpy as np
from urllib.parse import urlparse,parse_qs
from datetime import date,timedelta
import pandas as pd
from .data import ROOT

def evaluate_signal(decision_date, path=None):
    cutoff=(date.fromisoformat(decision_date)-timedelta(days=1)).isoformat()
    folder=ROOT/'data/raw/signals'
    csv=Path(path) if path else folder/f'CPIAUCSL_{cutoff}.csv'
    meta=csv.with_suffix('.meta.json')
    if not csv.exists() or not meta.exists():return {'status':'Not Known','reason':f'No authentic ALFRED snapshot for {cutoff}','cutoff':cutoff,'yoy':None}
    metadata=json.loads(meta.read_text())
    if not metadata.get('sha256') or hashlib.sha256(csv.read_bytes()).hexdigest()!=metadata['sha256']:
        return {'status':'Not Known','reason':'Signal snapshot checksum mismatch','cutoff':cutoff,'yoy':None}
    url=urlparse(metadata.get('url',''));query=parse_qs(url.query)
    if (metadata.get('vintage')!=cutoff or url.scheme!='https' or url.hostname!='alfred.stlouisfed.org'
        or query.get('id')!=['CPIAUCSL'] or query.get('vintage_date')!=[cutoff]):
        return {'status':'Not Known','reason':'Vintage identity does not match prior-day cutoff','cutoff':cutoff,'yoy':None}
    frame=pd.read_csv(csv,na_values=['.'])
    if len(frame.columns)!=2 or not frame.columns[1].startswith('CPIAUCSL'):raise ValueError('Wrong signal series.')
    frame.columns=['date','value'];frame['date']=pd.to_datetime(frame['date']);frame['value']=pd.to_numeric(frame['value'])
    if frame.date.duplicated().any():raise ValueError('Duplicate signal observation dates.')
    frame=frame.sort_values('date')
    if (frame.date>pd.Timestamp(cutoff)).any():return {'status':'Not Known','reason':'Observation after vintage cutoff','cutoff':cutoff,'yoy':None}
    if not frame.empty and (pd.isna(frame.iloc[-1].value) or not np.isfinite(frame.iloc[-1].value) or frame.iloc[-1].value<=0):
        return {'status':'Not Known','reason':'Latest CPI observation missing or invalid; no silent fallback','cutoff':cutoff,'yoy':None}
    if frame.empty:return {'status':'Not Known','reason':'Empty vintage','cutoff':cutoff,'yoy':None}
    last=frame.iloc[-1];prior_date=last.date-pd.DateOffset(years=1)
    prior=frame.loc[frame.date==prior_date,'value']
    if prior.empty or not np.isfinite(prior.iloc[0]) or prior.iloc[0]<=0:return {'status':'Not Known','reason':'Missing same-month prior-year CPI','cutoff':cutoff,'yoy':None}
    if (pd.Timestamp(cutoff)-last.date).days>100:return {'status':'Not Known','reason':'Signal observation older than 100 days','cutoff':cutoff,'yoy':None}
    return {'status':'Pass','reason':'Code verified vintage identity and prior-day cutoff; student-reported three-value spot check is documented separately; Cedar policy approval remains pending',
      'cutoff':cutoff,'observation_date':last.date.date().isoformat(),'value':float(last.value),'prior_value':float(prior.iloc[0]),
      'yoy':float(last.value/prior.iloc[0]-1),'metadata':metadata,'history':frame.tail(24).assign(date=lambda x:x.date.dt.strftime('%Y-%m-%d')).to_dict('records')}

from pathlib import Path

def effective_reserve(config,signal):
    floor=max(config['reserve_min'],4*config['quarterly_spending']/config['assets'])
    return max(floor,config['signal_reserve_floor']) if signal['status']=='Pass' and signal['yoy']>config['signal_trigger'] else floor
