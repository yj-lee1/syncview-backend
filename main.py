
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from Cloud Run"}


@app.get("/login")
def login():
    return "Login OK"
