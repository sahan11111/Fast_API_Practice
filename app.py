import fastapi
import pydantic
from fastapi import FastAPI,Body,Query
from pydantic import BaseModel,EmailStr

app = FastAPI()

# class User(BaseModel):
#     username: str #username as string
#     email: EmailStr #validating email format
#     age: int    #age as integer

# @app.post("/signup")
# async def user_signup(user: User):
#     return {"message": "User signed up successfully", "user": user}



class User(BaseModel):
    username: str
    password: str
    
'''Body ma default value pathauna ne milxa Body(username=sahan,password=s123) yo rakh da data lai json ma change garna pardei na'''

@app.post("/signup")
async def user_signup(user: User =Body(...)): #using Body to explicitly declare request body and data validation or required field and ... means it's required json data
    
    return {"message": "User signed up successfully", "user": user}
