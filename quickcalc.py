#import et clear
import random
import os
os.system('cls')


#Déclaration de nos variables
nombre1 = random.randint(0,100)
nombre2 = random.randint(0,100)
nombrereel = nombre1 + nombre2



#on lui affiche les deux nombres et on demande si il veut additionner
print(nombre1, nombre2)
addition = input("Voulez vous additionner les deux nombres ? : (Y or N) ")

#Vérification si le nombre est bon et si la saisie est valide
if addition.lower() == "y":
    saisie = int(input("additionnez les deux nombres : "))
    if saisie != nombrereel:
        print("Votre saisie est fausse !")
    else:
        print("Bravo, le bon résultat est bel et bien " + str(nombrereel))

elif addition.lower() == "n":
    print("Vous avez choisi d'arrêter le jeu.")

else: 
    print("Votre saisie n'est pas valide. Veuillez relancer le programme")

print("Merci d'avoir joué")
