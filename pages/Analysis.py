import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(layout='wide',page_title= 'Airline Passenger Satisfaction')

st.image('image.jpg')
st.header('Airline Passenger Satisfaction Project')
page = st.sidebar.radio('Page', ['Data', 'Column overview', 'Analysis','Prediction'])
def load_data():
    df= pd.read_csv('cleaned_df.csv', index_col=0)
    return df

df= load_data()
st.header('1- Is there any numerical correlation between Data ?')
corr_df = df.corr(numeric_only= True).round(2)
st.plotly_chart(px.imshow(corr_df, text_auto= True, width= 1000, height= 800))

st.header('2- Are loyal customers more satisfied than disloyal customers?')
st.plotly_chart(px.histogram(data_frame=df,x='customer type',color='satisfaction',barmode='group',text_auto=True,title='satisfaction per loyality').update_xaxes(categoryorder='max descending'))

st.header('3- Dose delay in departure effects in satisfaction?')
satis_dd_df=df.groupby('satisfaction')['departure delay in minutes'].mean().round(2).reset_index()
st.plotly_chart(px.bar(data_frame=satis_dd_df,x='satisfaction',y='departure delay in minutes',title='Departure delay Vs Satisfaction',text_auto=True,labels={'departure delay in minutes':'AVG departure delay in minutes'}))

st.header('4- Dose delay in arrival effects in satisfaction?')
satis_ad_df=df.groupby('satisfaction')['arrival delay in minutes'].mean().round(2).reset_index()    
st.plotly_chart(px.bar(data_frame=satis_ad_df,x='satisfaction',y='arrival delay in minutes',text_auto=True,title='Arrival delay Vs Satisfaction',labels={'arrival delay in minutes':'AVG arrival delay in minutes'}))

st.header('5- Dose fleight distance effects in satisfaction?')
satis_fd_df=df.groupby('satisfaction')['flight distance'].mean().round(2).reset_index()
st.plotly_chart(px.bar(data_frame=satis_fd_df,x='satisfaction',y='flight distance',labels={'flight distance': 'AVG flight distance'},title='Flight distance Vs Satisfaction',text_auto=True))

st.header("6- Which class's passenger more satisfy ?")
st.plotly_chart(px.histogram(data_frame=df,x='class',color='satisfaction',barmode='group',text_auto=True,title='Satisfaction for each class').update_xaxes(categoryorder='max descending'))
    
st.header('7- Which gender more satisfy?')
st.plotly_chart(px.histogram(data_frame=df,x='gender',color='satisfaction',barmode='group',text_auto=True,title='Satisfaction by gender').update_xaxes(categoryorder='max descending'))
    
st.header('8- Does customer satisfaction differ based on the type of travel (Business vs Personal)')
st.plotly_chart(px.histogram(data_frame=df,x='type of travel',color='satisfaction',barmode='group',title='satisfaction according travel type',text_auto=True))

st.image('letter-logo-aeroplane-icon-transportation-600nw-2504057815.webp')
