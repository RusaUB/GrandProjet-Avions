def ouverture_fichier_txt(nomfichier):
    """
    Cette fonction a pour objectif l'ouverture d'un fichier au format texte
    IN : le nom du fichier à traiter
    OUT : une liste de listes de chaines de caractères. Chaque sous-liste représente une enregistrement du fichier
          ex pour le  fichier compagnies.txt : nomcompagnie,pays,codeiata
    """
    ##################################################
    #ouverture et recuperation du contenu du fichier
    ##################################################
    fic_input = []

    try :
        zone_Echange = open(nomfichier, 'r')
    except :
        print("1-Problème d'ouverture de fichier en lecture")
        return

    # Boucle permettant de transformer la liste de chaines de caractères en
    # liste de listes de chaines de caractères
    for ligne in zone_Echange.readlines():
        pt_data = ligne.split(sep=',')
        #print(pt_data)
        fic_input.append(pt_data)

    zone_Echange.close()

    #print("fic_input = ",fic_input)

    return  fic_input


def ecriture_fichier_txt(contenu_fichier, nomFichier):
    """
    Cette fonction a pour objectif l'ouverture d'un fichier au format texte
    IN : le nom du fichier à traiter
    OUT : une liste de listes de chaines de caractères. Chaque sous-liste représente une enregistrement du fichier
          ex pour le  fichier compagnies.txt : nomcompagnie,pays,codeiata
    """
    ##################################################
    #ouverture et recuperation du contenu du fichier
    ##################################################
    fic_output = []
    #print(contenu_fichier)

    # Boucle permettant de transformer la liste de chaines de caractères en
    # liste de listes de chaines de caractères
    for sous_liste in contenu_fichier :
        pt_data = ",".join(sous_liste)
        fic_output.append(pt_data)

    try :
        zone_Echange = open(nomFichier, 'w')
        zone_Echange.writelines(fic_output)
        zone_Echange.close()
    except :
        print("2-Problème d'ouverture de fichier en ecriture")
        return
