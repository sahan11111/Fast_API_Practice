import fastapi
import pydantic
from fastapi import FastAPI,Body,Query,Request
from pydantic import BaseModel,EmailStr

app = FastAPI()
'''using pydantic model for data structure validation'''
class User(BaseModel):
    username: str #username as string
    email: EmailStr #validating email format
    age: int    #age as integer

@app.post("/details")
async def user_signup(user: User):
    return {"message": "User signed up successfully", "user": user}


'''using Body to explicitly declare request body and data validation and pydantic model for data structure validation'''
class User(BaseModel):
    username: str
    password: str
    
'''Body ma default value pathauna ne milxa Body(username=sahan,password=s123) yo rakh da data lai json ma change garna pardei na'''

@app.post("/signup")
async def user_signup(user: User =Body(...)): #using Body to explicitly declare request body and data validation or required field and ... means it's required json data
    
    return {"message": "User signed up successfully", "user": user}

'''query parameters example using Query get request ma data pathaune http://127.0.0.1:8000/login?username=sahan&password=sahan123'''
@app.post("/login")
async def user_login(username = Query(...),password=Query(...)): #using Query to explicitly declare query parameters and data validation or required field and ... means it's required query parameters
    return f"User successfully logged in with username: {username} and password: {password}"
    


'''Request Object example to access request data directly'''
@app.get("/info")
async def user_info(request: Request): #using Request object to access request data directly and its data stored in request body
    client_host=(request.client.host) #getting client host info
    url=(request.url)#getting url of the request
    method=(request.method)#getting method of the request
    headers=(request.headers)#getting headers of the request
    
    ''' you can access any request data using request object'''
    return {"message": "User info received", "url": url, "method": method, "client_host": client_host, "header_agent":{headers["user-agent"]},}#"headers": headers 



''' request body example using Request Object'''
@app.post("/data")
async def user_data(request: Request):
    data = await request.json() #accessing request body data directly using request object and converting it to json format
    return {"message": "Data received", "data": data}



''' query parameters example using Request Object'''
@app.get("/query")
async def user_query(request: Request):
    query_params = request.query_params #accessing query parameters directly using request object
    
    return {"message": "Query parameters received", "query_params": query_params}


''' request body example using Request Object and accessing raw body data'''
@app.get("/details2")
async def user_signup2(request: Request):
    body=await request.body() #accessing request body data directly using request object
    
    return {"message": "Data received", "data": body}