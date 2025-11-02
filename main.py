from fastapi import FastAPI

from src.routes import diabetes

app = FastAPI()

app.include_router(diabetes.router)