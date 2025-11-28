from pydantic import BaseModel, Field
from typing import Annotated, Literal

from enum import Enum, IntEnum

class GeneralHealthEnum(IntEnum):
  EXCELLENT = 1
  VERY_GOOD = 2
  GOOD = 3
  FAIR = 4
  POOR = 5

class AgeGroupEnum(IntEnum):
  AGE_18_24 = 1
  AGE_25_29 = 2
  AGE_30_34 = 3
  AGE_35_39 = 4
  AGE_40_44 = 5
  AGE_45_49 = 6
  AGE_50_54 = 7
  AGE_55_59 = 8
  AGE_60_64 = 9
  AGE_65_69 = 10
  AGE_70_74 = 11
  AGE_75_79 = 12
  AGE_80_99 = 13

class YesNoEnum(Enum):
  YES = "Yes"
  NO = "No"


class EducationLevelEnum(IntEnum):
  NO_SCHOOL_OR_KINDERGARTEN_ONLY = 1
  ELEMENTARY_SCHOOL = 2
  SOME_HIGH_SCHOOL = 3
  HIGH_SCHOOL_GRADUATE = 4
  SOME_COLLEGE_OR_TECHNICAL_SCHOOL = 5
  COLLEGE_GRADUATE = 6


class IncomeLevelEnum(IntEnum):
  LESS_THAN_10K = 1
  LESS_THAN_15K = 2
  LESS_THAN_20K = 3
  LESS_THAN_25K = 4
  LESS_THAN_35K = 5
  LESS_THAN_50K = 6
  LESS_THAN_75K = 7
  AT_75K_OR_MORE = 8

class InputRequest(BaseModel):
  high_blood_pressure: bool
  high_blood_cholestrol: bool
  cholestrol_checked_in_last_5_years: bool
  body_mass_index: float
  smoker: bool
  stroke: bool
  heart_attack_or_heart_disease: bool
  any_physical_activity_in_last30: bool
  consume_fruits: bool
  consume_veggies: bool
  heavy_drinker: bool
  have_health_insurance: bool
  no_dr_visit_due_to_cost: bool
  general_health_rating: GeneralHealthEnum
  mental_health:int
  physical_health:int
  difficulty_walking:bool
  is_male:bool
  age: AgeGroupEnum
  education_level:EducationLevelEnum
  income: IncomeLevelEnum

class InputRequestV3(BaseModel):
    high_blood_pressure: str
    high_blood_cholestrol: str
    cholestrol_checked_in_last_5_years: str
    body_mass_index: float
    stroke: str
    heart_attack_or_heart_disease: str
    heavy_drinker: str
    general_health_rating: str
    difficulty_walking: str
    is_male: str
    age: str