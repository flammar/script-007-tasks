import json

text = """
{
  "id": 1000,
  "request_processed": true,
  "who": "myuser"
}
"""
data = json.loads(text)
print('type:', type(data))
print('data:', data)
print('who:', data['who'])
