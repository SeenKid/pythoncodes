argent = float(input("Entrez la somme d'argent que vous possédez : "))
computer = float(input("Entrez le prix de l'ordinateur que vous voulez payer : "))
argent_restant = argent - computer
print()


if computer > argent:
    print("Vous ne pouvez pas acheter cet ordinateur, il est trop cher.")
else:
    confirmation = input("êtes vous sûr de vouloir payer cet ordinateur ? Il vous restera {} CHF. (Y/N) ".format(argent_restant))
    if confirmation == str("Y"):
        print("Vous avez acheté l'ordinateur, il vous reste {} CHF.".format(argent_restant))
    else:
        print("Il semble que vous ayez annulé la commande.")

print()
print("Au revoir et à bientôt dans notre magasin !")
print()
