import requests
api_url = "http://127.0.0.1:8000/details2"

# data={
#     "username":"sahan",
#     "email":"sahan@gmail.com",
#     "age":22
# }

data={
    "username":"sahan",
    "password":"mypassword"
}
response=requests.post(api_url,json=data) #using json to post json data
response=requests.get(api_url,data=data) #using data to send data in form format

print(response.status_code)
print(response.json())