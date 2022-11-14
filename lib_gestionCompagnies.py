#--*-- coding:utf-8 --*--


from lib_commun import ouverture_fichier_txt, ecriture_fichier_txt 


def gestionCompagnies():
    """
    Cette fonction a pour objectif
    IN :
    OUT :
    """

    def ajoutCompagnie(*donneesComp):
        """
        Cette fonction a pour objectif
        IN : importer le nom, le pays et le code IATA de la nouvelle compagnie
        OUT : ecrire les attributs de la nouvelle compagnie dans le fichier "compagnie.txt"
        """
        # Recuperation des donnees
        nom_fichier = "compagnies.txt"
        L_compagnies = ouverture_fichier_txt(nom_fichier)
        # Verification si la compagnie existe deja. Si elle existe -> arret du processus
        for i in L_compagnies:
            if i[0] == donneesComp[0]:
                print("La compagnie existe déjà")
                return
        
        print("La compagnie n'est pas dans la base de données")


        # Preparation de la nouvelle compagnie
        new_compagnie = []
        for elem in donneesComp:
            new_compagnie.append(elem)

        # Ajout de \n de fin ligne
        codeIATA = new_compagnie[2]
        new_compagnie[2] = str(str(codeIATA) + str("\n"))
        
        # Ajout dans la liste des compagnies 
        L_compagnies.append(new_compagnie)
        
        # Reecriture du fichier actualise
        ecriture_fichier_txt(L_compagnies,"compagnies.txt")

            

    def suppressionCompagnie(compagnie) :
        """
        Cette fonction a pour objectif
        
        IN : vérifier si la compagnie existe plusieurs fois
        OUT : sélectionner la compa
        """
        # Recuperation des donnees
        nomfichier = "compagnies.txt"
        fichierAvions = "avions.txt"
        fichierVols = "vols.txt"
        indice = 0  # indicateur donnant le rang ou la compagnie a ete trouvee
        existe_compagnie = False  # indicateur d'existence de la compagnie dans le fichier
        existe_avion = False  # indicateur d'existence de compagnie/avion  dans le fichier avions.txt
        existe_vol = False  # indicateur d'existence de compagnie/vol  dans le fichier vols.txt
        L_compagnies = ouverture_fichier_txt(nomfichier)
        L_avions = ouverture_fichier_txt(fichierAvions)
        L_vols = ouverture_fichier_txt(fichierVols)

        # Verification compagnie dans compagnies.txt
        for i in L_compagnies:
            if i[0] == compagnie:
                existe_compagnie = True
                break
        
        # Sortie si la compagnie n existe pas
        if existe_compagnie == False:
            print("La compagnie n'est pas dans la base de données")
            return
        
        # Verification compagnie/avion  dans le fichier avions.txt
        for i in L_avions:
            if i[1] == compagnie:
                existe_avion = True
                break

        # Verification compagnie/vol  dans le fichier vols.txt
        for i in L_vols:
            if i[1] == compagnie:
                existe_vol = True
                break

        # suppression de la compagnie 
        liste_compagnies_del = L_compagnies
        if existe_avion == False and existe_compagnie == True and existe_vol == False:
            for indice in liste_compagnies_del:
                if indice[0] == compagnie:
                    liste_compagnies_del.remove(indice)
                    print("La compagnie a été supprimée")
                

        # reecriture du fichier modifie
        ecriture_fichier_txt(liste_compagnies_del,"compagnies.txt")
    
    
    
   
    def affichageCompagnies() :
        """
        Cette procédure a pour objectif d'afficher l'ensemble des informations administratives des compagnies.
        Soit : nom de la compagnie, son code OACI,son aeroport_principal,le nom de son alliance,le nombre d'avions,
        le nombre de liaisons
        IN : aucun paramètre en entrée
        OUT : aucun retour
        """
        ##################################################
        #ouverture et recuperation du contenu du fichier
        ##################################################
        nomfichier = "compagnies.txt"
        L_compagnies = ouverture_fichier_txt(nomfichier)
        #print("\n\nL_compagnies = ",L_compagnies,"\n")

        for i in range(0,len(L_compagnies)) :
            L_compagnies[i][2] = (L_compagnies[i][2][0:-1]) # on enleve le \n du numéro de tph

        print("****************************************************************")
        print("*                 Descriptif compagnies aeriennes              *")
        print("****************************************************************")
        print("*          Compagnie         *          Pays          *  IATA  *")
        print("****************************************************************")

        for i in range(0,len(L_compagnies)) :
            print("*   {:<22}    *  {:<20}  * {:^5} *" . format(L_compagnies[i][0], L_compagnies[i][1], L_compagnies[i][2]))

        print("****************************************************************\n")

        ##################################################
        #
        ##################################################
    
    while True:
        menu_choix = int(input("Rentrez votre choix ( valeur entre 1-5): \n 1- Ajout compagnie \n 2- Modification compagnie\n 3- Suppression compagnie\n 4- Affichage compagnies\n 5- Sortie\n\n Reponse :\n"))
                                                                            
        if menu_choix == 1 :
            compagnie = input("Saisissez le nom de la compagnie\n->")
            pays = input("Saisissez le pays de la compagnie\n->")
            codeiata = input("Saisissez le code IATA de la compagnie\n->")
            ajoutCompagnie(compagnie,pays,codeiata)

        if menu_choix == 3 :
            compagnie = input("Saisissez le nom de la compagnie a supprimer\n->")
            suppressionCompagnie(compagnie) 

        if menu_choix == 4 :
            affichageCompagnies() 


        if menu_choix == 5 :
            return 
