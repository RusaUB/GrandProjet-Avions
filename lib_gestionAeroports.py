#--*-- coding:utf-8 --*--

from lib_commun import ouverture_fichier_txt, ecriture_fichier_txt


def gestionAeroports() :
    """
    Cette fonction a pour objectif
    IN :
    OUT :
    """

    def ajoutAeroport(*donneesAerop) :
        """
        Cette fonction a pour objectif
        IN :
        OUT :
        """
        nomfichier = "aeroports.txt"
        L_aeroports = ouverture_fichier_txt(nomfichier)


        """
            AJOUTER AEROPORT
        """

        for i in L_aeroports:
            if i[0] == donneesAerop[0]:
                print("La compagnie existe déjà")
                return

        print("La compagnie n'est pas dans la base de données")


        # Preparation de la nouvelle compagnie
        new_aeroport = []

        for elem in donneesAerop:
            new_aeroport.append(elem)

        # Ajout de \n de fin ligne
        new_aeroport.append("\n")

        # Ajout dans la liste des compagnies
        L_aeroports.append(new_aeroport)

        # Reecriture du fichier actualise
        ecriture_fichier_txt(L_aeroports,nomfichier)


    def suppressionAeroport(aeroport) :
        """
        Cette fonction a pour objectif
        IN :
        OUT :
        """



        """
            SUPPRESSION AEROPORT
            Не должен конфронтировать с vol,avions
        """

        L_aeroports = ouverture_fichier_txt("aeroports.txt")
        L_avions = ouverture_fichier_txt("avions.txt")

        #Существует ли аэропорт
        if any(aeroport in s for s in L_aeroports):
            for k in range(len(L_aeroports)):
                if L_aeroports[k][0] == aeroport:
                    #Есть ли в этом аэропорту самолеты
                    if not any(aeroport in s for s in L_avions):
                        L_aeroports[k].clear()
                        ecriture_fichier_txt(L_aeroports,"aeroports.txt")
                    else :
                        print('il y a avion dans aeroprt')
        else:
            print("aeroport n'existe pas")


        # Verification aeroport  prevu pour un vol dans le fichier vols.txt






        # suppression de la compagnie





        # reecriture du fichier modifie
        #ecriture_fichier_txt(L_aeroports, nomfichier)



    def affichageAeroports() :
        """
        Cette procédure a pour objectif d'afficher l'ensemble des informations administratives des aeroports.
        Soit : nomaeroport,nomville,pays,altitude
        IN : aucun paramètre en entrée
        OUT : aucun retour
        """
        ##################################################
        #ouverture et recuperation du contenu du fichier
        ##################################################
        nomfichier = "aeroports.txt"
        L_aeroports = ouverture_fichier_txt(nomfichier)

        for i in range(0,len(L_aeroports)) :
            L_aeroports[i][3] = (L_aeroports[i][3][0:-1]) # on enleve le \n du numéro de tph

        print("*******************************************************************************************************************")
        print("*                                              Descriptif aeroports                                               *")
        print("*******************************************************************************************************************")
        print("*                Aeroport               *          Ville           *                Pays               *    Alt   *")
        print("*******************************************************************************************************************")

        for i in range(0,len(L_aeroports)) :
            print("*   {:<32}    *  {:<22}  *  {:<32}  *  {:>5}  *" . format(L_aeroports[i][0], L_aeroports[i][1], L_aeroports[i][2], L_aeroports[i][3]))

        print("*******************************************************************************************************************\n")








    ##################################################
    #
    ##################################################
    while True:
        menu_choix = int(input("Rentrez votre choix ( valeur entre 1-5): \n 1- Ajout aeroport \n 2- Suppression aeroport\n 3- Affichage aeroports\n 4- Sortie\n\n Reponse :\n"))

        if menu_choix == 1 :
            aeroport = input("Saisissez le nom de l aeroporte\n->")
            ville = input("Saisissez la ville localisation de l aeroport\n->")
            pays = input("Saisissez le pays de l aeroport\n->")
            altitude = input("Saisissez l altitude de l aeroport\n->")
            ajoutAeroport(aeroport,ville,pays,altitude)

        if menu_choix == 2 :
            aeroport = input("Saisissez le nom de l aeroporte\n->")
            suppressionAeroport(aeroport)




        if menu_choix == 3 :
            affichageAeroports()


        if menu_choix == 4 :
            return
