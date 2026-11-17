import copy,json
import pandas as pd
import plotly.express as px
import streamlit as st
from src.data import ROOT,load_prices,monthly_returns
from src.workflow import run,load_config,comparison
st.set_page_config(page_title='Cedar | Investment Committee',page_icon='C',layout='wide')
st.title('Cedar Investment Committee')
st.caption('Built with OpenAI Codex assistance. Student review pending. Educational analysis, not investment advice.')
@st.cache_data(show_spinner=False)
def calculate(config_json):return run(json.loads(config_json))
base=load_config();c=copy.deepcopy(base)
with st.sidebar:
 st.header('Analytical assumptions')
 st.caption('Controls change scenarios, not the original client mandate.')
 c['estimation_months']=st.selectbox('Estimation months',[60,36,48])
 c['cpi_assumption']=st.number_input('Illustrative CPI assumption (%)',0.0,20.0,2.5,.1)/100
 c['ongoing_cost_bps']=st.number_input('Additional annual costs (bps)',0,500,0,5)
 c['trading_cost_bps']=st.number_input('Transaction cost per side (bps)',0,500,10,5)
 c['reserve_min']=st.slider('Analytical BIL reserve floor (%)',3,90,3)/100
 c['max_weight']=st.slider('Maximum fund weight (%)',10,100,100)/100
 use_risk=st.checkbox('Apply illustrative volatility cap')
 if use_risk:c['risk_limit']=st.number_input('Illustrative volatility cap (%)',0.1,50.0,10.0,.5)/100
 st.caption('Actual risk limit, current holdings, costs and BIL approval remain unconfirmed. Full compliance cannot be certified.')
 with st.expander('Override annual return estimates'):
  if st.checkbox('Use analyst return assumptions'):
   c['mean_overrides']={t:st.number_input(t+' annual expected return (%)',-100.0,100.0,5.5,.25)/100 for t in c['funds']}
 st.button('Rerun model',type='primary')
try:
 with st.spinner('Calculating allocations and checking constraints...'):r=calculate(json.dumps(c,sort_keys=True))
except Exception as e:
 st.error(f'Unable to evaluate: {e}');st.stop()
tabs=st.tabs(['Executive dashboard','Portfolio construction','Portfolio comparison','Point-in-time signal','Stress testing','Committee recommendation'])
with tabs[0]:
 st.subheader(r['decision']['recommendation']+' deployment - draft for student review')
 st.warning(r['decision']['committee_ask'])
 st.write('**Client:** Cedar Scholarship Foundation; assets $20 million; ten-year horizon; quarterly scholarships $150,000.')
 st.write('**Objective:** CPI + 3% annually after costs over rolling five-year periods. **Universe:** BIL, IEF, LQD, VT. **Comparator:** 60% VT / 40% LQD, inherited from Lab 14; Cedar approval not recovered.')
 st.write('**Constraints:** long only, fully invested; $600,000 reserve; 95% five-day liquidity; 5% nonexempt direct issuer cap; annual rebalancing and 20% annual one-way turnover cap.')
 st.caption(f"Frozen research decision: {r['as_of']} | Latest price month: {r['price_end']} | Historical estimation observations: {r['observations']}")
 if r['solver']['success']:
  p=r['portfolios']['Constrained'];a,b,d=st.columns(3);a.metric('Annual mean estimate',f"{p['expected_return']:.2%}");b.metric('Annual volatility',f"{p['volatility']:.2%}");d.metric('Full mandate',p['compliance']['mandate_status'])
 else:st.error('No verified feasible constrained portfolio: '+r['solver']['message'])
 st.write('Process status:',r['decision']['status']);st.json({'Failed':r['decision']['failed'],'Unresolved':r['decision']['unknown']})
with tabs[1]:
 st.subheader('Recovered fund universe and adjusted-price data')
 st.dataframe(load_prices(),width='stretch')
 st.caption('Recovered Yahoo monthly Adj Close, 2026-10-20 download. Includes payout/split adjustment per Lab 14; provider-adjusted return proxy, not independently reconstructed total returns. No forward filling.')
 mu=pd.DataFrame({'Fund':c['funds'],'Annual arithmetic mean':r['mean_estimates']})
 st.dataframe(mu,hide_index=True);st.dataframe(pd.DataFrame(r['covariance'],index=c['funds'],columns=c['funds']))
 st.write('Objective: minimize variance subject to the illustrative return hurdle and explicit allocation constraints. Solver results are independently rechecked.')
 st.json(r['solver'])
 if r['solver']['success']:st.plotly_chart(px.bar(x=c['funds'],y=r['solver']['weights'],labels={'x':'Fund','y':'Weight'},title='Constrained research allocation'),width='stretch')
with tabs[2]:
 st.subheader('Same mandate, different construction rules')
 st.dataframe(pd.DataFrame(comparison(r)),hide_index=True,width='stretch')
 st.write(f"Benchmark annual mean estimate: {r['benchmark']['expected_return']:.2%}; volatility: {r['benchmark']['volatility']:.2%}.")
 st.caption('Authorization gate is Pass/Fail: missing evidence fails authorization while its underlying financial rule remains Not Known. Pass among testable constraints is not full mandate compliance. Unknown inputs stay Not Known. Equal weight and inverse volatility are not repaired to hide failures.')
 allocation=pd.DataFrame({name:p['weights'] for name,p in r['portfolios'].items()},index=c['funds']);st.bar_chart(allocation)
 st.subheader('Separate chronological holdout diagnostic')
 st.warning(r['holdout']['label']);st.json(r['holdout'])
with tabs[3]:
 st.subheader('Proposed fallback: inflation pressure')
 st.write('CPIAUCSL, monthly seasonally adjusted CPI index. YoY = latest index / same-month prior-year index - 1. The signal uses the ALFRED snapshot dated the calendar day before the decision.')
 st.json({k:v for k,v in r['signal'].items() if k!='history'})
 if r['signal'].get('history'):st.line_chart(pd.DataFrame(r['signal']['history']).set_index('date'))
 st.write(f"Effective analytical BIL floor: {r['effective_reserve_floor']:.2%}. Proposed policy raises the floor to 5% when observed YoY inflation exceeds 3%, without reducing the client's reserve minimum.")
 st.warning('Lab 17 left the Project 2 signal quarantined. This proposed signal has genuine vintage evidence but is not represented as your prior selection or approval.')
 card=ROOT/'docs/signal-data-card.md'
 if card.exists():st.markdown(card.read_text(encoding='utf-8'))
with tabs[4]:
 st.subheader('Required robustness checks')
 st.error('STOP deployment on infeasibility, invalid/missing signal, stale prices, or more than 20 percentage points of weight instability. Unresolved mandate evidence also blocks authorization.')
 for s in r['stress']:
  with st.expander(s['scenario'],expanded=True):st.json(s)
 if r['stress']:
  st.caption('Transaction-cost control: inspect transition_cost_sensitivity for a nonzero hypothetical rebalance. Actual client costs cannot be computed without holdings.')
 st.write('For customized input stresses, change the sidebar controls. Cost stress uses an explicitly hypothetical baseline holding vector; actual client turnover is unknown.')
 st.info('The separate Locked Changed-Input Record is not run here. Its student-authored AI-off prediction must be committed to GitHub before execution.')
with tabs[5]:
 st.subheader('Evidence-based committee ask')
 st.write(r['decision']['committee_ask']);st.write('New-process allocation range:',r['decision']['new_process_allocation_range'])
 st.write('Monitor: reserve coverage, net real outcomes, annual turnover, signal vintage, price freshness, solver feasibility and allocation stability. Resolve the missing mandate evidence before revisiting deployment.')
 memo=ROOT/'docs/decision-memo.md'
 if memo.exists():
  st.caption('The saved memo below describes the frozen default run; customized results are shown above and in the download.')
  st.markdown(memo.read_text(encoding='utf-8'))
 st.download_button('Download this scenario',json.dumps(r,indent=2),file_name='cedar_scenario.json')
