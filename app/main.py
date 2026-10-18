from fastapi import FastAPI

app = FastAPI(title="Recipe-API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/recipes")
def recipes():
    return {"welcometext": "Welcome to the Recipe API"}

