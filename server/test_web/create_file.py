import requests
from utils.StrUtils import to_json

response = requests.post('http://127.0.0.1:8080/files', data=to_json({
    'filename': 'poem.txt',
    'content': 'New file content\r\nIn two lines!',
}))
print(f'code: {response.status_code}')
print(f'body: {response.text}')
