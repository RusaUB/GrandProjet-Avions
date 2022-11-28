#--*-- coding:utf-8 --*--

from lib_commun import ouverture_fichier_txt, ecriture_fichier_txt 


def gestionVols() :
    """
    Cette fonction a pour objectif
    IN :  numvol, nomcompagnie ,aeroportDep,dateDep,heureDep, aeroportArr,dateArr, heureArr,immatavion, nbplacesAffR, nbplacesPremR, nbplacesEcoR
    OUT :
    """

    def ajoutVol(*donneesVol) :
        """
        Cette fonction a pour objectif
        IN :
        OUT :
        """
        nomfichier = "vols.txt"
        fichierCompagnies = "compagnies.txt"
        fichierAeroports = "aeroports.txt"
        fichierAvions = "avions.txt"

        L_vols = ouverture_fichier_txt(nomfichier)

        L_compagnies = ouverture_fichier_txt(fichierCompagnies)
        L_aeroports = ouverture_fichier_txt(fichierAeroports)
        L_avions = ouverture_fichier_txt(fichierAvions)

        existe_aeroport_dep = False  # indicateur d'existence de l aeroport de depart dans le fichier aeroports.txt
        existe_aeroport_arr = False  # indicateur d'existence de l aeroport d arrivee dans le fichier aeroports.txt        
        existe_compagnie = False  # indicateur d'existence de la compagnie dans le fichier compagnies.txt
        existe_avion = False  # indicateur d'existence de l aeroport dans le fichier aeroports.txt

        #numvol, nomcompagnie ,aeroportDep,dateDep,heureDep, aeroportArr,dateArr, heureArr,immatavion, nbplacesAffR, nbplacesPremR, nbplacesEcoR

        #===============================================================================================
        # Pour identifier un vol, il faut connaitre numvol, nomcompagnie ,aeroportDep,dateDep,heureDep
        #===============================================================================================
        
		
		

        # Verification la compagnie dans compagnies.txt
        
		
		
		
		
                            

        # Verification de l aeroport de depart dans le fichier aeroports.txt
        
		
		
		
		
		

        # Verification de l aeroport d arrivee dans le fichier aeroports.txt
        
		
		
		
		

        #numvol, nomcompagnie ,aeroportDep,dateDep,heureDep, aeroportArr,dateArr, heureArr,immatavion, nbplacesAffR, nbplacesPremR, nbplacesEcoR

        # Verification de l avion dans le fichier avions.txt
        
		
		
		
		
		

        # Ajout vol
        
		
		
		
		
		
		
		
		suivre")


    def modificationVol(*donneesVolmod) :
        """
        Cette fonction a pour objectif
        IN :  numvol,aeroportDep,jourDep,heureDep,aeroportArr,heureDepNew
        OUT :
        """
        nomfichier = "vols.txt"

        L_vols = ouverture_fichier_txt(nomfichier)

        indice = 0  # indicateur donnant le rang ou le vol a ete trouve
        existe_vol = False  # indicateur d'existence du vol dans le fichier vols.txt

        # format fichier vols.txt
        # numvol, nomcompagnie ,aeroportDep,dateDep,heureDep, aeroportArr,dateArr, heureArr,immatavion, nbplacesAffR, nbplacesPremR, nbplacesEcoR

        #===============================================================================================
        # Pour identifier un vol, il faut connaitre numvol, aeroportDep,dateDep,heureDep,aeroportArr
        #===============================================================================================

        
		
		
		
		
		
		
		



    def suppressionVol(*donneesVolsup) :
        """
        Cette fonction a pour objectif
        IN :  numvol,aeroportDep,jourDep,heureDep,aeroportArr,heureDepNew
        OUT :
        """
        nomfichier = "vols.txt"

        L_vols = ouverture_fichier_txt(nomfichier)

        
		

        # format fichier vols.txt
        # numvol, nomcompagnie ,aeroportDep,dateDep,heureDep, aeroportArr,dateArr, heureArr,immatavion, nbplacesAffR, nbplacesPremR, nbplacesEcoR

        #===============================================================================================
        # Pour identifier un vol, il faut connaitre numvol, aeroportDep,dateDep,heureDep,aeroportArr
        #===============================================================================================

        
		
		
		
		
		
		
		






    def affichageVols() :
        """
        Cette procédure a pour objectif d'afficher l'ensemble des informations administratives des volss.
        Soit : numvol, nomcompagnie ,aeroportDep,dateDep,heureDep, aeroportArr,dateArr, heureArr,immatavion, nbplacesAffR, nbplacesPremR, nbplacesEcoR
        IN : aucun paramètre en entrée
        OUT : aucun retour
        """
        ##################################################
        #ouverture et recuperation du contenu du fichier
        ##################################################
        nomfichier = "vols.txt"
        L_vols = ouverture_fichier_txt(nomfichier)

        for i in range(0,len(L_vols)) :
            L_vols[i][-1] = (L_vols[i][-1][0:-1]) # on enleve le \n du numéro de tph

        print("***********************************************************************************************************************************************************************************************")
        print("*                                                                                  Descriptif des vols                                                                                        *")
        print("***********************************************************************************************************************************************************************************************")
        print("*  NumVol  *       Compagnie      *             Aeroport DEP         *   Date DEP   *  Heure DEP *             Aeroport ARR         *   Date ARR   * Heure ARR  *   Avion   * AFF * PRE * ECO *")
        print("***********************************************************************************************************************************************************************************************")

        for i in range(0,len(L_vols)) :
            print("* {:<8} * {:<20} * {:<32} * {:<12} * {:<10} * {:<32} * {:<12} * {:<10} * {:<8}  * {:>3} * {:>3} * {:>3} *" . format(L_vols[i][0], L_vols[i][1], L_vols[i][2], L_vols[i][3], L_vols[i][4], L_vols[i][5], L_vols[i][6], L_vols[i][7], L_vols[i][8], L_vols[i][9], L_vols[i][10], L_vols[i][-1]))

        print("***********************************************************************************************************************************************************************************************\n")



    ##################################################
    #
    ##################################################
    while True:
        menu_choix = int(input("Rentrez votre choix ( valeur entre 1-5): \n 1- Ajout vol \n 2- Modification vol\n 3- Suppression vol\n 4- Affichage vols\n 5- Sortie\n\n Reponse :\n"))

        if menu_choix == 1 :
            #numvol, nomcompagnie ,aeroportDep,dateDep,heureDep, aeroportArr,dateArr, heureArr,immatavion, nbplacesAffR, nbplacesPremR, nbplacesEcoR
            numvol = input("Saisissez le numero du vol\n->")
            compagnie = input("Saisissez la compagnie assurant le vol\n->")
            aeroportDep = input("Saisissez l aeroport de depart du vol\n->")
            dateDep = input("Saisissez le jour du vol\n->")
            heureDep = input("Saisissez l heure du vol\n->")
            aeroportArr = input("Saisissez l aeroport d arrivee du vol\n->")
            dateArr = input("Saisissez le jour d arrivee du vol\n->")
            heurArr = input("Saisissez l heure d arrivee du vol\n->")
            immat = input("Saisissez l immatriculation de l'avion\n->")
            nbPlacesAFF = input("Saisissez le nombre de places AFFAIRE de l avion\n->")
            nbPlacesTRE = input("Saisissez le nombre de places PREMIUM de l avion\n->")
            nbPlacesECO = input("Saisissez le nombre de places ECONOMIQUE de l avion\n->")
 
            ajoutVol(numvol,compagnie,aeroportDep,dateDep,heureDep,aeroportArr,dateArr, heurArr,immat,nbPlacesAFF,nbPlacesTRE,nbPlacesECO)

        #===============================================================================================
        # Pour identifier un vol, il faut connaitre numvol, aeroportDep,dateDep,heureDep,aeroportArr
        #===============================================================================================
        if menu_choix == 2 :
            numvol = input("Saisissez le numero du vol\n->")
            aeroportDep = input("Saisissez l aeroport de depart du vol\n->")
            dateDep = input("Saisissez le jour du vol\n->")
            heureDep = input("Saisissez l heure prevue de depart  du vol\n->")
            aeroportArr = input("Saisissez l aeroport d arrivee du vol\n->")
            heureDepNew = input("Saisissez la nouvelle heure de depart du vol\n->")
            modificationVol(numvol,aeroportDep,dateDep,heureDep,aeroportArr,heureDepNew)

        if menu_choix == 3 :
            numvol = input("Saisissez le numero du vol\n->")
            aeroportDep = input("Saisissez l aeroport de depart du vol\n->")
            dateDep = input("Saisissez le jour du vol\n->")
            heureDep = input("Saisissez l heure prevue de depart  du vol\n->")
            aeroportArr = input("Saisissez l aeroport d arrivee du vol\n->")            
            suppressionVol(numvol,aeroportDep,dateDep,heureDep,aeroportArr)

        if menu_choix == 4 :
            affichageVols() 
            


        if menu_choix == 5 :
            return 
