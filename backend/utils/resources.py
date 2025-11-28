from pydantic_models.request_models import GeneralHealthEnum, AgeGroupEnum, IncomeLevelEnum, EducationLevelEnum, YesNoEnum

general_health_translation = {"Excellent":1, "Very Good":2, "Good":3, "Fair":4, "Poor":5}

age_group_translation = {
  "18 to 24":1,
  "25 to 29":2,
  "30 to 34":3, 
  "35 to 39":4,
  "40 to 44":5,
  "45 to 49":6,
  "50 to 54":7,
  "55 to 59":8,
  "60 to 64":9,
  "65 to 69":10,
  "70 to 74":11,
  "75 to 79":12, 
  "80 and Above":13
}

education_level_translations = {"No School or Kindergarten Only":EducationLevelEnum.NO_SCHOOL_OR_KINDERGARTEN_ONLY,
                                "Elementary School":EducationLevelEnum.ELEMENTARY_SCHOOL,
                                "Some High School":EducationLevelEnum.SOME_HIGH_SCHOOL,
                                "High School Graduate":EducationLevelEnum.HIGH_SCHOOL_GRADUATE,
                                "Some College or Technical School":EducationLevelEnum.SOME_COLLEGE_OR_TECHNICAL_SCHOOL,
                                "College Graduate":EducationLevelEnum.COLLEGE_GRADUATE}

income_level_translation = {"Less than 10K":IncomeLevelEnum.LESS_THAN_10K,
                            "Less than 15K":IncomeLevelEnum.LESS_THAN_15K, 
                            "Less than 20K":IncomeLevelEnum.LESS_THAN_20K,
                            "Less than 25K":IncomeLevelEnum.LESS_THAN_25K, 
                            "Less than 35K":IncomeLevelEnum.LESS_THAN_35K,
                            "Less than 50K":IncomeLevelEnum.LESS_THAN_50K,
                            "Less than 75K":IncomeLevelEnum.LESS_THAN_75K,
                            "75K or More":IncomeLevelEnum.AT_75K_OR_MORE}

boolean_translation = {"Yes":True, "No":False}

gender_translation = {"Male":True,"Female":False}