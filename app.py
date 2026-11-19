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
[data-testid="stSidebar"] [data-testid="stNumberInput"] input,
[data-testid="stSidebar"] [data-testid="stTextInput"] input,
[data-testid="stSidebar"] [data-baseweb="input"] input {color:#102d29!important;-webkit-text-fill-color:#102d29!important;background:#fff!important;opacity:1!important;}
[data-testid="stSidebar"] [data-testid="stNumberInput"] [data-baseweb="input"],
[data-testid="stSidebar"] [data-testid="stTextInput"] [data-baseweb="input"] {background:#fff!important;}
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
st.caption('Built with OpenAI Codex assistance. Student selected the analytical design and reported checking three CPI source values on November 19, 2026; final review remains pending. Educational analysis, not investment advice.')
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
 signal=r['signal']
 st.write('The app checks a historical CPI observation available in the November 1 ALFRED vintage, before the frozen November 2 research decision. This is an inflation-pressure indicator, not a return forecast.')
 a,b,d=st.columns(3)
 a.metric('Signal check',signal['status'])
 b.metric('Year-over-year inflation',f"{signal['yoy']:.2%}" if signal.get('yoy') is not None else 'Unavailable')
 d.metric('Analytical BIL floor',f"{r['effective_reserve_floor']:.0%}")
 if signal.get('status')=='Pass':
  st.write(f"**Calculation:** {signal['value']:.3f} (September 2026 CPI) / {signal['prior_value']:.3f} (September 2025 CPI) - 1 = {signal['yoy']:.2%}.")
  st.write('**Portfolio effect:** Inflation exceeds the proposed 3% trigger, so the analytical BIL floor rises to 5%. The default constrained portfolio already holds more BIL than that floor; the signal does not change its default weights.')
 else:st.error('The signal is unavailable or invalid. Do not use it to authorize deployment. '+signal.get('reason',''))
 if r['signal'].get('history'):st.line_chart(pd.DataFrame(r['signal']['history']).set_index('date'))
 st.warning('This AI-proposed CPI rule was selected for the coursework model. The student reported checking three source values and the arithmetic, but Cedar has not approved the policy; the signal does not authorize deployment.')
 with st.expander('Source details and raw signal record'):
  st.write('Series: CPIAUCSL, seasonally adjusted monthly CPI. The observation date labels the month, not the original release time. The saved vintage is',signal.get('cutoff','unavailable'))
  st.json({k:v for k,v in signal.items() if k!='history'})
 card=ROOT/'docs/signal-data-card.md'
 if card.exists():
  with st.expander('Read the signal data card'):st.markdown(card.read_text(encoding='utf-8'))
with tabs[4]:
 st.subheader('Required robustness checks')
 st.error('STOP deployment on infeasibility, invalid/missing signal, stale prices, or more than 20 percentage points of weight instability. Unresolved mandate evidence also blocks authorization.')
 if r['stress']:
  rows=[]
  for s in r['stress']:
   rows.append({'Scenario':s['scenario'],'Solver':'Pass' if s['success'] else 'Fail',
    'BIL':f"{s['weights'][0]:.1%}" if s['success'] else '—','IEF':f"{s['weights'][1]:.1%}" if s['success'] else '—',
    'LQD':f"{s['weights'][2]:.1%}" if s['success'] else '—','VT':f"{s['weights'][3]:.1%}" if s['success'] else '—',
    'Annual mean':f"{s['expected_return']:.2%}" if s['success'] else '—',
    'Volatility':f"{s['volatility']:.2%}" if s['success'] else '—',
    'Largest weight move':f"{s['largest_weight_change']*100:.2f} pp" if s['success'] else '—',
    'Authorization':s['mandate']['authorization_gate'] if s['success'] else 'Fail'})
  st.dataframe(pd.DataFrame(rows),hide_index=True,width='stretch')
  largest=max((s.get('largest_weight_change',0) for s in r['stress']),default=0)
  st.write(f'**What moved most:** The largest tested allocation change is {largest*100:.2f} percentage points. The analyst stop threshold is 20 percentage points. Passing these scenario optimizations does not establish full Cedar authorization.')
  for s in r['stress']:
   with st.expander(s['scenario']+' — interpretation and evidence'):
    if s['success']:
     st.write(f"Weights: {', '.join(f'{fund} {weight:.1%}' for fund,weight in zip(c['funds'],s['weights']))}. Estimated annual mean {s['expected_return']:.2%}; volatility {s['volatility']:.2%}. Largest move from the base allocation: {s['largest_weight_change']*100:.2f} percentage points.")
     st.write(f"Testable constraints: {s['mandate']['testable_constraints']}. Full mandate: {s['mandate']['mandate_status']}. Authorization: {s['mandate']['authorization_gate']}.")
     if s.get('transition_cost_sensitivity'):
      t=s['transition_cost_sensitivity']
      st.write(f"**Cost illustration:** A hypothetical baseline-to-equal-weight transition has {t['hypothetical_one_way_turnover']:.1%} one-way turnover and costs {t['at_stress_50bps']:.2%} of assets at 50 bps per traded side. These are not Cedar's actual holdings or trades.")
    else:st.error('Solver infeasible or failed: '+s['message'])
    with st.expander('Raw scenario record'):st.json(s)
 if r['stress']:
  st.caption('The cost illustration uses hypothetical holdings. Actual client costs cannot be computed without Cedar holdings and trades.')
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
