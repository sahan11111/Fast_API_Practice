import requests

url="http://127.0.0.1:8000/hello"

a=requests.get(url)

print(a.text)