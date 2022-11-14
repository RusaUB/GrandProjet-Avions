#--*-- coding:utf-8 --*--

from lib_commun import ouverture_fichier_txt, ecriture_fichier_txt 


def gestionReservations() :
    """
    Cette fonction a pour objectif
    IN :  numvol, nomcompagnie ,aeroportDep,dateDep,heureDep, aeroportArr,dateArr, heureArr,immatavion, nbplacesAffR, nbplacesPremR, nbplacesEcoR
    OUT :
    """

    def ajoutReservation(*donneesResa) :
        """
        Cette fonction a pour objectif
        numresa,numvol,numclient, dateDep,heureDep, dateResa,heureResa, placeAff, placePrem, placeEco
          0       1       2          3       4          5        6         7          8          9        
        IN :
        OUT :
        """
        nomfichier = "reservations.txt"
        fichierVols = "vols.txt"
        fichierPassagers = "passagers.txt"
        fichierAvions = "avions.txt"


        L_resas = ouverture_fichier_txt(nomfichier)
        print("L_resas = ",L_resas)
        L_vols = ouverture_fichier_txt(fichierVols)
        L_passagers = ouverture_fichier_txt(fichierPassagers)
        L_avions = ouverture_fichier_txt(fichierAvions)

        existe_vol = False  # indicateur d'existence de l aeroport de depart dans le fichier aeroports.txt
        existe_passager = False  # indicateur d'existence de l aeroport d arrivee dans le fichier aeroports.txt        

        placeAFFT = 0  # nombre de places Affaire theoriques presentent dans l'avion. Servira pour verifier s il reste une place disponible
        placePREMT = 0  # nombre de places Premium theoriques presentent dans l'avion. Servira pour verifier s il reste une place disponible
        placeECOT = 0  # nombre de places Eco theoriques presentent dans l'avion. Servira pour verifier s il reste une place disponible

        placeAFFR = 0  # nombre de places Affaire reservees dans l'avion. Servira pour verifier s il reste une place disponible
        placePREMR = 0  # nombre de places Premium reservees dans l'avion. Servira pour verifier s il reste une place disponible
        placeECOR = 0  # nombre de places Eco reservees dans l'avion. Servira pour verifier s il reste une place disponible

        resaAFF = False # indicateur de verification de demande de place AFF
        resaPREM = False # indicateur de verification de demande de place PREM
        resaECO = False # indicateur de verification de demande de place ECO

        indice_vol = 0  # indice permettant de sauvegarder le rang du vol dans le fichier avant reecriture
        # donneesResa = ('2', 'AF-22', '2', '2019-08-10', '08:00:00', '2019-08-07', '12:00:00', '0', '0', '1')

        # Verification si la reservation n existe pas deja
        for w in range(len(L_resas)) :
            if L_resas[w][0] == donneesResa[0] :
                print("La reservation existe déjà, l'opération ne peut se poursuivre")
                return

        # Verification si le vol existe bien
        for i in range(len(L_vols)) :
            if L_vols[i][0] == donneesResa[1] and L_vols[i][3] == donneesResa[3] and L_vols[i][4] == donneesResa[4] :
                indice_vol = i

                existe_vol = True
                avion = L_vols[i][8]
                placeAFFR = int(L_vols[i][9])
                placePREMR = int(L_vols[i][10])
                L_vols[i][11] = L_vols[i][11][0:-1] # suppression de \n
                print("L_vols[i][11] =",L_vols[i][11])
                placeECOR = int(L_vols[i][11]) 
                print("placeECOR =",placeECOR)
                print("Le vol existe, l'opération peut se poursuivre")

        print("Le vol = ",L_vols[indice_vol])

        print("placeAFFR = ",placeAFFR)
        print("type_placeAFFR = ",type(placeAFFR))
        print("placePREMR = ",placePREMR)
        print("type_placePREMR = ",type(placePREMR))
        print("placeECOR = ",placeECOR)
        print("type_placeECOR = ",type(placeECOR))

        print("donneesResa =",donneesResa)


        # Verification si le passager existe bien
        for passager in L_passagers :
            if passager[0] == donneesResa[2] :
                existe_passager = True
                print("Le passager existe, l'opération peut se poursuivre")

        # donneesResa = ('2', 'AF-22', '2', '2019-08-10', '08:00:00', '2019-08-07', '12:00:00', '0', '0', '1')
        placeAff = int(donneesResa[7])
        placePrem = int(donneesResa[8])
        placeEco = int(donneesResa[9])



        # Verification que la demande ne concerne qu une seule place (soit 1 placeAff ou 1 placePrem ou 1 placeEco pour le vol) dans la reservation
        if placeAff == 0 :
            if placePrem == 0 :
                if placeEco == 0 :
                    print("Vous n avez pas demande de place\n L operation ne peut se poursuivre")
                    return
                elif placeEco == 1 :
                    print("Vous avez demande 1 place ECO\n L operation peut se poursuivre")
                    resaECO = True
                else :
                    print("Vous avez demade plus d une place ECO\n L operation ne peut se poursuivre")
                    return

            if placePrem == 1 :
                if placeEco > 0 :
                    print("Vous avez deja demande 1 place PREM.\n Vous ne pouvez pas demande 1 place ECO\n L operation ne peut se poursuivre")
                    return
                    
                else :
                    print("Vous avez demande 1 place PREM\n L operation peut se poursuivre")
                    resaPREM = True

        elif placeAff == 1 :
            if placePrem == 0  and placeEco == 0 :
                print("Vous avez demande 1 place AFF\n L operation ne peut se poursuivre")
                resaAFF = True
            else :
                print("Vous avez deja demande 1 place AFF.\n Vous ne pouvez pas demande 1 autre place\n L operation ne peut se poursuivre")
                return
        print("resaAFF = ",resaAFF)
        print("resaPREM = ",resaPREM)
        print("resaECO = ",resaECO)

        # RESERVATION ====================================================================================
        #numresa,numvol,numclient, dateDep,heureDep, dateResa,heureResa, placeAff, placePrem, placeEco
        #   0       1       2          3       4          5        6         7          8          9    
        #===============================================================================================

        # VOL ====================================================================================================================================
        #numvol, nomcompagnie ,aeroportDep,dateDep,heureDep, aeroportArr,dateArr, heureArr,immatavion, nbplacesAffR, nbplacesPremR, nbplacesEcoR
        #   0         1             2         3        4          5         6        7         8            9              10           11
        #=======================================================================================================================================

        # Verification de la disponibilite de la place dans le vol
        # recherche de l avion effectuant le vol et recuperation des places deja reservees sur le vol par categories
        #for i in range(len(L_vols)) :
        #    if L_vols[i][0] == donneesResa[1] and L_vols[i][3] == donneesResa[3] and L_vols[i][4] == donneesResa[4] :
        #        avion = L_vols[i][8]
        #        placeAFFR = L_vols[i][9]
        #        placePREMR = L_vols[i][10]
        #        placeECOR = L_vols[i][11] 
                
        # recherche de l avion dans le fichier avions.txt pour recuperer les places theoriques par categories
        for j in range(len(L_avions)) :  # on utilise l indice j pour conserver l indice i qui donne le rang du vol dans vols.txt 
            if L_avions[j][0] == avion :
                placeAFFT = int(L_avions[j][4])
                placePREMT = int(L_avions[j][5])
                placeECOT = int(L_avions[j][6]) 

        print("placeAFFT = ",placeAFFT)
        print("placePREMT = ",placePREMT)
        print("placeECOT = ",placeECOT)


        placeAFFOK = False  # indicateur de place Affaire validee
        placePREMOK = False  # indicateur de place Affaire validee
        placeECOOK = False  # indicateur de place Affaire validee

        # Prise en compte de la demande de reservation d une place pour le vol
        if resaAFF == True :
            if placeAFFT - placeAFFR > 0 :
                placeAFFOK = True
            else :
                print("Il n y a plus de place AFFAIRE sur ce vol.\n L operation ne peut se poursuivre")

        if resaPREM == True :
            if placePREMT - placePREMR > 0 :
                placePREMOK = True
            else :
                print("Il n y a plus de place PREMIUM sur ce vol.\n L operation ne peut se poursuivre")

        if resaECO == True :
            if placeECOT - placeECOR > 0 :
                placeECOOK = True
            else :
                print("Il n y a plus de place ECONOMIQUE sur ce vol.\n L operation ne peut se poursuivre")

        print("placeAFFOK = ",placeAFFOK)
        print("placePREMOK = ",placePREMOK)
        print("placeECOOK = ",placeECOOK)
        
        

        # Ajout reservation
        print("J arrive dans la condition complexe")
        if existe_vol == True and existe_passager == True and (placeAFFOK == True or placePREMOK == True or  placeECOOK == True ) == True :
            new_resa = []

            for k in range(len(donneesResa)) :
                new_resa.append(donneesResa[k])

            # Ajout de \n de fin ligne
            new_resa[-1] = new_resa[-1] + "\n"
        
            L_resas.append(new_resa)
        
            ecriture_fichier_txt(L_resas, nomfichier)


        # VOL ====================================================================================================================================
        #numvol, nomcompagnie ,aeroportDep,dateDep,heureDep, aeroportArr,dateArr, heureArr,immatavion, nbplacesAffR, nbplacesPremR, nbplacesEcoR
        #   0         1             2         3        4          5         6        7         8            9              10           11
        #=======================================================================================================================================


            #print("L_vols[i][11] = ",L_vols[i][11])
            # actualisation du nombre de place restantes sur le vol pour la categorie
            if placeAFFOK == True :
                placeAFFR = placeAFFR + 1
                print("placeAFFR_ecr = ",placeAFFR)
                L_vols[i][9] = str(placeAFFR)
            
            if placePREMOK == True :
                placePREMR = placePREMR + 1
                print("placePREMR_ecr = ",placePREMR)
                L_vols[i][10] = str(placePREMR)

            if placeECOOK == True :
                placeECOR = placeECOR + 1
                print("placeECOR_ecr = ",placeECOR)
                print("type placeECOR_ecr = ",type(placeECOR))
                L_vols[indice_vol][11] = str(placeECOR) + "\n"
            print("L_vols[indice] =",L_vols[indice_vol])

            ecriture_fichier_txt(L_vols, fichierVols)

        else :
            print("Le vol ou le passager n'existent pas\n L operation ne peut se poursuivre")
            return





    def suppressionReservation(*donneesSupp) :
        """
        Cette fonction a pour objectif
        numresa,numvol,numclient, dateDep,heureDep, dateResa,heureResa, placeAff, placePrem, placeEco
          0       1       2          3       4          5        6         7          8          9        
        IN :  numresa,numclient,numvol
        OUT :
        """
        # Recuperation des donnees
        nomfichier = "reservations.txt"
        L_resas = ouverture_fichier_txt(nomfichier)

        existe_resa = False  # indicateur d'existence du vol dans le fichier vols.txt
        indice_resa = 0  # rang de la resa à supprimer dans la liste L_resas

        # Verification de presence de la resa a supprimer
        for i in range(len(L_resas)) :
            if L_resas[i][0] == donneesSupp[0] :
                existe_resa = True
                indice_resa = i

        # suppression de la resa dans la liste L_resas
        if existe_resa == False :
            print("La reservation n existe pas.\nLe processus ne peut continuer")
            return
        else :
            L_resas.pop(indice_resa)

        # ecriture de la liste actualisee dans le fichier reservations.txt
        ecriture_fichier_txt(L_resas, nomfichier) 




    def affichageReservations() :
        """
        Cette procédure a pour objectif d'afficher l'ensemble des informations administratives des reservations.
        Soit :                                                                               numresa,numvol,numclient, dateDep,heureDep, dateResa,heureResa, placeAff, placePrem, placeEco
        IN : aucun paramètre en entrée
        OUT : aucun retour
        """
        ##################################################
        #ouverture et recuperation du contenu du fichier
        ##################################################
        nomfichier = "reservations.txt"
        L_resas = ouverture_fichier_txt(nomfichier)

        for i in range(0,len(L_resas)) :
            L_resas[i][-1] = (L_resas[i][-1][0:-1]) # on enleve le \n du numéro de tph

        print("***************************************************************************************************************")
        print("*                                     Descriptif des reservations                                             *")
        print("***************************************************************************************************************")
        print("* NumResa *   NumVol   * NumClient *   Date DEP   *  Heure DEP *   Date Resa  * Heure Resa * AFF * PRE * ECO  *")
        print("***************************************************************************************************************")

        for i in range(0,len(L_resas)) :
            print("* {:^7} * {:^10} * {:^9} * {:<12} * {:<10} * {:<12} * {:<10} * {:>3} * {:>3} * {:>3}  *" . format(L_resas[i][0], L_resas[i][1], L_resas[i][2], L_resas[i][3], L_resas[i][4], L_resas[i][5], L_resas[i][6], L_resas[i][7], L_resas[i][8], L_resas[i][9]))

        print("***************************************************************************************************************\n")
 


    ##################################################
    #
    ##################################################
    while True:
        menu_choix = int(input("Rentrez votre choix ( valeur entre 1-5): \n 1- Ajout reservation \n 2- Suppression reservation\n 3- Affichage reservation\n 4- Sortie\n\n Reponse :\n"))

        if menu_choix == 1 :
            #numvol, nomcompagnie ,aeroportDep,dateDep,heureDep, aeroportArr,dateArr, heureArr,immatavion, nbplacesAffR, nbplacesPremR, nbplacesEcoR
            numresa = input("Saisissez le numero resa\n->")
            numvol = input("Saisissez le numero du vol\n->")
            numclient = input("Saisissez le numero du client\n->")
            dateDep = input("Saisissez la date du vol\n->")
            heureDep = input("Saisissez l heure du vol\n->")
            dateResa = input("Saisissez la date de resa du vol\n->")
            heureResa = input("Saisissez l heure de resa du vol\n->")
            PlacesAFF = input("Saisissez place AFFAIRE\n->")
            PlacesTRE = input("Saisissez place PREMIUM\n->")
            PlacesECO = input("Saisissez place ECONOMIQU\n->")
            ajoutReservation(numresa,numvol,numclient,dateDep,heureDep,dateResa,heureResa,PlacesAFF,PlacesTRE,PlacesECO)

        #===============================================================================================
        # Pour identifier un vol, il faut connaitre numvol, aeroportDep,dateDep,heureDep,aeroportArr
        #===============================================================================================


        if menu_choix == 2 :
            numresa = input("Saisissez le numero de réservation\n->")
            numclient = input("Saisissez le numero de client\n->")
            numvol = input("Saisissez le numero du vol\n->")
            suppressionReservation(numresa,numclient,numvol)

        if menu_choix == 3 :
            affichageReservations() 

        if menu_choix == 4 :
            return 
