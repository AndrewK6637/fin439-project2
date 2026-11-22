import importlib.util
import json
from src.data import ROOT
import pytest

def test_blank_prediction_gate_does_not_run_model(monkeypatch):
    spec=importlib.util.spec_from_file_location('locked',ROOT/'scripts/locked_experiment.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    blank={'experiment_id':'cedar-reserve-85','original':.03,'changed':.85,
           'student_prediction':'','student_reasoning':'','expected_output_direction':'','expected_decision_effect':''}
    def fake_git(*args):
        if args[0]=='show':return json.dumps(blank)
        raise AssertionError('A blank prediction must stop before any repository or model check')
    monkeypatch.setattr(m,'git',fake_git)
    with pytest.raises(ValueError,match='STUDENT ACTION REQUIRED'):m.verify_prediction('not-a-real-commit','main')


@pytest.mark.parametrize('dirty,later_change',[(True,False),(False,True)])
def test_model_freeze_gate_without_student_prediction(monkeypatch,dirty,later_change):
    spec=importlib.util.spec_from_file_location('locked',ROOT/'scripts/locked_experiment.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    def fake_git(*args):
        if args[0]=='status':return ' M src/engine.py' if dirty else ''
        if args[0]=='diff':return 'src/engine.py' if later_change else ''
        raise AssertionError('No remote or model operation allowed in this unit test')
    monkeypatch.setattr(m,'git',fake_git)
    with pytest.raises(ValueError):m.verify_frozen_model('unit-test-id-not-a-real-commit')
