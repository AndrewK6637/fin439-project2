"""Download authentic public ALFRED snapshots; never synthesize vintage values."""
import argparse,hashlib,json,time,urllib.request
from datetime import datetime,timezone,date
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--vintage',default='2026-11-01');args=parser.parse_args()
    date.fromisoformat(args.vintage)
    folder=ROOT/'data/raw/signals';folder.mkdir(parents=True,exist_ok=True)
    url=f'https://alfred.stlouisfed.org/graph/alfredgraph.csv?id=CPIAUCSL&vintage_date={args.vintage}'
    target=folder/f'CPIAUCSL_{args.vintage}.csv'
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url,timeout=40) as r:raw=r.read()
            if not raw.decode('utf-8-sig').splitlines()[0].lower().startswith(('date,','observation_date,')):raise ValueError('Not a CSV response')
            target.write_bytes(raw)
            target.with_suffix('.meta.json').write_text(json.dumps({'url':url,'vintage':args.vintage,'series':'CPIAUCSL','retrieved_at':datetime.now(timezone.utc).isoformat(),'sha256':hashlib.sha256(raw).hexdigest(),'availability':'Present in historical ALFRED snapshot by cutoff; exact original release timestamp not inferred'},indent=2))
            print('Saved',target);return
        except Exception:
            if attempt==2:raise
            time.sleep(2**attempt)
if __name__=='__main__':main()
