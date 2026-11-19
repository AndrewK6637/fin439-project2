import copy,json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from src.data import ROOT,load_prices,monthly_returns
from src.workflow import run,load_config,comparison
st.set_page_config(page_title='Cedar | Investment Committee',page_icon='C',layout='wide')
st.markdown('''<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap');
html, body, [class*="css"], [data-testid="stAppViewContainer"] {font-family:'DM Sans',sans-serif;}
h1,h2,h3 {font-family:'Outfit',sans-serif!important;letter-spacing:-.025em;}
[data-testid="stAppViewContainer"] {background:radial-gradient(circle at 82% 0%,#e7f6ee 0,#f8fbf9 30%,#f8fbf9 100%);}
[data-testid="stSidebar"] {background:#102d29;}
[data-testid="stSidebar"] * {color:#f0f7f3!important;}
[data-testid="stSidebar"] [data-baseweb="input"] input {color:#102d29!important;}
[data-testid="stSidebar"] [data-baseweb="select"] * {color:#102d29!important;}
.block-container {padding-top:2rem;max-width:1480px;}
.cedar-hero {background:linear-gradient(115deg,#102d29,#155849 60%,#247b62);color:#fff;padding:2rem 2.3rem;border-radius:22px;box-shadow:0 16px 42px #103d3024;margin-bottom:1rem;}
.cedar-eyebrow {font-size:.73rem;font-weight:800;letter-spacing:.18em;text-transform:uppercase;color:#b9e5c9;margin-bottom:.5rem;}
.cedar-hero h1 {font-size:2.5rem;margin:0;color:#fff!important;line-height:1.08;}
.cedar-hero p {color:#d4e9df;margin:.7rem 0 0;font-size:1rem;}
.cedar-kicker {color:#36745f;font-size:.72rem;font-weight:800;letter-spacing:.16em;text-transform:uppercase;margin-top:1rem;}
[data-testid="stMetric"] {background:#fff;border:1px solid #dcebe2;border-radius:16px;padding:1rem 1.2rem;box-shadow:0 5px 20px #163b2910;}
[data-testid="stMetricLabel"] {font-weight:700;color:#48695a;}
[data-testid="stMetricValue"] {font-family:'Outfit',sans-serif;color:#103d31;}
[data-testid="stTabs"] button {font-weight:700;}
[data-testid="stAlert"] {border-radius:14px;}
div[data-testid="stDataFrame"], div[data-testid="stPlotlyChart"] {border-radius:16px;overflow:hidden;}
</style>''',unsafe_allow_html=True)
st.markdown('<div class="cedar-hero"><div class="cedar-eyebrow">FIN 439 · Project 2 · Research dashboard</div><h1>Cedar Investment Committee</h1><p>Portfolio construction, mandate evidence, and an honest deployment decision.</p></div>',unsafe_allow_html=True)
st.caption('Built with OpenAI Codex assistance. Student selected the analytical design; source checks and final review remain pending. Educational analysis, not investment advice.')
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
   try:
    reference=calculate(json.dumps(c,sort_keys=True))['mean_estimates']
   except Exception as e:
    st.error(f'Unable to load baseline return estimates: {e}');st.stop()
   c['mean_overrides']={t:st.number_input(t+' annual expected return (%)',-100.0,100.0,float(reference[i]*100),.25,format='%.4f')/100 for i,t in enumerate(c['funds'])}
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
  st.caption(f"After the additional annual cost assumption ({c['ongoing_cost_bps']} bps): {p['net_return_before_trade_cost']:.2%} estimated annual return before transition costs. Actual transition costs remain unverified without client holdings.")
  left,right=st.columns([1.15,1])
  with left:
   fig=go.Figure(go.Pie(labels=c['funds'],values=p['weights'],hole=.68,sort=False,marker=dict(colors=['#1c8067','#7fba9e','#d8b66a','#233f6b']),textinfo='label+percent',textposition='outside'))
   fig.update_layout(title='Constrained research allocation',paper_bgcolor='rgba(0,0,0,0)',font=dict(family='DM Sans',color='#173d32'),height=340,margin=dict(l=20,r=20,t=58,b=15),showlegend=False,annotations=[dict(text='Research<br>only',x=.5,y=.5,showarrow=False,font=dict(size=18,color='#153f33'))])
   st.plotly_chart(fig,width='stretch')
  with right:
   st.markdown('<div class="cedar-kicker">Decision boundary</div>',unsafe_allow_html=True)
   st.write('A feasible optimizer result is a research candidate. Missing client approvals and trade evidence keep the authorization gate closed.')
   st.metric('Benchmark annual mean',f"{r['benchmark']['expected_return']:.2%}")
 else:st.error('No verified feasible constrained portfolio: '+r['solver']['message'])
 st.subheader('What still needs evidence')
 st.info('Process status: **Not Known**. The model has no documented failed rule for this candidate, but it cannot certify Cedar approval or real-world implementation from the available records.')
 if r['decision']['failed']:
  st.error('Failed rules: '+ '; '.join(r['decision']['failed']))
 for item in r['decision']['unknown']:
  st.markdown(f'- {item}')
with tabs[1]:
 st.subheader('Recovered fund universe and adjusted-price data')
 st.dataframe(load_prices(),width='stretch')
 st.caption('Recovered Yahoo monthly Adj Close, 2026-10-20 download. Includes payout/split adjustment per Lab 14; provider-adjusted return proxy, not independently reconstructed total returns. No forward filling.')
 mu=pd.DataFrame({'Fund':c['funds'],'Annual arithmetic mean':r['mean_estimates']})
 st.dataframe(mu,hide_index=True);st.dataframe(pd.DataFrame(r['covariance'],index=c['funds'],columns=c['funds']))
 st.write('Objective: minimize variance subject to the illustrative return hurdle and explicit allocation constraints. Solver results are independently rechecked.')
 st.json(r['solver'])
 if r['solver']['success']:
  fig=px.bar(x=c['funds'],y=[100*w for w in r['solver']['weights']],labels={'x':'Fund','y':'Weight (%)'},title='Constrained research allocation',color=c['funds'],color_discrete_sequence=['#1c8067','#7fba9e','#d8b66a','#233f6b'])
  fig.update_layout(showlegend=False,plot_bgcolor='rgba(0,0,0,0)',paper_bgcolor='rgba(0,0,0,0)')
  st.plotly_chart(fig,width='stretch')
with tabs[2]:
 st.subheader('Same mandate, different construction rules')
 st.dataframe(pd.DataFrame(comparison(r)),hide_index=True,width='stretch')
 st.write(f"Benchmark annual mean estimate: {r['benchmark']['expected_return']:.2%}; volatility: {r['benchmark']['volatility']:.2%}.")
 st.caption('Authorization gate is Pass/Fail: missing evidence fails authorization while its underlying financial rule remains Not Known. Pass among testable constraints is not full mandate compliance. Unknown inputs stay Not Known. Equal weight and inverse volatility are not repaired to hide failures.')
 allocation=pd.DataFrame({name:[100*w for w in p['weights']] for name,p in r['portfolios'].items()},index=c['funds'])
 fig=px.bar(allocation.reset_index().melt(id_vars='index',var_name='Portfolio',value_name='Weight (%)'),x='index',y='Weight (%)',color='Portfolio',barmode='group',title='Weights by construction rule',color_discrete_sequence=['#80bca0','#d4ae63','#153f6a'])
 fig.update_layout(xaxis_title='Fund',plot_bgcolor='rgba(0,0,0,0)',paper_bgcolor='rgba(0,0,0,0)')
 st.plotly_chart(fig,width='stretch')
 st.subheader('Separate chronological holdout diagnostic')
 st.warning(r['holdout']['label']);st.json(r['holdout'])
with tabs[3]:
 st.subheader('Student-selected fallback: inflation pressure')
 st.write('CPIAUCSL, monthly seasonally adjusted CPI index. YoY = latest index / same-month prior-year index - 1. The signal uses the ALFRED snapshot dated the calendar day before the decision.')
 st.json({k:v for k,v in r['signal'].items() if k!='history'})
 if r['signal'].get('history'):st.line_chart(pd.DataFrame(r['signal']['history']).set_index('date'))
 st.write(f"Effective analytical BIL floor: {r['effective_reserve_floor']:.2%}. Proposed policy raises the floor to 5% when observed YoY inflation exceeds 3%, without reducing the client's reserve minimum.")
 st.warning('You chose to keep this AI-proposed fallback for Project 2. It was not your original Lab 17 selection. Personal source-value checks are still pending, so it does not authorize deployment.')
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
