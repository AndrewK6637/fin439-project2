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
[data-testid="stSidebar"] [data-testid="stSelectbox"] [data-baseweb="select"] > div {background:#fff!important;}
[data-testid="stSidebar"] [data-testid="stSelectbox"] [data-baseweb="select"] * {color:#102d29!important;-webkit-text-fill-color:#102d29!important;opacity:1!important;}
.block-container {padding-top:1.5rem;padding-bottom:3rem;max-width:1480px;}
.cedar-hero {background:linear-gradient(115deg,#102d29,#155849 60%,#247b62);color:#fff;padding:2rem 2.3rem;border-radius:22px;box-shadow:0 16px 42px #103d3024;margin-bottom:1rem;}
.cedar-eyebrow {font-size:.73rem;font-weight:800;letter-spacing:.18em;text-transform:uppercase;color:#b9e5c9;margin-bottom:.5rem;}
.cedar-hero h1 {font-size:clamp(1.8rem,3vw,2.5rem);margin:0;color:#fff!important;line-height:1.2;overflow-wrap:anywhere;}
.cedar-hero p {color:#d4e9df;margin:.7rem 0 0;font-size:1rem;}
.cedar-kicker {color:#36745f;font-size:.72rem;font-weight:800;letter-spacing:.16em;text-transform:uppercase;margin-top:1rem;}
[data-testid="stMetric"] {background:#fff;border:1px solid #dcebe2;border-radius:16px;padding:1rem 1.2rem;box-shadow:0 5px 20px #163b2910;}
[data-testid="stMetricLabel"] {font-weight:700;color:#48695a;}
[data-testid="stMetricValue"] {font-family:'Outfit',sans-serif;color:#103d31;}
[data-testid="stTabs"] button {font-weight:700;}
[data-testid="stSidebar"] [data-testid="stSlider"] [data-baseweb="slider"] * {opacity:1!important;}
[data-testid="stSidebar"] [data-testid="stNumberInput"] button {background:#eaf2ed!important;color:#102d29!important;}
[data-testid="stSidebar"] [data-testid="stSelectbox"] svg {fill:#102d29!important;}
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
applied=r['config'];hurdle=applied['cpi_assumption']+applied['real_return_objective']
def weight_table(weights):
 return pd.DataFrame({'Fund':applied['funds'],'Weight':[f'{w:.2%}' for w in weights]})
def applied_assumptions():
 st.caption(f"Applied scenario: {r['observations']} monthly returns ({r['estimate_start']} to {r['price_end']}); illustrative CPI {applied['cpi_assumption']:.2%} + real spread {applied['real_return_objective']:.2%} = {hurdle:.2%} nominal screening hurdle; additional annual costs {applied['ongoing_cost_bps']} bps; transaction cost {applied['trading_cost_bps']} bps per side; entered BIL floor {applied['reserve_min']:.0%}; effective BIL floor {r['effective_reserve_floor']:.0%}; maximum fund weight {applied['max_weight']:.0%}.")
tabs=st.tabs(['Executive dashboard','Portfolio construction','Portfolio comparison','Point-in-time signal','Stress testing','Committee recommendation'])
with tabs[0]:
 decision=r['decision']
 st.header('Reject deployment for now' if decision['recommendation']=='Reject' else 'Monitored pilot — committee authorization required')
 st.metric('New capital to proposed strategy','0%' if decision['new_process_allocation_range'].startswith('0%-0%') else decision['new_process_allocation_range'])
 st.write('This recommendation applies to **new capital in the proposed strategy** and leaves Cedar’s existing holdings in place.')
 st.warning(decision['committee_ask'])
 st.write('**Client:** Cedar Scholarship Foundation; assets $20 million; ten-year horizon; quarterly scholarships $150,000.')
 st.write('**Objective:** CPI + 3% annually after costs over rolling five-year periods. **Universe:** BIL, IEF, LQD, VT. **Comparator:** 60% VT / 40% LQD, inherited from Lab 14; Cedar approval not recovered.')
 st.write('**Constraints:** long only, fully invested; $600,000 reserve; 95% five-day liquidity; 5% nonexempt direct issuer cap; annual rebalancing and 20% annual one-way turnover cap.')
 st.caption(f"Frozen research decision: {r['as_of']} | Latest price month: {r['price_end']} | Historical estimation observations: {r['observations']}")
 applied_assumptions()
 if r['solver']['success']:
  p=r['portfolios']['Constrained'];st.subheader('Constrained research candidate')
  a,b,d=st.columns(3);a.metric('Annual mean estimate',f"{p['expected_return']:.2%}");b.metric('Annual volatility',f"{p['volatility']:.2%}");d.metric('Net before transition costs',f"{p['net_return_before_trade_cost']:.2%}")
  a,b,d=st.columns(3);a.metric('Testable constraints',p['compliance']['testable_constraints']);b.metric('Full mandate',p['compliance']['mandate_status']);d.metric('Deployment authorization',p['compliance']['authorization_gate'])
  st.write('**Research weights:** '+', '.join(f'{fund} {weight:.2%}' for fund,weight in zip(applied['funds'],p['weights'])))
  if applied==base:st.caption('Default research candidate: 77.04% BIL / 22.96% VT. This is a modeled mix, not an authorized trade.')
  st.caption(f"After the additional annual cost assumption ({c['ongoing_cost_bps']} bps): {p['net_return_before_trade_cost']:.2%} estimated annual return before transition costs. Actual transition costs remain unverified without client holdings.")
  left,right=st.columns([1.15,1])
  with left:
   fig=go.Figure(go.Pie(labels=c['funds'],values=p['weights'],hole=.68,sort=False,marker=dict(colors=['#1c8067','#7fba9e','#d8b66a','#233f6b']),textinfo='label+percent',textposition='outside'))
   fig.update_layout(title='Current scenario research allocation',paper_bgcolor='rgba(0,0,0,0)',font=dict(family='DM Sans',color='#173d32'),height=370,margin=dict(l=50,r=50,t=65,b=25),showlegend=False,annotations=[dict(text='Research<br>only',x=.5,y=.5,showarrow=False,font=dict(size=18,color='#153f33'))])
   st.plotly_chart(fig,width='stretch')
  with right:
   st.markdown('<div class="cedar-kicker">Decision boundary</div>',unsafe_allow_html=True)
   st.write('A feasible optimizer result is a research candidate. Missing client approvals and trade evidence keep the authorization gate closed.')
   st.metric('Benchmark annual mean',f"{r['benchmark']['expected_return']:.2%}")
 else:st.error('No verified feasible constrained portfolio: '+r['solver']['message'])
 st.subheader('Main blockers to funding')
 if decision['failed']:
  for item in decision['failed']:st.error(item)
 if decision['unknown']:
  for item in decision['unknown'][:4]:st.write('• '+item)
  if len(decision['unknown'])>4:
   with st.expander('Other unresolved evidence'):
    for item in decision['unknown'][4:]:st.write('• '+item)
with tabs[1]:
 st.subheader('Recovered fund universe and adjusted-price data')
 st.dataframe(load_prices(),width='stretch')
 st.caption('Recovered Yahoo monthly Adj Close, 2026-10-20 download. Includes payout/split adjustment per Lab 14; provider-adjusted return proxy, not independently reconstructed total returns. No forward filling.')
 mu=pd.DataFrame({'Fund':applied['funds'],'Annual arithmetic mean estimate':[f'{x:.2%}' for x in r['mean_estimates']]})
 st.dataframe(mu,hide_index=True,width='stretch')
 with st.expander('Annualized covariance matrix (decimal return units)'):
  st.dataframe(pd.DataFrame(r['covariance'],index=applied['funds'],columns=applied['funds']))
 st.write('Objective: minimize variance subject to the illustrative return hurdle and explicit allocation constraints. Solver results are independently rechecked.')
 st.caption(f"Evaluation date: {r['as_of']}; prices through {r['price_end']}. Weights and returns below are percentages; volatility is annualized.")
 if r['solver']['success']:
  st.dataframe(weight_table(r['solver']['weights']),hide_index=True,width='stretch')
  st.write(f"**Solver:** {r['solver']['message']} · independent verification: {'Pass' if r['solver']['verified'] else 'Fail'}.")
 with st.expander('Raw solver record'):st.json(r['solver'])
 if r['solver']['success']:
  fig=px.bar(x=c['funds'],y=[100*w for w in r['solver']['weights']],labels={'x':'Fund','y':'Weight (%)'},title='Constrained research allocation',color=c['funds'],color_discrete_sequence=['#1c8067','#7fba9e','#d8b66a','#233f6b'])
  fig.update_layout(showlegend=False,plot_bgcolor='rgba(0,0,0,0)',paper_bgcolor='rgba(0,0,0,0)')
  st.plotly_chart(fig,width='stretch')
with tabs[2]:
 st.subheader('Same mandate, different construction rules')
 summary=[]
 for name,p in r['portfolios'].items():
  summary.append({'Portfolio':name,'Annual mean':f"{p['expected_return']:.2%}",'Annual volatility':f"{p['volatility']:.2%}",'Testable rules':p['compliance']['testable_constraints'],'Full mandate':p['compliance']['mandate_status'],'Authorization':p['compliance']['authorization_gate']})
 st.dataframe(pd.DataFrame(summary),hide_index=True,width='stretch')
 st.write(f"Benchmark annual mean estimate: {r['benchmark']['expected_return']:.2%}; volatility: {r['benchmark']['volatility']:.2%}.")
 st.caption('Authorization gate is Pass/Fail: missing evidence fails authorization while its underlying financial rule remains Not Known. Pass among testable constraints is not full mandate compliance. Unknown inputs stay Not Known. Equal weight and inverse volatility are not repaired to hide failures.')
 allocation=pd.DataFrame({name:[100*w for w in p['weights']] for name,p in r['portfolios'].items()},index=c['funds'])
 fig=px.bar(allocation.reset_index().melt(id_vars='index',var_name='Portfolio',value_name='Weight (%)'),x='index',y='Weight (%)',color='Portfolio',barmode='group',title='Weights by construction rule',color_discrete_sequence=['#80bca0','#d4ae63','#153f6a'])
 fig.update_layout(xaxis_title='Fund',plot_bgcolor='rgba(0,0,0,0)',paper_bgcolor='rgba(0,0,0,0)')
 st.plotly_chart(fig,width='stretch')
 for name,p in r['portfolios'].items():
  with st.expander(name+' weights and rule evidence'):
   st.dataframe(weight_table(p['weights']),hide_index=True,width='stretch')
   for label,key in [('Failed rules','failed'),('Unverified rules','unknown')]:
    items=p['compliance'].get(key,[])
    st.write('**'+label+':**')
    if items:
     for item in items:st.write('• '+str(item))
    else:st.write('None recorded.')
 st.subheader('Separate chronological holdout diagnostic')
 st.warning(r['holdout']['label'])
 st.caption(f"Holdout evaluation: {r['holdout']['evaluation_start']} to {r['holdout']['evaluation_end']}, trained through {r['holdout']['train_end']}; later-downloaded price snapshot, diagnostic only. Gross return is over the evaluation period; volatility is annualized.")
 holdout_rows=[]
 for name,item in r['holdout']['results'].items():
  row={'Portfolio':name,**{fund:f'{w:.2%}' for fund,w in zip(applied['funds'],item['weights'])},'Gross return':f"{item['realized_gross_return']:.2%}",'Annual volatility':f"{item['realized_volatility']:.2%}"}
  holdout_rows.append(row)
 st.dataframe(pd.DataFrame(holdout_rows),hide_index=True,width='stretch')
 with st.expander('Raw holdout record'):st.json(r['holdout'])
with tabs[3]:
 st.subheader('Student-selected fallback: inflation pressure')
 signal=r['signal']
 st.write('The app checks a historical CPI observation available in the November 1 ALFRED vintage, before the frozen November 2 research decision. This is an inflation-pressure indicator, not a return forecast.')
 a,b,d=st.columns(3)
 a.metric('Signal check',signal['status'])
 b.metric('Year-over-year inflation',f"{signal['yoy']:.2%}" if signal.get('yoy') is not None else 'Unavailable')
 d.metric('Historical CPI signal',f"{signal['yoy']:.2%}" if signal.get('yoy') is not None else 'Unavailable')
 st.write(f"**BIL floor:** you entered {applied['reserve_min']:.0%}; the solver used {r['effective_reserve_floor']:.0%}. **Return hurdle:** illustrative CPI {applied['cpi_assumption']:.2%} + real spread {applied['real_return_objective']:.2%} = {hurdle:.2%} nominal. The historical CPI signal is separate from that assumption.")
 if signal.get('status')=='Pass':
  st.write(f"**Calculation:** {signal['value']:.3f} (September 2026 CPI) / {signal['prior_value']:.3f} (September 2025 CPI) - 1 = {signal['yoy']:.2%}.")
  if r['solver']['success']:
   st.write(f"**Portfolio effect:** the {signal['yoy']:.2%} historical signal exceeds the proposed 3% trigger, lifting the analytical floor to at least 5%. The current constrained candidate holds {r['portfolios']['Constrained']['weights'][0]:.2%} BIL, above the {r['effective_reserve_floor']:.0%} floor, so the floor does not bind this allocation.")
  else:st.write('**Portfolio effect:** the signal lifts the analytical BIL floor to at least 5%, but this scenario has no feasible constrained candidate to compare with it.')
 else:st.error('The signal is unavailable or invalid. Do not use it to authorize deployment. '+signal.get('reason',''))
 if signal.get('history'):
  history=pd.DataFrame(signal['history']);history['date']=pd.to_datetime(history['date'])
  fig=go.Figure(go.Scatter(x=history['date'],y=history['value'],mode='lines+markers',connectgaps=False,name='CPI index'))
  fig.update_layout(xaxis_title='Observation month',yaxis_title='CPI index (1982–84 = 100)',height=300,margin=dict(l=25,r=25,t=20,b=35))
  st.plotly_chart(fig,width='stretch')
  missing=history.loc[history['value'].isna(),'date'].dt.strftime('%B %Y').tolist()
  if missing:st.caption('Stored vintage has no observation for '+', '.join(missing)+'. The chart preserves the gap; no value is filled or interpolated.')
 st.warning('Student report: three CPI source values and the year-over-year arithmetic were spot-checked on November 19, 2026. Code check: vintage identity and pre-decision cutoff pass. Still unverified: independent review of the reported source check and Cedar approval of the 3% trigger/5% floor policy. The signal does not authorize deployment.')
 with st.expander('Source details and raw signal record'):
  st.write('Series: CPIAUCSL, seasonally adjusted monthly CPI. The observation date labels the month, not the original release time. The saved vintage is',signal.get('cutoff','unavailable'))
  st.json({k:v for k,v in signal.items() if k!='history'})
 card=ROOT/'docs/signal-data-card.md'
 if card.exists():
  with st.expander('Read the signal data card'):st.markdown(card.read_text(encoding='utf-8'))
with tabs[4]:
 st.subheader('Required robustness checks')
 applied_assumptions()
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
  cost_case=next((s for s in r['stress'] if s['scenario']=='Trading cost 50 bps per side'),None)
  if cost_case and cost_case['success']:
   t=cost_case['transition_cost_sensitivity']
   st.info(f"**Trading cost stress:** Raising cost to 50 bps per side leaves the optimized target {'unchanged' if cost_case['largest_weight_change']<0.00005 else 'changed'} ({cost_case['largest_weight_change']*100:.2f} percentage-point largest weight move). Separately, a hypothetical baseline-to-equal-weight trade would turn over {t['hypothetical_one_way_turnover']:.2%} of assets one way and incur {t['at_stress_50bps']:.2%} of assets in cost. That trade is not the optimized target or Cedar's actual trade.")
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
 applied_assumptions()
 st.write(r['decision']['committee_ask']);st.write('New-process allocation range:',r['decision']['new_process_allocation_range'])
 st.write('Monitor: reserve coverage, net real outcomes, annual turnover, signal vintage, price freshness, solver feasibility and allocation stability. Resolve the missing mandate evidence before revisiting deployment.')
 memo=ROOT/'docs/decision-memo.md'
 if memo.exists():
  st.caption('Frozen memo dated November 2, 2026: documents the saved default decision. The live decision above and the scenario download use the currently applied controls.')
  st.markdown(memo.read_text(encoding='utf-8'))
 st.download_button('Download this scenario',json.dumps(r,indent=2),file_name='cedar_scenario.json')
