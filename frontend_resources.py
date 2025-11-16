from src.pydantic_models.request_models import GeneralHealthEnum, AgeGroupEnum, IncomeLevelEnum, EducationLevelEnum, InputRequest

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