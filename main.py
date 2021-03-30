# coding : utf-8

import sys
import datetime
import courant
import epargne


def depart( ) :
    commencer()
def commencer( ) :
    print("Bonjour M . Bienvenue à la YB BANK, la banque du peuple.")
    print ("Choisissez un compte")
    print("     1 - Compte Courant")
    print("     2 - Compte Epargne")
    print("     3 - Quitter")
    choix = input()
    choix_compte (choix)

def choix_compte(choix):
    if choix == "1" :
        operation_courant ()
    elif choix == "2" :
        operation_epargne ()
    elif choix == "3" :
        sys.exit()
    else :
        print("action invalide")
        commencer()

def operation_courant ():
    print("Que voulez-vous faire sur votre compte courant ?")
    print("     1- Consulter votre solde")
    print("     2- Afficher la liste de vos transactions")
    print("     3- Faire un dépôt")
    print("     4- Faire un retrait")
    print("     5- Retour")
    choix = input()

    if choix == "1" :
        courant.solde()
        commencer()
    elif choix == "2" :
        courant.transactions()
        commencer()
    elif choix == "3" :
        courant.depot()
        commencer()
    elif choix == "4" :
        courant.retrait()
        commencer()
    elif choix == "5" :
        print("retour au menu principal...")
        commencer()
    else :
        print("action invalide")
        commencer()

def operation_epargne ():
    print("Que voulez-vous faire sur votre compte épargne ?")
    print("     1- Consulter votre solde")
    print("     2- Afficher la liste de vos transactions")
    print("     3- Faire un dépôt")
    print("     4- Faire un retrait")
    print("     5- Retour")
    choix = input()

    if choix == "1" :
        epargne.solde()
        commencer()
    elif choix == "2" :
        epargne.transactions()
        commencer()
    elif choix == "3" :
        epargne.depot()
        commencer()
    elif choix == "4" :
        epargne.retrait()
        commencer()
    elif choix == "5" :
        print("retour au menu principal...")
        commencer()
    else :
        print("action invalide")
        commencer()

#----------------------- Execution du programme ---------------------------

depart()