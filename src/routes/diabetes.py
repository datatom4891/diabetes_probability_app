import os
from xgboost import XGBClassifier

from src.database.database  import DiabetesProbability
from src.database.utils import get_db
from src.pydantic_models.request_models import InputRequest

from fastapi import APIRouter, Depends, HTTPException, Path
from typing import Annotated
from sqlalchemy.orm import Session

model_dir = os.path.join(os.getcwd(),"src","ml_models","diabetes_probability_model_v1.model")
xgb_classifier = XGBClassifier()
xgb_classifier.load_model(model_dir)

db_dependency = Annotated[Session, Depends(get_db)]

router = APIRouter(prefix="/diabetes", tags=["diabetes"])

@router.post("/probability")
async def diabetes_probability(user_input:InputRequest, db: db_dependency):
  return user_input