#--*-- coding:utf-8 --*--
#-------------------------------------------------------------------------------
# Name:       Projet GP211 Gestion réservations vols
#
# Nom :         PICHON      UBAIDULLOEV
# Prenom :      Lucas       Rustam
#
# Classe :      2PE         2PE
# Groupe :      1           1
#
#-------------------------------------------------------------------------------


import time

from lib_gestionCompagnies import *
from lib_gestionAeroports import *
from lib_gestionAvions import *
from lib_gestionPassagers import *
from lib_gestionReservations import *
from lib_gestionVols import *

print("*************************************************** \n--------------------------------------------------- \n              Programme principal           --------------------------------------------------- \n***************************************************")

menu_choix = 0


# Lancement du programme
#AffichageMenu()


while True:
    menu_choix = int(input("Rentrez votre choix (valeur entre 1-7): \n 1- gestion Compagnies \n 2- gestion Aeroports\n 3- gestion Avions\n 4- gestion Passagers\n 5- gestion Vols\n 6- gestion Reservations\n 7- Sortie\n\n Reponse :\n"))
    
    
    if menu_choix == 1:
        gestionCompagnies()

    elif menu_choix == 2:
        gestionAeroports()

    elif menu_choix == 3:
        gestionAvions()

    elif menu_choix == 4:
        gestionPassagers()

    elif menu_choix == 5:
        gestionVols()

    elif menu_choix == 6:
        gestionReservations()

    elif menu_choix == 7:
        break


print("Au revoir")




