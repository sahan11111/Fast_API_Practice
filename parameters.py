
from fastapi import FastAPI,APIRouter

# Example endpoint with query parameter
app = FastAPI()
database = {
    "alice": {"age": 30, "city": "New York"},
    "bob": {"age": 25, "city": "Los Angeles"},
}
@app.get("/sahan")
def read_sahan(name: str):
    return {"message": f"Hello, {name}!"}

# @app.get("/{username}")
# def find_user(username: str):
#     if username in database:
#         return database[username]
#     else:
#         return {"error": "User not found"}
   
   
#query parameters example
'''http://127.0.0.1:8000/?username=sahan'''

# @app.get("/")
# def find_user(username):
#     return {"username": username}

# @app.get("/")
# def find_user(username):
#     '''checking in database'''
#     if username in database:
#         return database[username]
#     else:
#         return {"error": "User not found"}
    
@app.get("/")
def find_user(username,password):
    return {"username": username, "password": password}

# @app.get("/")
# def find_user(username,password):
#     '''checking in database with password'''
#     if username in database and password=="secret":
#         return database[username]
#     else:
#         return {"error": "User not found or incorrect password"}
    