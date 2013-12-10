import urllib


def sanitize(str):
    if str:
        return urllib.unquote(str.encode('utf-8')).decode('utf-8')
    else:
        return str
