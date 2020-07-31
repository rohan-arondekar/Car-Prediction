import streamlit as st
import numpy as np
import pickle


file = open('car_prediction_model.pkl','rb')
classifier = pickle.load(file)

st.image('cars_image_title.png',use_column_width=True)
st.header("Fill details below to get an estimate")
st.markdown('')

market_price = float(st.text_input('Current market price of the car model (in lakhs)',10))

year_bought = st.slider('Year Bought', 2000, 2020, 2015)
age = 2020 - year_bought

kms_driven = float(st.text_input('Number of kilometers driven',0))

owner = int(st.text_input('Number of previous owners',0))

fuel = st.selectbox('Fuel Type',['Petrol','Diesel','CNG'])
if fuel == 'Petrol':
	petrol = 1
	diesel = 0
elif fuel == 'Diesel':
	petrol = 0
	diesel = 1
else:
	petrol = 0
	diesel = 0

seller_type = st.selectbox('Seller Type', ['Individual', 'Dealership'])
if seller_type == 'Individual':
	seller = 1
else:
	seller = 0

transmission_type = st.selectbox('Transmission', ['Manual', 'Automatic'])
if transmission_type == 'Manual':
	transmission = 1
else:
	transmission = 0

inputs = np.array([[market_price, kms_driven, owner, age, diesel, petrol, seller, transmission]])


prediction = classifier.predict(inputs)

if st.button('Predict'):
	st.success('You should expect the car price to be around INR {:.2f} lakh'.format(prediction[0]))


