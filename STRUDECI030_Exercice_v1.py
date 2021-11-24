#============================================================================
#====         EPTM - Ecole professionnelle technique et des métiers
#============================================================================
#====                      Programmation Module M319
#====                     ---------------------------
#====------------------------------------------------------------------------
#==== Nom du projet de programme        : STRUDECI030_Enoncé_v1
#==== Langage de programmation utilisé  : Python
#==== Version                           : V1.0
#==== Nom du(des) fichier(s) source     : STRUDECI030_Enoncé_v1.py
#====------------------------------------------------------------------------
#==== Créateur (Nom, Prénom)            : Berlemont Yann
#==== Classe                            : Info1A
#==== Date de création                  : 22.11.21
#==== Date de la dernière modification  : 22.11.21
#====------------------------------------------------------------------------
#==== Description succincte du programme:
#==== ----------------------------------
#==== 
#====
#====
#====
#============================================================================

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
if addition == "Y" or addition == "y":
    saisie = int(input("additionnez les deux nombres : "))
    if saisie != nombrereel:
        print("Votre saisie est fausse !")
    else: 
        print("Bravo, le bon résultat est bel et bien " + str(nombrereel))
elif addition != "Y" and "y" and "N" and "n":
    print("Je n'ai pas compris votre saisie.")