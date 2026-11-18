"""STUDENT-RUN ONLY after genuine AI-off prediction is committed and pushed."""
import argparse,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))

def git(*args):
    return subprocess.check_output(['git','-C',str(ROOT),*args],text=True).strip()

def verify_frozen_model(commit):
    # Freeze the actual model and data as well as the prediction. No model run occurs here.
    material=['src','config','data','scripts/locked_experiment.py','requirements-lock.txt']
    if git('status','--porcelain','--',*material):raise ValueError('Material model/input files have uncommitted changes.')
    if git('diff','--name-only',commit,'HEAD','--',*material):raise ValueError('Model/input files changed after the prediction commit; establish a new AI-off prediction.')

def verify_prediction(commit,remote_branch):
    spec=json.loads(git('show',f'{commit}:config/locked_experiment.json'))
    for field in ['student_prediction','student_reasoning','expected_output_direction','expected_decision_effect']:
        if not spec.get(field,'').strip():raise ValueError(f'STUDENT ACTION REQUIRED: {field} must be genuinely authored with AI off before committing.')
    if spec['experiment_id']!='cedar-reserve-85' or spec['original']!=.03 or spec['changed']!=.85:raise ValueError('Experiment definition changed; establish a new pre-run protocol.')
    if git('status','--porcelain','--','config/locked_experiment.json'):raise ValueError('Prediction file has uncommitted changes.')
    if git('show',f'{commit}:config/locked_experiment.json')!=(ROOT/'config/locked_experiment.json').read_text().strip():raise ValueError('Working prediction differs from committed prediction.')
    verify_frozen_model(commit)
    remote=git('remote','get-url','origin')
    if not (remote.startswith('https://github.com/') or remote.startswith('git@github.com:')):raise ValueError('Origin must identify the actual student GitHub repository.')
    line=git('ls-remote','origin',f'refs/heads/{remote_branch}')
    if not line:raise ValueError('Remote branch not found.')
    tip=line.split()[0]
    subprocess.run(['git','-C',str(ROOT),'merge-base','--is-ancestor',commit,tip],check=True)
    return spec,remote,tip

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--prediction-commit',required=True);parser.add_argument('--remote-branch',default='main');parser.add_argument('--student-ai-off-run',action='store_true');args=parser.parse_args()
    if not args.student_ai_off_run:parser.error('STUDENT ACTION REQUIRED: close AI assistance and execute this run yourself.')
    spec,remote,tip=verify_prediction(args.prediction_commit,args.remote_branch)
    output=ROOT/'outputs/locked_changed_input.json'
    if output.exists():raise SystemExit('An experiment result already exists; preserve it instead of overwriting.')
    from src.workflow import load_config,run
    config=load_config();before=run(config);config[spec['input']]=spec['changed'];after=run(config)
    output.write_text(json.dumps({'prediction_commit':args.prediction_commit,'remote':remote,'verified_remote_tip':tip,'spec':spec,'before':before,'after':after},indent=2))
    print('Result saved. Complete the reconciliation yourself in docs/changed-input-record.md.')
if __name__=='__main__':main()
