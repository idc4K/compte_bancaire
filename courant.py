# coding : utf-8

import datetime

def solde():
    fichier = open("data_courant.txt","r")
    lire = fichier.read()
    print("Votre solde est de {} francs".format(lire))
    fichier.close()


def transactions () :
    """ Cette fonction affiche l'historique de vos transactions """
    fichier = open("transactions_courant.txt","r")
    lire = fichier.read()
    print (lire)
    fichier.close()

def depot () :
    """C'est une fonction qui vous permet de déposer de l'argent sur votre compte
    puis enregistre le montant et la date de votre transaction """
    #on ouvre le fichier data_courant, qui contient la somme actuelle contenue dans le compte
    #on recupère le montant dans mtnt_initial puis on referme le fichier
    fichier = open("data_courant.txt","r")
    montant_texte = fichier.read()
    montant_initial = int(montant_texte)
    fichier.close()
    #on lui demande de saisir le montant du depot
    x = 1
    while x == 1 :
        print("Entrez le montant de votre dépôt")
        montant_depose = input()
        try:
            montant_depose = int(montant_depose)
        except ValueError:
            print("Entrez un montant svp")
            x = 1
        if montant_depose <= 0 :
            print("Entrez un montant supérieur à 0 svp")
            x = 1
        else :
            x = 2
    nouveau_montant = montant_initial + montant_depose
    print("Dépot effectué avec succès.")
    print("Votre nouveau solde est de {} francs".format(nouveau_montant))
    
    #enregistrement du nouveau montant dans le compte
    fichier_2 = open("data_courant.txt","w")
    nouveau_montant_texte = str(nouveau_montant)
    fichier_2.write(nouveau_montant_texte)
    fichier_2.close()

    #enregistrement de la transaction avec la date
    auj = datetime.datetime.now()
    aa = auj.strftime('%Y-%m-%d %H:%M:%S')
    file = open("transactions_courant.txt", "a")
    file.write("\n {} Vous avez fait un dépôt de {} francs.".format(aa,montant_depose))
    file.close()
     

def retrait ():
    """C'est une fonction qui vous permet de retirer de l'argent sur votre compte
    puis enregistre le montant et la date de votre transaction """
    #on ouvre le fichier data_courant, qui contient la somme actuelle contenue dans le compte
    #on recupère le montant dans mtnt_initial puis on referme le fichier
    fichier = open("data_courant.txt","r")
    montant_texte = fichier.read()
    montant_initial = int(montant_texte)
    fichier.close()
    #on lui demande de saisir le montant du retrait
    x = 1
    while x == 1 :
        print("Entrez le montant de votre retrait")
        montant_retire = input()
        try:
            montant_retire = int(montant_retire)
        except ValueError:
            print("Entrez un montant svp")
            x = 1
        if montant_retire <= 0 :
            print("Entrez un montant supérieur à 0 svp")
            x = 1
        elif montant_retire > montant_initial :
            print("Vous ne pouvez pas retirer plus que ce que vous avez dans votre compte")
            x = 1
        else :
            x = 2
    nouveau_montant = montant_initial - montant_retire
    print("Retrait effectué avec succès.")
    print("Votre nouveau solde est de {} francs".format(nouveau_montant))
    
    #enregistrement du nouveau montant dans le compte
    fichier_2 = open("data_courant.txt","w")
    nouveau_montant_texte = str(nouveau_montant)
    fichier_2.write(nouveau_montant_texte)
    fichier_2.close()

    #enregistrement de la transaction avec la date
    auj = datetime.datetime.now()
    aa = auj.strftime('%Y-%m-%d %H:%M:%S')
    file = open("transactions_courant.txt", "a")
    file.write("\n {} Vous avez fait un retrait de {} francs.".format(aa,montant_retire))
    file.close()