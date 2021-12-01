import datetime
import json


def serialize(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime.datetime):
        serial = obj.strftime("%Y.%m.%d %H:%M:%S")
        return serial

    return obj.__dict__


myObj = {
    'what': 'nothing happens',
    'when': datetime.datetime.now(),
}
print(json.dumps(myObj, default=serialize))
