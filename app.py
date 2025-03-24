import streamlit as st
import pandas as pd
import pickle as pkl
# For loading your trained model

# Load your dataset
ds = pd.read_csv("cleaned_data.csv 2")
model = pkl.load(open("D_Cls.pkl", "rb"))
# Load your trained model (ensure your model file path is correct)
#model = joblib.load("path/to/your_model.pkl")  # Update this path

# Streamlit app title
st.title("Diabetic Patient Prediction")

# Input fields for patient data
pregnancies = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose", min_value=0)
blood_pressure = st.number_input("Blood Pressure", min_value=0)
skin_thickness = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=0)

# Prediction button
if st.button("Predict"):
    input_data = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]]
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display the prediction
    st.write(f"Prediction: {'Diabetic' if prediction[0] == 1 else 'Not Diabetic'}")



