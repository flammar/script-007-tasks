import json

import requests
from utils.StrUtils import to_json

response = requests.get('http://127.0.0.1:8080/files/1.txt')
print(f'code: {response.status_code}')
# print(f'body: {response.text}')
pretty_response = to_json(json.loads(response.text))
print(f'body: {pretty_response}')
