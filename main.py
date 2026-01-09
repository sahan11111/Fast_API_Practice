

from fastapi import FastAPI
from parameters import router as parameters_router

app = FastAPI()


@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}

@app.post("/goodbye")
def goodbye():
    return {"message": "Goodbye, World!"}
