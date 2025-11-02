from pydantic import BaseModel
from typing import Optional

class ModelResponse(BaseModel):
  probability: float
  explanation: str | None = "Not Available"