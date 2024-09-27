import streamlit as st 
import pandas as pd 
import plotly.express as px

st.set_page_config(layout='wide')

st.markdown("<h2 style='text-align: center;'>COVID DETAILS</h2>", unsafe_allow_html=True)
data=pd.read_csv('/workspaces/covid_dashboard/Covid Dashboard_data1.csv')
#with st.expander('show more'):
    #st.write(data)

st.markdown("<h3 style='text-align: center;'>Covid detailes of India</h3>", unsafe_allow_html=True)
ct=st.container(border=True)
c1,c2,=ct.columns(2)
c3,c4 =ct.columns(2)
c1.metric('Total Covid Cases',data['Total Cases'].sum())
c2.metric('Recovered',data['Discharged'].sum())
c3.metric('Death',data['Deaths'].sum())
c4.metric('Active',data['Active'].sum())

d=data['State/UTs'].unique()
s=st.selectbox('Select State',d)
df=data[data['State/UTs']==s]

st.markdown("<h3 style='text-align: center;'>Covid Details of States</h3>", unsafe_allow_html=True)

st.subheader('Covid Details of States')

ctn=st.container(border=True)
cl1,cl2=ctn.columns(2)
cl3,cl4=ctn.columns(2)


cl1.metric('Total Covid Cases',df['Total Cases'].sum())
cl2.metric('Recovered',df['Discharged'].sum())
cl3.metric('Death',df['Deaths'].sum())
cl4.metric('Active',df['Active'].sum())

ctnt=st.container(border=True)
ctnt.markdown("<h3 style='text-align: center;'>Total Cases</h3>", unsafe_allow_html=True)
col1,col2=ctnt.columns([1,1],)

col1.markdown("<h4 style='text-align: center;'>Highest</h4>", unsafe_allow_html=True)
high = data.nlargest(5, 'Total Cases')[['State/UTs', 'Total Cases']]
high.rename(columns={'State/UTs': 'States', 'Total Cases': 'Cases'}, inplace=True)
col1.dataframe(high,use_container_width=True)

col2.markdown("<h4 style='text-align: center;'>Least</h4>", unsafe_allow_html=True)
least = data[data['Total Cases'] > 0].nsmallest(5, 'Total Cases')[['State/UTs', 'Total Cases']]
least.rename(columns={'State/UTs': 'States', 'Total Cases': 'Cases'}, inplace=True)
col2.dataframe(least,use_container_width=True)


cont=st.container(border=True)
cont.markdown("<h3 style='text-align: center;'>Recovered</h3>", unsafe_allow_html=True)
cool1, cool2 = cont.columns([1, 1])

cool1.markdown("<h4 style='text-align: center;'>Highest</h4>", unsafe_allow_html=True)
high1 = data.nlargest(5, 'Discharge Ratio')[['State/UTs', 'Discharge Ratio']]
high1.rename(columns={'State/UTs': 'States', 'Discharge Ratio': 'Recovered'}, inplace=True)
cool1.dataframe(high1, use_container_width=True)

cool2.markdown("<h4 style='text-align: center;'>Least</h4>", unsafe_allow_html=True)
least1 = data[data['Discharge Ratio'] > 0].nsmallest(5, 'Discharge Ratio')[['State/UTs', 'Discharge Ratio']]
least1.rename(columns={'State/UTs': 'States', 'Discharge Ratio': 'Recovered'}, inplace=True)
cool2.dataframe(least1, use_container_width=True)


contain=st.container(border=True)
contain.markdown("<h4 style='text-align: center;'>Deaths</h4>", unsafe_allow_html=True)
cll1,cll2=contain.columns([1,1])

cll1.markdown("<h4 style='text-align: center;'>Highest</h4>", unsafe_allow_html=True)
high2 = data.nlargest(5, 'Death Ratio')[['State/UTs', 'Death Ratio']]
high2.rename(columns={'State/UTs': 'States', 'Death Ratio': 'Deaths'}, inplace=True)
cll1.dataframe(high2,use_container_width=True)

cll2.markdown("<h4 style='text-align: center;'>Least</h4>", unsafe_allow_html=True)
least2 = data[data['Death Ratio'] > 0].nsmallest(5, 'Death Ratio')[['State/UTs', 'Death Ratio']]
least2.rename(columns={'State/UTs': 'States', 'Death Ratio': 'Deaths'}, inplace=True)
cll2.dataframe(least2,use_container_width=True)



container=st.container(border=True)
container.markdown("<h3 style='text-align: center;'>Active</h3>", unsafe_allow_html=True)
coo1,coo2 = container.columns([1,1])

coo1.markdown("<h4 style='text-align: center;'>Highest</h4>", unsafe_allow_html=True)
high3 = data.nlargest(5, 'Active Ratio')[['State/UTs', 'Active Ratio']]
high3.rename(columns={'State/UTs': 'States', 'Active Ratio': 'Active'}, inplace=True)
coo1.dataframe(high3,use_container_width=True)

coo2.markdown("<h4 style='text-align: center;'>Least</h4>", unsafe_allow_html=True)
least3 = data[data['Active Ratio'] > 0].nsmallest(5, 'Active Ratio')[['State/UTs', 'Active Ratio']]
least3.rename(columns={'State/UTs': 'States', 'Active Ratio': 'Active'}, inplace=True)
coo2.dataframe(least3,use_container_width=True)



colum1,colum2=st.columns(2)
colum3,colum4=st.columns(2)


colum1.metric('Death Average(Death Value)',df['Death Ratio'].mean())
#top= data.nlargest(15, 'Death Ratio')
bar = px.bar(data, y='State/UTs', x='Death Ratio', title='Death Ratio by State (%)',color_continuous_scale='Viridis')
colum1.plotly_chart(bar)


colum2.metric('Recovery Average(recover Value)',df['Discharged'].mean())
#top1= data.nlargest(10, 'Discharged')
bar1 = px.bar(data, y='State/UTs', x='Discharged', title='Recovery Ratio by State (%)')
colum2.write(bar1)


colum3.metric('Active Average(active Value)',df['Active'].mean())
fig3 = px.bar(data, 
               x='State/UTs', 
               y=['Active', 'Deaths'], 
               title='Active Cases and Deaths',
               labels={'value': 'Count', 'variable': 'Category'},
               barmode='group')
colum3.write(fig3)

colum4.metric('Population Average',df['Population'].mean())
fig4=px.bar(data,x='State/UTs',y=['Total Cases','Discharged'],barmode='group',
color_discrete_sequence=['#28a745', '#dc3545'])
colum4.plotly_chart(fig4)