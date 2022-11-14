#--*-- coding:utf-8 --*--


from lib_commun import ouverture_fichier_txt, ecriture_fichier_txt 


def gestionPassagers() :
    """
    Cette fonction a pour objectif
    IN :
    OUT :
    """
    
    def ajoutPassager(*donneesPass) :
        """
        Cette fonction a pour objectif
        IN : numclient,nomclient,prenomclient,numrue,nomrue,ville,pays
        OUT :
        """
        # Recuperation des donnees
        nomfichier = "passagers.txt"
        L_passagers = ouverture_fichier_txt(nomfichier)

        
        
        # Verification de l existence du passager




        # Preparation de la nouveau passager




        # Ajout de \n de fin ligne


        
        # Ajout dans la liste des cpassagers 


        
        # Reecriture du fichier actualise




    def suppressionPassager(idpassager) :
        """
        Cette fonction a pour objectif
        IN :
        OUT :
        """
        # Recuperation des donnees






        # Verification le passager existe dans le fichier passagers.txt







        # Verification reservation/passager  dans le fichier reservations.txt



                

        # suppression de l avion 






        # reecriture du fichier modifie



    def affichagePassagers() :
        """
        Cette procédure a pour objectif d'afficher l'ensemble des informations administratives des passagers.
        Soit : numpassager,nompassager,prenompassager,numrue,nomrue,nomville,pays
        IN : aucun paramètre en entrée
        OUT : aucun retour
        """
        ##################################################
        #ouverture et recuperation du contenu du fichier
        ##################################################
        nomfichier = "passagers.txt"
        L_passagers = ouverture_fichier_txt(nomfichier)

        for i in range(0,len(L_passagers)) :
            L_passagers[i][-1] = (L_passagers[i][-1][0:-1]) # on enleve le \n du pays

        print("**********************************************************************************************************************************************")
        print("*                                                              Descriptif avions                                                             *")
        print("**********************************************************************************************************************************************")
        print("*  id  *          Nom         *         Prenom       *  NumR  *             NomRue             *         Ville        *         Pays         *")
        print("**********************************************************************************************************************************************")

        for i in range(0,len(L_passagers)) :
            print("* {:<3}  * {:<20} * {:<20} * {:<6} * {:<30} * {:<20} * {:<20} *" . format(L_passagers[i][0], L_passagers[i][1], L_passagers[i][2], L_passagers[i][3], L_passagers[i][4], L_passagers[i][5], L_passagers[i][-1]))

        print("**********************************************************************************************************************************************\n")





    ##################################################
    #
    ##################################################
    while True:
        menu_choix = int(input("Rentrez votre choix ( valeur entre 1-5): \n 1- Ajout passager \n 2- Suppression passager\n 3- Affichage passagers\n 4- Sortie\n\n Reponse :\n"))
                                                                            
        if menu_choix == 1 :
            numclient = input("Saisissez le numero du client\n->")
            nomclient = input("Saisissez le nom du client\n->")
            prenomclient = input("Saisissez le prenom du client\n->")
            numrue = input("Saisissez le numero de la rue\n->")
            nomrue = input("Saisissez le nom de la rue\n->")
            ville = input("Saisissez le nom de la ville\n->")
            pays = input("Saisissez le nom du pays\n->")
            ajoutPassager(numclient,nomclient,prenomclient,numrue,nomrue,ville,pays)

        if menu_choix == 2 :
            numpassager = input("Saisissez le numero du passager\n->")
            suppressionPassager(numpassager)

        if menu_choix == 3 :
            affichagePassagers() 

        if menu_choix == 4 :
            return 