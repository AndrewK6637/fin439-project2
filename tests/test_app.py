from streamlit.testing.v1 import AppTest
from src.data import ROOT

def test_dashboard_controls():
    at=AppTest.from_file(str(ROOT/'app.py'),default_timeout=60).run()
    assert not at.exception and len(at.tabs)==6
    at.selectbox[0].set_value(36).run();assert not at.exception
    at.slider[1].set_value(10).run();assert not at.exception
    assert any('No verified feasible' in e.value for e in at.error)
