import jwt
import datetime
import fastapi
from fastapi import FastAPI
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from fastapi import Depends

app=FastAPI()


security=HTTPBearer()

@app.get("/get-token")
async def get_access_token():
    return get_token()

SECRET_KEY="LMO123"


payloads={
    "user":"sahan"
}


def get_token():
    token=jwt.encode(payloads,SECRET_KEY,algorithm="HS256",) 
    return token




@app.get("/dashboard")
async def dashboard(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Returns a welcome message to the authenticated user on the dashboard.
    """
    token=credentials.credentials
    
    if verify_token(token) == False:
        return "return invalid token"
    
    return "welcome to dashboard"
    
    
    
    
def verify_token(token):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=["HS256"])
        return True
    except:
        return False
    



