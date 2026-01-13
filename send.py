import requests  # Import the requests library to make HTTP requests

# Define the URL for the API endpoint
url = "http://127.0.0.1:8000/dashboard"

# Set up the headers with Authorization token (JWT Bearer token)
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoic2FoYW4ifQ.0mJDLzR-rqrNKoHr3tx3l6jvJ-iid3DQ3_9AyfATzr8"
}

# Make a GET request to the specified URL with the headers
response = requests.get(url, headers=headers)

# Print the HTTP status code of the response
print(response.status_code)

# Print the JSON content of the response
print(response.json())

# Print the text content of the response
print(response.text)