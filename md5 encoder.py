import hashlib

resultat = hashlib.md5("ez".encode())

print(resultat.hexdigest())