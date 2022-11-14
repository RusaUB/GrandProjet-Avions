#--*-- coding:utf-8 --*--

from lib_commun import ouverture_fichier_txt, ecriture_fichier_txt


def gestionAvions() :
    """
    Cette fonction a pour objectif
    IN :
    OUT :
    """

    def ajoutAvion(*donneesAvion) :
        """
        Cette fonction a pour objectif
        IN :
        OUT :
        """
        nomfichier = "avions.txt"
        fichierCompagnies = "compagnies.txt"
        fichierAeroports = "aeroports.txt"
        L_avions = ouverture_fichier_txt(nomfichier)
        L_compagnies = ouverture_fichier_txt(fichierCompagnies)
        L_aeroports = ouverture_fichier_txt(fichierAeroports)


        existe_compagnie = False  # indicateur d'existence de la compagnie dans le fichier compagnies.txt
        existe_aeroport = False  # indicateur d'existence de l aeroport dans le fichier aeroports.txt

        # Verification si l avion existe deja dans avions.txt





        # Verification la compagnie dans compagnies.txt





        # Verification l aeroport  dans le fichier aeroports.txt





        # Ajout avion








    def modificationAvion(*majAvion) :
        """
        Cette fonction a pour objectif
        IN :
        OUT :
        """







        # Verification d existence de l avion dans avions.txt








        # Verification d existence de l aeroport dans aeroports.txt





        # mise a jour de l avion




        # reecriture du fichier avions.txt modifie




    def suppressionAvion(avion) :
        """
        Cette fonction a pour objectif
        IN :
        OUT :
        """
        nomfichier = "avions.txt"
        fichierVols = "vols.txt"
        indice = 0  # indicateur donnant le rang ou l avion a ete trouvee

        existe_avion = False  # indicateur d'existence de aeroport/avion  dans le fichier avions.txt
        existe_vol = False  # indicateur d'existence de aeroport/vol  dans le fichier vols.txt

        L_avions = ouverture_fichier_txt(nomfichier)
        L_vols = ouverture_fichier_txt(fichierVols)

        # Verification avion dans avions.txt







        # Verification vol/avion  dans le fichier vols.txt







        # suppression de l avion








        # reecriture du fichier modifie




    def affichageAvions() :
        """
        Cette procédure a pour objectif d'afficher l'ensemble des informations administratives des avions.
        Soit : immatavion,nomcompagnie,aerostation,typeavion,nbplacesAffT, nbplacesPremT, nbplacesEcoT
        IN : aucun paramètre en entrée
        OUT : aucun retour
        """
        ##################################################
        #ouverture et recuperation du contenu du fichier
        ##################################################
        nomfichier = "avions.txt"
        L_avions = ouverture_fichier_txt(nomfichier)

        for i in range(0,len(L_avions)) :
            L_avions[i][-1] = (L_avions[i][-1][0:-1]) # on enleve le \n du numéro de tph

        print("***********************************************************************************************************")
        print("*                                          Descriptif avions                                              *")
        print("***********************************************************************************************************")
        print("*   Avion   *        Compagnie      *         Aeroport rattachement     *   TypeAvion   * AFF * PRE * ECO *")
        print("***********************************************************************************************************")

        for i in range(0,len(L_avions)) :
            print("* {:<8}  * {:<20}  * {:<32}  *  {:<11}  * {:>3} * {:>3} * {:>3} *" . format(L_avions[i][0], L_avions[i][1], L_avions[i][2], L_avions[i][3], L_avions[i][4], L_avions[i][5], L_avions[i][-1]))

        print("***********************************************************************************************************\n")







    ##################################################
    #
    ##################################################
    while True:
        menu_choix = int(input("Rentrez votre choix ( valeur entre 1-5): \n 1- Ajout avion \n 2- Modification avion\n 3- Suppression avion\n 4- Affichage avions\n 5- Sortie\n\n Reponse :\n"))

        if menu_choix == 1 :
            immat = input("Saisissez l immatriculation de l'avion\n->")
            compagnie = input("Saisissez la compagnie de l'avion\n->")
            rattachement = input("Saisissez l aeroport de rattachement de l'avion\n->")
            typeAvion = input("Saisissez le type avion de l'avion\n->")
            nbPlacesAFF = input("Saisissez le nombre de places AFFAIRE de l avion\n->")
            nbPlacesTRE = input("Saisissez le nombre de places PREMIUM de l avion\n->")
            nbPlacesECO = input("Saisissez le nombre de places ECONOMIQUE de l avion\n->")
            ajoutAvion(immat,compagnie,rattachement,typeAvion,nbPlacesAFF,nbPlacesTRE,nbPlacesECO)

        if menu_choix == 2 :
            pass

        if menu_choix == 3 :
            pass

        if menu_choix == 4 :
            affichageAvions()


        if menu_choix == 5 :
            return
