
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide',page_title= 'Airline Passenger Satisfaction EDA')

st.image('image.jpg')
st.header('Airline Passenger Satisfaction Project')
page = st.sidebar.radio('Page', ['Data', 'Column overview', 'Analysis'])
df = pd.read_csv('cleaned_df.csv', index_col= 0)

if page == 'Data':
    st.header('Data Overview')
    st.dataframe(df)
    
    st.header('Dataset Description')
    column_description={'Gender' :'Passenger gender (Male/Female)',
'Customer Type': 'Whether the passenger is a returning (Loyal Customer) or first-time customer',
'Age':'Age of the passenger in years',
'Type of Travel':'Indicates the purpose of travel (Business/Personal)',
'Class': 'Ticket class (Eco, Eco Plus, Business)',
'Flight Distance': 'Total flight distance traveled (in miles)',
'Inflight wifi service':'Passenger rating of onboard Wi-Fi service (0–5)',
'Departure/Arrival time convenient':'Rating of convenience of flight timing (0–5)',
'Ease of Online booking':'Rating of the ease of booking the flight online (0–5)',
'Gate location': 'Rating of gate accessibility/location (0–5)',
'Food and drink':'Rating of food and beverage service (0–5)',
'Online boarding': 'Rating of online check-in and boarding process (0–5)',
'Seat comfort': 'Rating of seat comfort (0–5)',
'Inflight entertainment': 'Rating of entertainment options (0–5)',
'On-board service':'Rating of service provided by flight attendants (0–5)',
'Leg room service':'Rating of leg room comfort (0–5)',
'Baggage handling': 'Rating of baggage handling quality (0–5)',
'Checkin service':'Rating of check-in service (0–5)',
'Inflight service':'Rating of general inflight services (0–5)',
'Cleanliness': 'Rating of aircraft cleanliness (0–5)',
'Departure Delay in Minutes': 'Delay at departure (in minutes). 0 means on time',
'Arrival Delay in Minutes':'Delay at arrival (in minutes)',
'satisfaction':'Target column — indicates overall passenger satisfaction (Satisfied / Neutral or Dissatisfied'}

    desc_df = pd.DataFrame(list(column_description.items()), columns=["Column Name", "Description"])

    # Display table
    st.subheader("📝 Column Descriptions")
    st.table(desc_df)

elif page == 'Column overview':
    
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

elif page == 'Analysis':
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
