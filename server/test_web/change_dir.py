import requests
from utils.StrUtils import to_json

response = requests.post('http://127.0.0.1:8080/change_dir', data=to_json({'path': '123'}))
print(f'code: {response.status_code}')
print(f'body: {response.text}')
