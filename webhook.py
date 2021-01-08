import json
from urllib import request
from urllib.error import HTTPError


WEBHOOK_URL = 'WEBHOOK LINK'

payload = {
    'content': "MESSAGE A SPAM"
    'content': "MESSAGE A SPAM"
    'content': "MESSAGE A SPAM"
    'content': "MESSAGE A SPAM"
    'content': "MESSAGE A SPAM"
    'content': "MESSAGE A SPAM"
    'content': "MESSAGE A SPAM"
    'content': "MESSAGE A SPAM"
}

headers = {
    'Content-Type': 'application/json',
    'user-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
}

req = request.Request(url=WEBHOOK_URL,
                      data=json.dumps(payload).encode('utf-8'),
                      headers=headers,
                      method='POST')

try:
    response = request.urlopen(req)
    print(response.status)
    print(response.reason)
    print(response.headers)
except HTTPError as e:
    print('ERROR')
    print(e.reason)
    print(e.hdrs)
    print(e.file.read())
