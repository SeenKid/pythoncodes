age = int(input("Quel est votre âge ? "))
age2 = int(age) + 1
prenom = str(input("Quel est ton prénom ? "))

phrase = str("Vous avez" + " " + str(age) + " " + "ans, vous aurez" + " " + str(age2) + " " + "ans l'année prochaine et votre nom est " + prenom + ".")
phrase2 = str("Vous avez {} ans, vous aurez {} ans l'année prochaine et votre nom est {}.".format(age, age2, prenom))
phrase3 = str(f"Vous avez {age} ans, vous aurez {age2} ans l'année prochaine et votre nom est {prenom}."

print(phrase)
print(phrase2)
print(phrase3)
