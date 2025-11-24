from utils.resources import *

def transform_input(user_input):
  
  high_bp = boolean_translation[user_input["high_blood_pressure"]]
  high_chl = boolean_translation[user_input["high_blood_cholestrol"]]
  cholestrol_check = boolean_translation[user_input["cholestrol_checked_in_last_5_years"]]
  bmi = user_input["body_mass_index"]
  stroke = boolean_translation[user_input["stroke"]]
  heart_disease_attack = boolean_translation[user_input["heart_attack_or_heart_disease"]]
  heavy_drinker = boolean_translation[user_input["heavy_drinker"]]
  general_health = general_health_translation[user_input["general_health_rating"]]
  difficulty_walking = boolean_translation[user_input["difficulty_walking"]]
  is_male = gender_translation[user_input["is_male"]]
  age = age_group_translation[user_input["age"]]
  
  translated_input = [high_bp, high_chl, cholestrol_check, bmi, stroke, heart_disease_attack, heavy_drinker, general_health, difficulty_walking, is_male, age]
  
  return translated_input