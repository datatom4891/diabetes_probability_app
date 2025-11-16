from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy import create_engine, Column, Integer, Float, String, Boolean, ForeignKey

SQLITE_DATABASE_URL = 'sqlite:///./diabetes_probability_app.db'
engine = create_engine(SQLITE_DATABASE_URL)

class Base(DeclarativeBase):
  pass

# class DiabetesProbability(Base):
#   __tablename__ = "predictions"
  
#   id: Mapped[int] = mapped_column(primary_key=True)
#   diabetes_probability:Mapped[float]
#   probability_prediction_explanation:Mapped[str]
#   high_blood_pressure:Mapped[bool]
#   high_blood_cholestrol:Mapped[bool]
#   cholestrol_checked_in_last_5_years:Mapped[bool]
#   body_mass_index:Mapped[int]
#   smoker:Mapped[bool]
#   stroke:Mapped[bool]
#   heart_attack_or_heart_disease:Mapped[bool]
#   any_physical_activity_in_last30:Mapped[bool]
#   consume_fruits:Mapped[bool]
#   consume_veggies:Mapped[bool]
#   heavy_drinker:Mapped[bool]
#   have_health_insurance:Mapped[bool]
#   no_dr_visit_due_to_cost:Mapped[bool]
#   general_health_rating:Mapped[int]
#   mental_health:Mapped[int]
#   physical_health:Mapped[int]
#   difficulty_walking:Mapped[bool]
#   is_male:Mapped[bool]
#   age:Mapped[int]
#   education_level:Mapped[int]
#   income:Mapped[int]

class DiabetesProbabilityV3(Base):
  __tablename__ = "predictions_v3"
  
  id: Mapped[int] = mapped_column(primary_key=True)
  diabetes_probability:Mapped[float]
  probability_prediction_explanation:Mapped[str]
  high_blood_pressure:Mapped[bool]
  high_blood_cholestrol:Mapped[bool]
  cholestrol_checked_in_last_5_years:Mapped[bool]
  body_mass_index:Mapped[int]
  stroke:Mapped[bool]
  heart_attack_or_heart_disease:Mapped[bool]
  heavy_drinker:Mapped[bool]
  general_health_rating:Mapped[int]
  difficulty_walking:Mapped[bool]
  is_male:Mapped[bool]
  age:Mapped[int]

Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)