import json


class MyRequest:
    def __init__(self, id_, user_name, is_processed):
        self.id = id_
        self.name = user_name
        self.processed = is_processed

    def __repr__(self):
        return f'MyRequest({self.id},"{self.name}",{self.processed})'


def custom_decoder(obj):
    # calls for any dict
    if 'date' in obj and 'time' in obj:
        return ' '.join([obj['date'], obj['time'], obj['zone']])
    if '__type__' in obj and obj['__type__'] == 'MyRequest':
        return MyRequest(obj['id'], obj['who'], obj['request_processed'])
    return obj


text = """
{
    "timestamp": {
        "date": "2021.11.30",
        "time": "08:51:24",
        "zone": "utc+3"
    },
    "timestamp1": {
        "date": "2021.11.30",
        "time": "09:51:24",
        "zone": "utc+3"
    },
    "requests": [
        {
            "__type__": "MyRequest",
            "id": 1000,
            "request_processed": true,
            "who": "myadmin"
        },
        {
            "__type__": "MyRequest",
            "id": 1001,
            "request_processed": true,
            "who": "myuser"
        }
    ]
}
"""
data = json.loads(text, object_hook=custom_decoder)

print('data:', data)
