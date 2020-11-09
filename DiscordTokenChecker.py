#coding:utf-8

import requests
import time


with open("tokens.txt") as f:
    for line in f:
        token = line.strip("\n")
        headers = {'Content-Type': 'application/json', 'authorization': token}
        url = "https://discordapp.com/api/v6/users/@me/library"
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            print("{} worked.".format(line.strip("\n")))
        else:
            print("Votre token ne fonctionne pas")
