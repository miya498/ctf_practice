import requests

url = "http://example.com/login"
data = {
    "username": "admin",
    "password": "password123"
}

response = requests.post(url, data=data)
print(response.text)
