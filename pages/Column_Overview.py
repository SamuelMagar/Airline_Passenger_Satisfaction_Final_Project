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

st.header('Column Overview')
tab_num, tab_cat = st.tabs(['Numerical', 'Categorical'])
num_cols = df.select_dtypes(include= 'number')

     
    # Numerical Tab
num_cols = df.select_dtypes(include= 'number').columns
column_num = tab_num.selectbox('Column', num_cols)
tab_num.plotly_chart(px.histogram(data_frame= df, x= column_num,text_auto=True, title= column_num))

    # Categorical Tab
cat_cols = df.select_dtypes(include= 'object').columns
column_cat = tab_cat.selectbox('Column', cat_cols)

chart = tab_cat.selectbox('Chart', ['Histogram', 'Pie'])

if chart == 'Histogram':
    tab_cat.plotly_chart(px.histogram(data_frame= df, x= column_cat, title= column_cat,text_auto=True).update_xaxes(categoryorder = 'max descending'))

elif chart == 'Pie':
    tab_cat.plotly_chart(px.pie(data_frame= df, names= column_cat, title= column_cat))

st.image('letter-logo-aeroplane-icon-transportation-600nw-2504057815.webp')
