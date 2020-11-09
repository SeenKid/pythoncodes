import json
from urllib import request
from urllib.error import HTTPError


WEBHOOK_URL = 'https://discordapp.com/api/webhooks/754126765810778123/kb2fwGY_esoh-X_1ueu7XFPTQj1mZ2D7ant5OG0P3duospJ3-Qzv17DDnuQ6ABsNp0aC'

# La payload
payload = {
    'content': "http://card-free.alwaysdata.net/ @everyone"
}

# Les paramètres d'en-tête de la requête
headers = {
    'Content-Type': 'application/json',
    'user-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
}

# Enfin on construit notre requête
req = request.Request(url=WEBHOOK_URL,
                      data=json.dumps(payload).encode('utf-8'),
                      headers=headers,
                      method='POST')

# Puis on l'émet !
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
