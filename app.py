import streamlit as st 
import pandas as pd 
import plotly.express as px

st.set_page_config(layout='wide')

st.markdown("<u><h2 style='text-align: center;'>COVID-19 Data Insights for India</h2></u>", unsafe_allow_html=True)
data=pd.read_csv('/workspaces/covid_dashboard/Covid Dashboard_data1.csv')
#with st.expander('show more'):
    #st.write(data)

st.markdown('<br>',unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'>India's COVID-19 Overview</h3>", unsafe_allow_html=True)

c=st.container(border=True)
c1, c2, c3, c4 = c.columns(4)
c1.metric('Total Covid Cases', data['Total Cases'].sum())
c2.metric('Recovered', data['Discharged'].sum())
c3.metric('Deaths', data['Deaths'].sum())
c4.metric('Active', data['Active'].sum())
st.markdown('<br><br>',unsafe_allow_html=True)


st.markdown("<h3 style='text-align: center;'>COVID-19 Statistics by State</h3>", unsafe_allow_html=True)
cn=st.container(border=True)

d=data['State/UTs'].unique()
s=cn.selectbox('Select State',d)
df=data[data['State/UTs']==s]

cl1, cl2, cl3, cl4 = cn.columns(4)

st.markdown('<div class="metric-container">', unsafe_allow_html=True)
cl1.metric('Total Covid Cases', df['Total Cases'].sum())
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="metric-container">', unsafe_allow_html=True)
cl2.metric('Recovered', df['Discharged'].sum())
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="metric-container">', unsafe_allow_html=True)
cl3.metric('Deaths', df['Deaths'].sum())
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="metric-container">', unsafe_allow_html=True)
cl4.metric('Active', df['Active'].sum())
st.markdown('</div>', unsafe_allow_html=True)


st.markdown("<h3 style='text-align: center;'>Comprehensive COVID-19 Data by States</h3>", unsafe_allow_html=True)
st.markdown('<br>',unsafe_allow_html=True)
ctnr=st.container(border=True)
colum1,colum2,colum3=ctnr.columns(3)
st.markdown('<br>',unsafe_allow_html=True)

colum4,colum5,colum6=ctnr.columns(3)

#top= data.nlargest(15, 'Death Ratio')
bar = px.bar(data, y='State/UTs', x='Death Ratio', title='Death Ratio by State (%)',color='Death Ratio',color_continuous_scale='Viridis')
colum1.plotly_chart(bar)


figu = px.line(data, x='State/UTs', y='Deaths', title='Death of States', markers=True)
colum2.plotly_chart(figu)

#top1= data.nlargest(10, 'Discharged')
bar1 = px.bar(data, y='State/UTs', x='Discharged', title='Recovery Ratio by State (%)',color='Discharged',color_continuous_scale='Blues')
colum3.write(bar1)


fig3 = px.bar(data, 
               x='State/UTs', 
               y=['Active', 'Deaths'], 
               title='Active Cases and Deaths',
               labels={'value': 'Count', 'variable': 'Category'},
               barmode='group',color_discrete_sequence=['#0074D9', '#FF851B'])
colum4.write(fig3)

figg = px.pie(data, values="Total Cases", names="Zone",
             title='Cases of Zone', hover_data=['Deaths'])
colum5.write(figg)


fig4=px.bar(data,x='State/UTs',y=['Total Cases','Discharged'],title='Total Cases and Discharged',barmode='group',
color_discrete_sequence=['#28a745', '#dc3545'])
colum6.plotly_chart(fig4)



st.markdown('<br><br>',unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>COVID-19 Statistics: States with Highest and Least Cases</h3>", unsafe_allow_html=True)
st.markdown('<br>',unsafe_allow_html=True)

ctnt=st.container(border=True)
ctnt.markdown("<h4 style='text-align: center;'>Total Cases</h4>", unsafe_allow_html=True)
col1,col2=ctnt.columns([1,1],)

col1.markdown("<h5 style='text-align: center;'>Highest</h5>", unsafe_allow_html=True)
high = data.nlargest(5, 'Total Cases')[['State/UTs', 'Total Cases']]
high.rename(columns={'State/UTs': 'States', 'Total Cases': 'Cases'}, inplace=True)
col1.dataframe(high,use_container_width=True)

col2.markdown("<h5 style='text-align: center;'>Least</h5>", unsafe_allow_html=True)
least = data[data['Total Cases'] > 0].nsmallest(5, 'Total Cases')[['State/UTs', 'Total Cases']]
least.rename(columns={'State/UTs': 'States', 'Total Cases': 'Cases'}, inplace=True)
col2.dataframe(least,use_container_width=True)


st.markdown('<br><br>',unsafe_allow_html=True)

cont=st.container(border=True)
cont.markdown("<h4 style='text-align: center;'>Recovered</h4>", unsafe_allow_html=True)
cool1, cool2 = cont.columns([1, 1])

cool1.markdown("<h5 style='text-align: center;'>Highest</h5>", unsafe_allow_html=True)
high1 = data.nlargest(5, 'Discharge Ratio')[['State/UTs', 'Discharge Ratio']]
high1.rename(columns={'State/UTs': 'States', 'Discharge Ratio': 'Recovered'}, inplace=True)
cool1.dataframe(high1, use_container_width=True)

cool2.markdown("<h5 style='text-align: center;'>Least</h5>", unsafe_allow_html=True)
least1 = data[data['Discharge Ratio'] > 0].nsmallest(5, 'Discharge Ratio')[['State/UTs', 'Discharge Ratio']]
least1.rename(columns={'State/UTs': 'States', 'Discharge Ratio': 'Recovered'}, inplace=True)
cool2.dataframe(least1, use_container_width=True)


st.markdown('<br><br>',unsafe_allow_html=True)

contain=st.container(border=True)
contain.markdown("<h5 style='text-align: center;'>Deaths</h5>", unsafe_allow_html=True)
cll1,cll2=contain.columns([1,1])

cll1.markdown("<h5 style='text-align: center;'>Highest</h5>", unsafe_allow_html=True)
high2 = data.nlargest(5, 'Death Ratio')[['State/UTs', 'Death Ratio']]
high2.rename(columns={'State/UTs': 'States', 'Death Ratio': 'Deaths'}, inplace=True)
cll1.dataframe(high2,use_container_width=True)

cll2.markdown("<h5 style='text-align: center;'>Least</h45>", unsafe_allow_html=True)
least2 = data[data['Death Ratio'] > 0].nsmallest(5, 'Death Ratio')[['State/UTs', 'Death Ratio']]
least2.rename(columns={'State/UTs': 'States', 'Death Ratio': 'Deaths'}, inplace=True)
cll2.dataframe(least2,use_container_width=True)


st.markdown('<br><br>',unsafe_allow_html=True)

container=st.container(border=True)
container.markdown("<h4 style='text-align: center;'>Active</h4>", unsafe_allow_html=True)
coo1,coo2 = container.columns([1,1])

coo1.markdown("<h5 style='text-align: center;'>Highest</h5>", unsafe_allow_html=True)
high3 = data.nlargest(5, 'Active Ratio')[['State/UTs', 'Active Ratio']]
high3.rename(columns={'State/UTs': 'States', 'Active Ratio': 'Active'}, inplace=True)
coo1.dataframe(high3,use_container_width=True)

coo2.markdown("<h5 style='text-align: center;'>Least</h5>", unsafe_allow_html=True)
least3 = data[data['Active Ratio'] > 0].nsmallest(5, 'Active Ratio')[['State/UTs', 'Active Ratio']]
least3.rename(columns={'State/UTs': 'States', 'Active Ratio': 'Active'}, inplace=True)
coo2.dataframe(least3,use_container_width=True)

#st.markdown('<br><br>',unsafe_allow_html=True)
#cc1,cc2,cc3,cc4=st.columns(4)

#cc1.metric('Death Average(Death Value)',df['Death Ratio'].mean())
#cc2.metric('Recovery Average(recover Value)',df['Discharged'].mean())
#cc3.metric('Active Average(active Value)',df['Active'].mean())
#cc4.metric('Population Average',df['Population'].mean())




