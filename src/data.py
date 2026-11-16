"""Strict monthly adjusted-price handling; no forward filling."""
import json
from pathlib import Path
import numpy as np
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]

def load_prices(path=None):
    frame=pd.read_csv(path or ROOT/'data/processed/prices.csv',parse_dates=['Date']).set_index('Date')
    if frame.index.has_duplicates or not frame.index.is_monotonic_increasing:
        raise ValueError('Prices require unique increasing dates.')
    if frame.empty or not all(pd.api.types.is_numeric_dtype(t) for t in frame.dtypes):
        raise ValueError('Price columns must be numeric.')
    if np.isinf(frame.to_numpy()).any() or (frame<=0).any().any():
        raise ValueError('Prices must be positive and finite, or explicitly missing.')
    if frame.index.to_period('M').has_duplicates:raise ValueError('Only one price per calendar month.')
    # Expose absent months so pct_change cannot bridge them.
    periods=pd.period_range(frame.index[0].to_period('M'),frame.index[-1].to_period('M'),freq='M')
    frame.index=frame.index.to_period('M')
    frame=frame.reindex(periods)
    frame.index=frame.index.to_timestamp('M');frame.index.name='Date'
    return frame

def monthly_returns(prices):
    raw=prices.pct_change(fill_method=None)
    valid=raw.dropna(how='any')
    warnings=[]
    lost=int(raw.iloc[1:].isna().any(axis=1).sum())
    if lost:warnings.append(f'{lost} monthly return rows excluded due to missing observations; no filling or interval bridging.')
    if len(valid)<12:raise ValueError('At least twelve complete aligned return observations required.')
    return valid,warnings

def estimates(returns,months=None):
    r=returns.tail(months) if months else returns
    if len(r)<12:raise ValueError('Insufficient estimation observations.')
    return r.mean().to_numpy()*12,r.cov(ddof=1).to_numpy()*12

def snapshot_metadata():
    return json.loads((ROOT/'data/raw/price_metadata.json').read_text())
