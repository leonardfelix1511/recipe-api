from fastapi import FastAPI
from app.database import engine
from app.database import Base
from app.models import Rezept

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Recipe-API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def recipes():
    return {"welcometext": "Welcome to the Recipe API"}

