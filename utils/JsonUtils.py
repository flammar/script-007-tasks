import datetime
import json
from typing import Callable


def add_conv(cond: Callable[[object], bool], conv: Callable[[object], object],
             base: Callable[[object], object] = lambda x: x) -> Callable[[object], object]:
    # def res(my_input: object) -> object:
    return lambda my_input: conv(my_input) if cond(my_input) else base(my_input)


def bytes2str(b: bytes) -> str:
    return b.decode() if b else None


def str2bytes(s: str) -> bytes:
    return s.encode() if s else None


def is_datetime(obj):
    return isinstance(obj, datetime.datetime)


def is_datetime_ser(obj):
    return isinstance(obj, dict) and obj.get("__type__") == "datetime.datetime" and "isoformat" in obj


def datetime_encode(obj: datetime.datetime):
    return {"__type__": "datetime.datetime", "isoformat": obj.isoformat()}


def datetime_decode(obj: dict):
    return datetime.datetime.fromisoformat(obj["isoformat"])


json_serialize_helper = add_conv(lambda o: isinstance(o, bytes), bytes2str, add_conv(is_datetime, datetime_encode))


def to_json(data):
    return json.dumps(data, default=json_serialize_helper)