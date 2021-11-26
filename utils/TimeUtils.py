import datetime


def floattime_to_datatime(t: float) -> datetime.datetime:
    return datetime.datetime.utcfromtimestamp(t)
