import os
import numpy as np
from xgboost import XGBClassifier

from src.database.database  import DiabetesProbability
from src.database.utils import get_db
from src.pydantic_models.request_models import InputRequest
from src.pydantic_models.response_models import ModelResponse

from fastapi import APIRouter, Depends, HTTPException, Path
from typing import Annotated
from sqlalchemy.orm import Session

model_dir = os.path.join(os.getcwd(),"src","ml_models","diabetes_probability_model_v1.model")
xgb_classifier = XGBClassifier()
xgb_classifier.load_model(model_dir)

db_dependency = Annotated[Session, Depends(get_db)]

router = APIRouter(prefix="/diabetes", tags=["diabetes"])

# response_model=ModelResponse
@router.post("/probability",  response_model=ModelResponse)
async def diabetes_probability(user_input:InputRequest, db: db_dependency):
  model_input =[
                  [ 
                    user_input.model_dump()["high_blood_pressure"],
                    user_input.model_dump()["high_blood_cholestrol"],
                    user_input.model_dump()["cholestrol_checked_in_last_5_years"],
                    user_input.model_dump()["body_mass_index"],
                    user_input.model_dump()["smoker"],
                    user_input.model_dump()["stroke"],
                    user_input.model_dump()["heart_attack_or_heart_disease"],
                    user_input.model_dump()["any_physical_activity_in_last30"],
                    user_input.model_dump()["consume_fruits"],
                    user_input.model_dump()["consume_veggies"],
                    user_input.model_dump()["heavy_drinker"],
                    user_input.model_dump()["have_health_insurance"],
                    user_input.model_dump()["no_dr_visit_due_to_cost"],
                    user_input.model_dump()["general_health_rating"],
                    user_input.model_dump()["mental_health"],
                    user_input.model_dump()["physical_health"],
                    user_input.model_dump()["difficulty_walking"],
                    user_input.model_dump()["is_male"],
                    user_input.model_dump()["age"],
                    user_input.model_dump()["education_level"],
                    user_input.model_dump()["income"]
                  ]
  ]
  
  probabilities = xgb_classifier.predict_proba(model_input)[0]
  probaility_index = np.argmax(probabilities)
  diabetes_probability = round(probabilities[probaility_index].item(),2)
  model_response = ModelResponse(probability = diabetes_probability , explanation="Not Available")
  
  diabetes_probability_db = DiabetesProbability(diabetes_probability=model_response.probability,
                                                probability_prediction_explanation = model_response.explanation,
                                                high_blood_pressure = model_input[0][0],
                                                high_blood_cholestrol = model_input[0][1],
                                                cholestrol_checked_in_last_5_years = model_input[0][2],
                                                body_mass_index = model_input[0][3],
                                                smoker = model_input[0][4],
                                                stroke = model_input[0][5],
                                                heart_attack_or_heart_disease = model_input[0][6],
                                                any_physical_activity_in_last30 = model_input[0][7], 
                                                consume_fruits = model_input[0][8],
                                                consume_veggies = model_input[0][9],
                                                heavy_drinker = model_input[0][10],
                                                have_health_insurance = model_input[0][11],
                                                no_dr_visit_due_to_cost = model_input[0][12],
                                                general_health_rating = model_input[0][13],
                                                mental_health = model_input[0][14],
                                                physical_health = model_input[0][15],
                                                difficulty_walking = model_input[0][16],
                                                is_male = model_input[0][17],
                                                age = model_input[0][18],
                                                education_level = model_input[0][19],
                                                income = model_input[0][20])
  db.add(diabetes_probability_db)
  db.commit()
  return model_response