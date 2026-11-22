"""Reproduce calculated results without overwriting the student-reviewed committee memo."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from src.workflow import run,comparison
DECISION_LINE="Reject deployment of Cedar's proposed portfolio process; reconsider only after the committee documents the missing mandate approvals and actual holdings/costs, reviews the proposed signal policy, and a rerun shows feasible allocations with acceptable after-cost stress results."

def mdtable(rows):
    cols=list(rows[0]);return '\n'.join(['| '+' | '.join(cols)+' |','| '+' | '.join(['---']*len(cols))+' |']+['| '+' | '.join(str(r[k]).replace('|','/') for k in cols)+' |' for r in rows])
def main():
    r=run();(ROOT/'outputs/results.json').write_text(json.dumps(r,indent=2,allow_nan=False),encoding='utf-8')
    rows=comparison(r);brief=[{k:v for k,v in x.items() if k not in ['Unknown rules','Failed rules']} for x in rows]
    stresses=[]
    for s in r['stress']:
        stresses.append({'Scenario':s['scenario'],'Solver':'Pass' if s['success'] else 'Fail','Weights BIL/IEF/LQD/VT':' / '.join(f'{w:.2%}' for w in s['weights']) if s['success'] else 'Unavailable',
                        'Annual mean estimate':f"{s['expected_return']:.2%}" if s['success'] else 'Unavailable','Volatility':f"{s['volatility']:.2%}" if s['success'] else 'Unavailable','Largest weight move':f"{s['largest_weight_change']*100:.2f} pp" if s['success'] else 'Unavailable'})
    visible='# Visible executed output\n\n'+f"As-of: {r['as_of']}. Price end: {r['price_end']}. Estimates from {r['estimate_start']}. All returns and risks are annualized decimals displayed as percentages.\n\n"+mdtable(rows)+'\n\n## Stress results\n\n'+mdtable(stresses)+'\n\n## Decision\n\n'+json.dumps(r['decision'],indent=2)+'\n\n## Chronological holdout (revised snapshot, not PIT backtest)\n\n'+json.dumps(r['holdout'],indent=2)
    (ROOT/'outputs/visible-results.md').write_text(visible,encoding='utf-8')
    print(mdtable(brief));print('Calculated reports regenerated; reviewed decision memo and locked experiment were not changed.')
if __name__=='__main__':main()
