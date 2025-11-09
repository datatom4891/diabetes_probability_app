import streamlit as st
import requests

st.set_page_config(layout="wide", page_title="Diabetes Probability", page_icon=":rocket:")

probability = 0.0

boolean_options = ["Yes","No"]

general_health_options =["Excellent"," Very Good", "Good", "Fair","Poor"]

age_group_options = ["18 to 24", "25 to 29", "30 to 34", "35 to 39",
                     "40 to 44", "45 to 49", "50 to 54", "55 to 59",
                     "60 to 64", "70 to 74", "75 to 79", "80 and Above"]

education_level_options = ["No School or Kindergarten Only", "Elementary School",
                           "Some High School", "High School Graduate",
                           "Some College or Technical School","College Graduate"]

income_level_options = ["Less than 10K", "Less than 15K", "Less than 20K",
                        "Less than 25K", "Less than 35K", "Less than 50K",
                        "Less than 75K","75K or More"]

with st.sidebar:
  st.header("About App")

col1, col2 = st.columns(2)

with col1:
  with st.form("model_inputs"):
    high_bp = st.selectbox("Do you have High Blood Pressure?", boolean_options)
    high_chl = st.selectbox("Do you have High Blood Cholestrol?", boolean_options)
    cholestrol_check = st.selectbox("Have you checked your cholestrol in the last 5 years?", boolean_options)
    bmi = st.number_input("Body Mass Index")
    smoker = st.selectbox("Have you smoked at least 100 cigarettes in your entire life?", boolean_options)
    stroke = st.selectbox("Have you ever had a stroke?", boolean_options)
    heart_disease_attack = st.selectbox("Have you ever had a Heart Attack or have a history of Heart Disease?", boolean_options)
    exercise_30 = st.selectbox("Have you exercised in the past 30 Days?", boolean_options)
    fruits = st.selectbox("Do you eat fruits 1 or more times a day?", boolean_options)
    veggies = st.selectbox("Do you eat veggies 1 or more times a day?", boolean_options)
    heavy_alcohol_consump = st.selectbox("Do you drink heavily (Men: More than 14 drinks per week. Women: More than 7 drinks per week?)", boolean_options)
    healthcare_coverage = st.selectbox("Do you have any healthcare coverage?", boolean_options)
    unable_to_see_doc_12 = st.selectbox("In the last 12 months, did you need to see a doctor but didn't due to cost?", boolean_options)
    general_health = st.selectbox("How would you rate your general health",general_health_options)
    mental_health = st.number_input("How many days in the last 30 days has your mental health not been good (stress, depression and emotional problems)",min_value=1,max_value=30)
    physical_health = st.number_input("How many days in the last 30 days has your physical health not been good (physcial illness and injury)",min_value=1,max_value=30)
    difficulty_walking = st.selectbox("Do you have serious difficulty walking or climbing stairs?", boolean_options)
    gender = st.selectbox("Gender",["Male","Female"])
    age_group = st.selectbox("What is your age group?", age_group_options)
    education_level = st.selectbox("Education Level", education_level_options)
    income_level = st.selectbox("Income Level", income_level_options)
    
    submitted = st.form_submit_button("Submit")


with col2:
  st.text(f"Your probability of being diabetic is {probability}% ")