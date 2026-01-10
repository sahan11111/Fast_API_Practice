import requests
api_url = "http://127.0.0.1:8000/signup"

data={
    "username":"sahan_tak",
    "email":"sahan@gmail.com",
    "age":22
}

response=requests.post(api_url,json=data)


print(response.status_code)
print(response.json())