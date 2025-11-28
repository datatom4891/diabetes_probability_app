import streamlit as st
import streamlit.components.v1 as components
from utils.functions import submit_prediction
from utils.resources import *

st.set_page_config(layout="wide", page_title="Diabetes Probability", page_icon=":rocket:")

st.header("Diabetes Health Indicators 💊🌡️🩹💉🩺")

probability = 0.0
probability_response_flag = False
probability_error_msg = None
no_input_submitted = True
lime_explanation_html = None



with st.sidebar:
  st.header("About App")
  st.text("This is a predictive ML app that predicts the probability of being diabetic based on 11 Health Indicators.")
  st.text("The ML model was trained using a balanced dataset of diabetic and non-diabetic that was put together using the CDC's Behavioral Risk Factor Surveillance System (BRFSS)")
  st.text("The dataset was pulled from a Kaggle link provided below:\n")
  st.link_button("Kaggle Source","https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset")

with st.form("model_inputs"):
  
  col1, col2, col3 = st.columns(3)
  with col1:
    high_bp = st.selectbox("Do you have High Blood Pressure?", boolean_options)
    high_chl = st.selectbox("Do you have High Blood Cholestrol?", boolean_options)
    cholestrol_check = st.selectbox("Have you checked your cholestrol in the last 5 years?", boolean_options)
    bmi = st.number_input("Body Mass Index")
    stroke = st.selectbox("Have you ever had a stroke?", boolean_options)
    heart_disease_attack = st.selectbox("Have you ever had a Heart Attack or have a history of Heart Disease?", boolean_options)
    
  with col2:
    general_health = st.selectbox("How would you rate your general health",general_health_options)
    gender = st.selectbox("Gender",["Male","Female"])
    age_group = st.selectbox("What is your age group?", age_group_options)
    difficulty_walking = st.selectbox("Do you have serious difficulty walking or climbing stairs?", boolean_options)
    heavy_alcohol_consump = st.selectbox("Do you drink heavily (Men: More than 14 drinks per week. Women: More than 7 drinks per week?)", boolean_options)
    
    submitted = st.form_submit_button("Submit")
  
  with col3:
    if submitted:
      input_request= dict(high_blood_pressure = high_bp,
                          high_blood_cholestrol = high_chl,
                          cholestrol_checked_in_last_5_years=cholestrol_check,
                          body_mass_index=bmi, 
                          stroke=stroke,
                          heart_attack_or_heart_disease=heart_disease_attack,
                          heavy_drinker=heavy_alcohol_consump,
                          general_health_rating= general_health,
                          difficulty_walking=difficulty_walking,
                          is_male=gender, 
                          age=age_group)
      print(input_request)
      response_obj = submit_prediction(input_request)
      if response_obj.status_code == 200:
        response_dict = response_obj.json()
        #st.text(response_dict)
        probability = response_dict["probability_str"]
        probability_response_flag = True
        
        if response_dict["explanation_str"]:
          lime_explanation_html = response_dict["explanation_str"]
        else:
          lime_explanation_html = None
      else:
        probability_error_msg = "An error occured, please check that your inputs are correct"
      
      
      
      no_input_submitted = False
        
      


    if probability_response_flag:
      st.text(f"{probability}")
      #st.markdown(lime_explanation_html, unsafe_allow_html=True)
      components.html(lime_explanation_html, height=800)
    else:
      if no_input_submitted:
        st.text(f"Please enter inputs and hit submit to see a probability prediction.")
      else:
        st.text(f"{probability_error_msg}")
    
    
      