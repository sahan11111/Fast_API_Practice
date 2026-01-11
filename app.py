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



# class User(BaseModel):
#     username: str
#     password: str
    
# '''Body ma default value pathauna ne milxa Body(username=sahan,password=s123) yo rakh da data lai json ma change garna pardei na'''

# @app.post("/signup")
# async def user_signup(user: User =Body(...)): #using Body to explicitly declare request body and data validation or required field and ... means it's required json data
    
#     return {"message": "User signed up successfully", "user": user}

'''query parameters example using Query get request ma data pathaune http://127.0.0.1:8000/login?username=sahan&password=sahan123'''
@app.post("/login")
async def user_login(username = Query(...),password=Query(...)): #using Query to explicitly declare query parameters and data validation or required field and ... means it's required query parameters
    return f"User successfully logged in with username: {username} and password: {password}"
    