import streamlit as st
import pickle
import pandas as pd

# Load the pre-trained model
with open('model.pkl','rb') as model_file:
    model = pickle.load(model_file)
    
# Streamlit UI for user input
st.title("Tip Prediction app")

# Input fields for the user
total_bill = st.number_input("total_bill")
size = st.number_input("size", min_value=1, max_value=10, value=2)
sex = st.selectbox("Sex", ["Male","Female"])
day = st.selectbox("Day", ["Thur","Fri","Sat","Sun"])
smoker = st.selectbox("Smoker",['No','Yes'])
time = st.selectbox("Time",["Lunch","Dinner"])

# Creating a DataFrame with user inputs and applyning One-Hot encoding
input_data = pd.DataFrame({
    'total_bill' : [total_bill],
    'sex' : [sex],
    'smoker':[smoker],
    'day' : [day],
    'time' : [time],
    'size' : [size]
})

# Mpping categorical variables variables manually
sex_mapping = {'Male':0, 'Female':1}
smoker_mapping = {'No':0, 'Yes':1}
day_mapping = {'Thur':0, 'Fri':1, 'Sat':2, 'Sun':3}
time_mapping = {'Lunch':0, 'Dinner':1}

input_data['sex'] = input_data['sex'].map(sex_mapping)
input_data['smoker'] = input_data['smoker'].map(smoker_mapping)
input_data['day'] = input_data['day'].map(day_mapping)
input_data['time']=input_data['time'].map(time_mapping)

# Make the prediction
if st.button("Predict Tip"):
    prediction = model.predict(input_data)
    st.write(f"Predicted Tip :${round(prediction[0],2)}")