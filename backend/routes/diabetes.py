import os
import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from lime import lime_tabular

from database.database  import DiabetesProbabilityV3
from database.utils import get_db
from pydantic_models.request_models import InputRequestV3
from pydantic_models.response_models import ModelResponse
from utils.functions import transform_input

from fastapi import APIRouter, Depends, HTTPException, Path
from typing import Annotated
from sqlalchemy.orm import Session

model_dir = os.path.join(os.getcwd(),"ml_models","diabetes_probability_model_v3.model")
data = os.path.join(os.getcwd(),"data","lime_explainer_dataset.csv")
df = pd.read_csv(data)
features = list(df.columns)
X = df.values

xgb_classifier = XGBClassifier()
xgb_classifier.load_model(model_dir)

lime_explainer = lime_tabular.LimeTabularExplainer(X,feature_names=features, mode="classification",class_names=["Not Diabetic","Diabetic"])

db_dependency = Annotated[Session, Depends(get_db)]

router = APIRouter(prefix="/diabetes", tags=["diabetes"])

# response_model=ModelResponse
@router.post("/probability",  response_model=ModelResponse)
async def diabetes_probability(user_input:InputRequestV3, db: db_dependency):
  
  model_input =[
                  [ 
                    user_input.model_dump()["high_blood_pressure"],
                    user_input.model_dump()["high_blood_cholestrol"],
                    user_input.model_dump()["cholestrol_checked_in_last_5_years"],
                    user_input.model_dump()["body_mass_index"],
                    user_input.model_dump()["stroke"],
                    user_input.model_dump()["heart_attack_or_heart_disease"],
                    user_input.model_dump()["heavy_drinker"],
                    user_input.model_dump()["general_health_rating"],
                    user_input.model_dump()["difficulty_walking"],
                    user_input.model_dump()["is_male"],
                    user_input.model_dump()["age"]
                  ]
  ]
  
  model_input_np = np.array(model_input[0])
  probabilities = xgb_classifier.predict_proba(model_input)[0]
  probaility_index = np.argmax(probabilities)
  
  if probaility_index == 0:
    diabetes_probability = round(1- probabilities[probaility_index].item(),2)
    response_str = f"The model thinks the probability that you are diabetic is: {diabetes_probability}"
  else:
    diabetes_probability = round(probabilities[probaility_index].item(),2)
    response_str = f"The model thinks the probability that you are diabetic is: {diabetes_probability}"
  
  lime_explanation = lime_explainer.explain_instance(model_input_np, xgb_classifier.predict_proba,num_features=len(features))
  lime_explanation_html_str = lime_explanation.as_html()
  
  if lime_explanation_html_str:
    model_response = ModelResponse(probability_str = response_str , explanation_str=lime_explanation_html_str)
  else:
    model_response = ModelResponse(probability_str = response_str , explanation_str=None)
  
  diabetes_probability_db = DiabetesProbabilityV3(diabetes_probability=diabetes_probability,
                                                  probability_prediction_explanation =model_response.explanation_str,
                                                  high_blood_pressure = model_input[0][0],
                                                  high_blood_cholestrol = model_input[0][1],
                                                  cholestrol_checked_in_last_5_years = model_input[0][2],
                                                  body_mass_index = model_input[0][3],
                                                  stroke = model_input[0][4],
                                                  heart_attack_or_heart_disease = model_input[0][5],
                                                  heavy_drinker = model_input[0][6],
                                                  general_health_rating = model_input[0][7],
                                                  difficulty_walking = model_input[0][8],
                                                  is_male = model_input[0][9],
                                                  age = model_input[0][10]) 
  db.add(diabetes_probability_db)
  db.commit()
  return model_response

# response_model=ModelResponse
@router.post("/probability_ui", response_model=ModelResponse)
async def diabetes_probability2(user_input:InputRequestV3, db: db_dependency):
  
  user_input_dict = user_input.model_dump()
  user_input_translated = transform_input(user_input_dict)
  #return user_input_translated
  model_input =[user_input_translated]
  
  model_input_np = np.array(model_input[0])
  probabilities = xgb_classifier.predict_proba(model_input)[0]
  probaility_index = np.argmax(probabilities)
  
  if probaility_index == 0:
    diabetes_probability = round(1- probabilities[probaility_index].item(),2)
    response_str = f"The model thinks the probability that you are diabetic is: {diabetes_probability}"
  else:
    diabetes_probability = round(probabilities[probaility_index].item(),2)
    response_str = f"The model thinks the probability that you are diabetic is: {diabetes_probability}"
  
  lime_explanation = lime_explainer.explain_instance(model_input_np, xgb_classifier.predict_proba,num_features=len(features))
  lime_explanation_html_str = lime_explanation.as_html()
  
  if lime_explanation_html_str:
    model_response = ModelResponse(probability_str = response_str , explanation_str=lime_explanation_html_str)
  else:
    model_response = ModelResponse(probability_str = response_str , explanation_str=None)
  
  diabetes_probability_db = DiabetesProbabilityV3(diabetes_probability=diabetes_probability,
                                                  probability_prediction_explanation =model_response.explanation_str,
                                                  high_blood_pressure = model_input[0][0],
                                                  high_blood_cholestrol = model_input[0][1],
                                                  cholestrol_checked_in_last_5_years = model_input[0][2],
                                                  body_mass_index = model_input[0][3],
                                                  stroke = model_input[0][4],
                                                  heart_attack_or_heart_disease = model_input[0][5],
                                                  heavy_drinker = model_input[0][6],
                                                  general_health_rating = model_input[0][7],
                                                  difficulty_walking = model_input[0][8],
                                                  is_male = model_input[0][9],
                                                  age = model_input[0][10]) 
  db.add(diabetes_probability_db)
  db.commit()
  return model_response