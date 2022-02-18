#import et clear
import os, sys
import random
os.system('cls' if sys.platform == 'win32' else 'clear')

#Déclaration de nos variables
nombre1 = random.randint(0,100)
nombre2 = random.randint(0,100)
nombrereel = nombre1 + nombre2

#on lui affiche les deux nombres et on demande si il veut additionner 
print(nombre1, nombre2)
addition = input("Voulez vous additionner les deux nombres ? : (Y or N) ")

#Vérification si le nombre est bon et si la saisie est valide
if addition == "Y" or addition == "y":
    saisie = int(input("additionnez les deux nombres : "))
    if saisie != nombrereel:
        print("Votre saisie est fausse !")
    else: 
        print("Bravo, le bon résultat est bel et bien " + str(nombrereel))

elif addition == "N" or addition == "n":
    print("Vous avez choisi de ne pas faire le calcul...")

elif addition != "Y" and "y" and "N" and "n":
    print("Je n'ai pas compris votre saisie.")
    
#######################################
    
print("Fin du programme...")
