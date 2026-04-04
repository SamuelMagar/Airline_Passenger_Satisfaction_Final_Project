
import streamlit as st
import pandas as pd 
import plotly.express as px


st.image('image.jpg')
st.header('Passenger Satisfaction Prediction')
page = st.sidebar.radio('Page', ['Data', 'Column overview', 'Analysis','Prediction'])
@st.cache_data
def load_data():
    df= pd.read_csv('cleaned_df.csv', index_col=0)
    return df

df= load_data()
    
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
    # Display table

desc_df = pd.DataFrame(list(column_description.items()), columns=["Column Name", "Description"])
st.subheader("📝 Column Descriptions")
st.table(desc_df)
st.header('Data Sample')

st.dataframe(df)




st.image('letter-logo-aeroplane-icon-transportation-600nw-2504057815.webp')
