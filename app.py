import streamlit as st 
import pandas as pd 
import plotly.express as px

st.set_page_config(layout='wide')

st.header('COVID DETAILS ')
data=pd.read_csv('/workspaces/covid_dashboard/Covid Dashboard_data1.csv')
with st.expander('show more'):
    st.write(data)

st.subheader('Covid Details Of India')
ct=st.container(border=True)
c1,c2,c3,c4=ct.columns(4)
c1.metric('Total Covid Cases',data['Total Cases'].sum())
c2.metric('Recovered',data['Discharged'].sum())
c3.metric('Death',data['Deaths'].sum())
c4.metric('Active',data['Active'].sum())

d=data['State/UTs'].unique()
s=st.selectbox('Select State',d)
df=data[data['State/UTs']==s]


st.subheader('Covid Details of States')

ctn=st.container(border=True)
cl1,cl2,cl3,cl4=ctn.columns(4)

cl1.metric('Total Covid Cases',df['Total Cases'].sum())
cl2.metric('Recovered',df['Discharged'].sum())
cl3.metric('Death',df['Deaths'].sum())
cl4.metric('Active',df['Active'].sum())



st.subheader("Total Cases")

st.subheader('highest')
high = data.nlargest(5, 'Total Cases')[['State/UTs', 'Total Cases']]
high.rename(columns={'State/UTs': 'States', 'Total Cases': 'Cases'}, inplace=True)
st.dataframe(high)


st.header('Least')
least = data[data['Total Cases'] > 0].nsmallest(5, 'Total Cases')[['State/UTs', 'Total Cases']]
least.rename(columns={'State/UTs': 'States', 'Total Cases': 'Cases'}, inplace=True)
st.dataframe(least)


st.subheader("Recovered")

st.subheader('highest')
high1 = data.nlargest(5, 'Discharge Ratio')[['State/UTs', 'Discharge Ratio']]
high1.rename(columns={'State/UTs': 'States', 'Discharge Ratio': 'Recovered'}, inplace=True)
st.dataframe(high1)

st.header('Least')
least1 = data[data['Discharge Ratio'] > 0].nsmallest(5, 'Discharge Ratio')[['State/UTs', 'Discharge Ratio']]
least1.rename(columns={'State/UTs': 'States', 'Discharge Ratio': 'Recovered'}, inplace=True)
st.dataframe(least1)


st.subheader("Deaths")

st.subheader('highest')
high2 = data.nlargest(5, 'Death Ratio')[['State/UTs', 'Death Ratio']]
high2.rename(columns={'State/UTs': 'States', 'Death Ratio': 'Deaths'}, inplace=True)
st.dataframe(high2)

st.header('Least')
least2 = data[data['Death Ratio'] > 0].nsmallest(5, 'Death Ratio')[['State/UTs', 'Death Ratio']]
least2.rename(columns={'State/UTs': 'States', 'Death Ratio': 'Deaths'}, inplace=True)
st.dataframe(least2)




st.subheader("Actives")

st.subheader('highest')
high3 = data.nlargest(5, 'Active Ratio')[['State/UTs', 'Active Ratio']]
high3.rename(columns={'State/UTs': 'States', 'Active Ratio': 'Active'}, inplace=True)
st.dataframe(high3)

st.header('Least')
least3 = data[data['Active Ratio'] > 0].nsmallest(5, 'Active Ratio')[['State/UTs', 'Active Ratio']]
least3.rename(columns={'State/UTs': 'States', 'Active Ratio': 'Active'}, inplace=True)
st.dataframe(least3)


st.metric('Death Average(Death Value)',df['Death Ratio'].mean())
top= data.nlargest(15, 'Death Ratio')
bar = px.bar(top, y='State/UTs', x='Death Ratio', title='Death Ratio by State (%)')
st.write(bar)


st.metric('Recovery Average(recover Value)',df['Discharged'].mean())
top1= data.nlargest(10, 'Discharged')
bar1 = px.bar(data, y='State/UTs', x='Discharged', title='Recovery Ratio by State (%)')
st.write(bar1)