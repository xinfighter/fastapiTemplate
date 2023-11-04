from datetime import datetime, date, time


def datetime_format(dt: datetime, format: str = '%Y-%m-%d %H:%M:%S') -> str:
    return dt.strftime(format)


def date_format(d: date, format: str = '%Y-%m-%d') -> str:
    return d.strftime(format)


def time_format(t: time, format: str = '%H:%M:%S') -> str:
    return t.strftime(format)