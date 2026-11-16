import importlib.util
from src.data import ROOT
import pytest

def test_blank_prediction_gate_does_not_run_model(monkeypatch):
    spec=importlib.util.spec_from_file_location('locked',ROOT/'scripts/locked_experiment.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    monkeypatch.setattr(m,'git',lambda *args:(ROOT/'config/locked_experiment.json').read_text())
    with pytest.raises(ValueError,match='STUDENT ACTION REQUIRED'):m.verify_prediction('not-a-real-commit','main')
    assert not (ROOT/'outputs/locked_changed_input.json').exists()
