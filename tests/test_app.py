from streamlit.testing.v1 import AppTest
from src.data import ROOT

def test_dashboard_controls():
    at=AppTest.from_file(str(ROOT/'app.py'),default_timeout=60).run()
    assert not at.exception and len(at.tabs)==6
    at.selectbox[0].set_value(36).run();assert not at.exception
    at.slider[1].set_value(10).run();assert not at.exception
    assert any('No verified feasible' in e.value for e in at.error)


def test_expected_return_controls_and_extreme_infeasibility():
    at=AppTest.from_file(str(ROOT/'app.py'),default_timeout=60).run()
    next(x for x in at.checkbox if x.label=='Use analyst return assumptions').check().run()
    assert not at.exception
    for ticker in ['BIL','IEF','LQD','VT']:
        next(x for x in at.number_input if x.label==ticker+' annual expected return (%)').set_value(-99.0)
    at.run()
    assert not at.exception
    assert any('No verified feasible' in e.value for e in at.error)


def test_missing_data_shows_error_not_exception(monkeypatch):
    import src.workflow as workflow
    import streamlit as st
    def unavailable(*args,**kwargs):raise ValueError('Missing data audit fixture')
    monkeypatch.setattr(workflow,'run',unavailable);st.cache_data.clear()
    at=AppTest.from_file(str(ROOT/'app.py'),default_timeout=60).run()
    assert not at.exception and any('Missing data audit fixture' in x.value for x in at.error)
    st.cache_data.clear()
