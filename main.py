<<<<<<< HEAD
import fastapi
=======
from fastapi import FastAPI
from parameters import router as parameters_router

app = FastAPI()


@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}

@app.post("/goodbye")
def goodbye():
    return {"message": "Goodbye, World!"}
>>>>>>> 3c146f662939f0b2b8e5d0be644979299e8811b3
