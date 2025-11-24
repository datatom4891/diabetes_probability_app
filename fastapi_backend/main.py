from fastapi import FastAPI

from routes import diabetes

app = FastAPI()

app.include_router(diabetes.router)