import requests

response = requests.get('http://127.0.0.1:8080/')
print(f"code: {response.status_code}")
print(f"body: {response.text}")
