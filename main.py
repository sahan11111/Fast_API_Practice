import fastapi
import uvicorn

from fastapi import FastAPI


app=FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}

@app.post("/goodbye")
def goodbye():
    return {"message": "Goodbye, World!"}