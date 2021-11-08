iAgePersonne = int(input("Quel est votre âge = : "))

iAgeLimite = 18

if iAgePersonne < iAgeLimite:
    sReponse = "Vous êtes mineur"
else:
    sReponse = "Vous êtes majeur"

print(sReponse)
