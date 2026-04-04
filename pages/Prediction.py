import streamlit as st
import pandas as pd 
import joblib
from sklearn.preprocessing import RobustScaler,OneHotEncoder,OrdinalEncoder
from lightgbm import LGBMClassifier


st.image('image.jpg')
st.header('Passenger Satisfaction Prediction')

#load data
def load_data():
    df= pd.read_csv('cleaned_df.csv', index_col=0)
    return df

df= load_data()
# Create User Widgets

Gender=  st.radio('Gender',df['gender'].unique())
Customer_Type= st.radio('Customer Type', df['customer type'].unique())
age=     st.number_input('Age',step=1)
Travel_type= st.radio('Travel Type',df['type of travel'].unique())
Class=   st.selectbox('Class', df['class'].unique())
Flight_Distance= st.number_input('Flight Distance',step=1)
Wifi=    st.selectbox('Wifi Service', df['inflight wifi service'].unique())
Convenient= st.selectbox('Travel Time Convenient',df['departure/arrival time convenient'].unique())
Online_booking= st.selectbox('Ease of online booking',df['ease of online booking'].unique())
Gate_Location= st.selectbox('Gate location',df['gate location'].unique())
Food = st.selectbox('Food and Drink',df['food and drink'].unique())
online_boarding = st.selectbox('Online Boarding',df['online boarding'].unique())
Seat_Comfort = st.selectbox('Seat comfort',df['seat comfort'].unique())
inflight_entertainment= st.selectbox('Inflight entertainment',df['inflight entertainment'].unique())
on_board_service= st.selectbox('On-board service',df['on-board service'].unique())
leg_room_service= st.selectbox('Leg room service',df['leg room service'].unique())
Baggage_handling= st.selectbox('Baggage handling',df['baggage handling'].unique())
checkin_service	= st.selectbox('Checkin service',df['checkin service'].unique())
inflight_service= st.selectbox('Inflight service',df['inflight service'].unique())
cleanliness= st.selectbox('Cleanliness',df['cleanliness'].unique())
departure_delay_in_minutes	= st.number_input('Departure delay in minutes',step=1)
arrival_delay_in_minutes= st.number_input('Arrival delay in minutes',step=1)
customer_age= st.selectbox('customer_age',df['customer_age'].unique())


# Create Predicted row
input_columns = df.columns.drop('satisfaction')
predicted_data = pd.DataFrame(columns= input_columns, data= [[Gender , Customer_Type , age , Travel_type , Class , Flight_Distance , Wifi , Convenient , Online_booking , Gate_Location ,
                                                             Food , online_boarding , Seat_Comfort , inflight_entertainment , on_board_service , leg_room_service , Baggage_handling ,
                                                              checkin_service , inflight_service , cleanliness , departure_delay_in_minutes , arrival_delay_in_minutes ,customer_age  ]])

# Load Model
model = joblib.load('LightGBM Model.pkl')

result = model.predict(predicted_data)

button = st.button('Predict')

if button == True:
    if result == 1:
        st.success('Passinger is Satisfied')
        st.write(model.predict_proba(predicted_data).round(3)[0][1])

    else:
        st.error('Passenger is Neutral or dissatisfied ')
        st.write(model.predict_proba(predicted_data).round(3)[0][1])

st.image('letter-logo-aeroplane-icon-transportation-600nw-2504057815.webp')
