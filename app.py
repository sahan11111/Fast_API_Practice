import fastapi
import pydantic
from fastapi import FastAPI
from pydantic import BaseModel,EmailStr

app = FastAPI()

class User(BaseModel):
    username: str
    email: EmailStr
    age: int

@app.post("/signup")
async def user_signup(user: User):
    return {"message": "User signed up successfully", "user": user}