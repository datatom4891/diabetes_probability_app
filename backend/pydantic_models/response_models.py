from pydantic import BaseModel
from typing import Optional
from lime.explanation import Explanation

class ModelResponse(BaseModel):
  probability_str: str | None = "Model was unable to estimate a probability for you"
  explanation_str: str | None 