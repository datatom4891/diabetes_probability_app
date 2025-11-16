import streamlit as st
import streamlit.components.v1 as components
from frontend_utils import submit_prediction

from src.pydantic_models.request_models import GeneralHealthEnum, AgeGroupEnum, IncomeLevelEnum, EducationLevelEnum, InputRequest

st.set_page_config(layout="wide", page_title="Diabetes Probability", page_icon=":rocket:")

def submit_inputs(input_dict):
  return 0.0

probability = 0.0
probability_response_flag = False
probability_error_msg = None
no_input_submitted = True
lime_explanation_html = None

boolean_options = ["Yes","No"]
boolean_translation = {"Yes":True, "No":False}

gender_translation = {"Male":True,"Female":False}

general_health_options =["Excellent","Very Good", "Good", "Fair","Poor"]
general_health_translation = {"Excellent":GeneralHealthEnum.EXCELLENT,
                              "Very Good":GeneralHealthEnum.VERY_GOOD, 
                              "Good":GeneralHealthEnum.GOOD, 
                              "Fair":GeneralHealthEnum.FAIR, 
                              "Poor":GeneralHealthEnum.POOR}

age_group_options = ["18 to 24", "25 to 29", "30 to 34", "35 to 39",
                     "40 to 44", "45 to 49", "50 to 54", "55 to 59",
                     "60 to 64", "70 to 74", "75 to 79", "80 and Above"]

age_group_translation = {
  "18 to 24":AgeGroupEnum.AGE_18_24,
  "25 to 29":AgeGroupEnum.AGE_25_29,
  "30 to 34":AgeGroupEnum.AGE_30_34, 
  "35 to 39":AgeGroupEnum.AGE_35_39,
  "40 to 44":AgeGroupEnum.AGE_40_44,
  "45 to 49":AgeGroupEnum.AGE_45_49,
  "50 to 54":AgeGroupEnum.AGE_50_54,
  "55 to 59":AgeGroupEnum.AGE_55_59,
  "60 to 64":AgeGroupEnum.AGE_60_64,
  "65 to 69":AgeGroupEnum.AGE_65_69,
  "70 to 74":AgeGroupEnum.AGE_70_74,
  "75 to 79":AgeGroupEnum.AGE_75_79, 
  "80 and Above":AgeGroupEnum.AGE_80_99
}

education_level_options = ["No School or Kindergarten Only", "Elementary School",
                           "Some High School", "High School Graduate",
                           "Some College or Technical School","College Graduate"]
education_level_translations = {"No School or Kindergarten Only":EducationLevelEnum.NO_SCHOOL_OR_KINDERGARTEN_ONLY,
                                "Elementary School":EducationLevelEnum.ELEMENTARY_SCHOOL,
                                "Some High School":EducationLevelEnum.SOME_HIGH_SCHOOL,
                                "High School Graduate":EducationLevelEnum.HIGH_SCHOOL_GRADUATE,
                                "Some College or Technical School":EducationLevelEnum.SOME_COLLEGE_OR_TECHNICAL_SCHOOL,
                                "College Graduate":EducationLevelEnum.COLLEGE_GRADUATE}

income_level_options = ["Less than 10K", "Less than 15K", "Less than 20K",
                        "Less than 25K", "Less than 35K", "Less than 50K",
                        "Less than 75K","75K or More"]
income_level_translation = {"Less than 10K":IncomeLevelEnum.LESS_THAN_10K,
                            "Less than 15K":IncomeLevelEnum.LESS_THAN_15K, 
                            "Less than 20K":IncomeLevelEnum.LESS_THAN_20K,
                            "Less than 25K":IncomeLevelEnum.LESS_THAN_25K, 
                            "Less than 35K":IncomeLevelEnum.LESS_THAN_35K,
                            "Less than 50K":IncomeLevelEnum.LESS_THAN_50K,
                            "Less than 75K":IncomeLevelEnum.LESS_THAN_75K,
                            "75K or More":IncomeLevelEnum.AT_75K_OR_MORE}

with st.sidebar:
  st.header("About App")

# col1, col2 = st.columns(2)


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
      input_request= dict(high_blood_pressure = boolean_translation[high_bp],
                          high_blood_cholestrol = boolean_translation[high_chl],
                          cholestrol_checked_in_last_5_years=boolean_translation[cholestrol_check],
                          body_mass_index=bmi, 
                          stroke=boolean_translation[stroke],
                          heart_attack_or_heart_disease=boolean_translation[heart_disease_attack],
                          heavy_drinker=boolean_translation[heavy_alcohol_consump],
                          general_health_rating=general_health_translation[general_health],
                          difficulty_walking=boolean_translation[difficulty_walking],
                          is_male=gender_translation[gender], 
                          age=age_group_translation[age_group])
      
      response_obj = submit_prediction(input_request)
      if response_obj.status_code == 200:
        response_dict = response_obj.json()
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
    
    
      