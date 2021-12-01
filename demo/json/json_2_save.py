import json


def to_json(obj):
    return json.dumps(obj, indent=2, sort_keys=True)


myObj = {
    'who': 'myuser',
    'id': 1000,
    'request_processed': True,
}
print(to_json(myObj))
