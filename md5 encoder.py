import hashlib

resultat = hashlib.md5("YOUR_PASSWORD".encode())

print(resultat.hexdigest())
