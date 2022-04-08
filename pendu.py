"""
Ce programme simule un jeu, de base écrit en C par Jerry Peeren
Lien du code C : https://forums.commentcamarche.net/forum/affich-8228608-c-un-petit-jeu-du-pendu
Réécrit en python par =[ Seydina Oumar Cissé / M1 RTSEC ]

Ce jeu est basé sur un concept consistant à deviner les bonnes lettres pour former le bon mot avant la fin des tentatives(chances).
"""

import random
from dico import dico


def welcome():
    
    joueur = input("""
                ========================
                > Quel est votre nom:  <
                """).capitalize()
    
    if joueur.isalpha() == True:
        print("*****************************")
        print("*      Jeu de pendu         *")
        print(f"*   Bienvevue {joueur}\U0001F637      *")
        print("*                           *")
        print("*****************************")
        print()
        
           
    else:
        print('Svp, utilisez des carractères !')
        joueur = input("Saisir un nom:  ")
        print('Bonjour !',joueur,'Bienvenue au jeu de pendu !')
        
def play_again():
    
    """ La fonction demande au joueur s'il souhaite rejouer ou non """
    reponse = input("Voulez vous rejouer à nouveau? oui/non. Tapez 'O' pour Oui or 'N' pour Non: ").lower()

    if reponse == "o" or reponse == "O":
        jouer()
    else:
        print("A plutard !!")
        
def get_word():
    """
    Là on définit une fonction qui renvoie un mot aléatoire d'une liste de plusieurs mots
    """
    words = random.choice(dico)
    return words.lower()

def tirets(word):
    print("Le mot contient", len(word), "lettres.")
    print(len(word) * '_')

def statut(tentatives,word,status):
    if status == word:
        print("Great Job! Vous avez deviné le mot correctement!")
        devine = True
    elif tentatives == 0:
        print("Oupps! Vous avez perdu!")

def traitement(proposition,alphabet):
    if proposition not in alphabet:
        print("Verifiez votre saisi ")
    
def jouer():
    """
    fonction déclenchant une partie du jeu :
     * Affichage du mot à deviner
     * Demander une lettre au joueur
     * Mise à jour de l'affichage
     On répète cela jusqu'a ce que le mot complet soit trouvé / le nombre de tentative soit terminé
    """
    word = get_word()
    devine_lettre = []
    tentatives = 7
    devine = False
    alphabet = ("abcdefghijklmnopqrstuvwxyz")
    print()
    tirets(word)
    
    while devine == False and tentatives > 0:
        print("Vous avez " + str(tentatives) + " tentatives")
        proposition = input("Proposez une lettre svp >>> ").lower()
        if len(proposition) == 1:
            traitement(proposition,alphabet)
            if proposition in devine_lettre:
                print("Vous avez dèja saisi cette lettre! Essayez encore")
            elif proposition not in word:
                print("Desolé ! la lettre n'est pas dans le mot! ")
                devine_lettre.append(proposition)
                tentatives -=1
            elif proposition in word:
                print("Bien vu!")
                devine_lettre.append(proposition)
            else:
                print("Mauvais saisi! ")

        elif len(proposition) == len(word):
            if proposition == word:
                print("Bien joué! ")
                devine = True
            else:
                print("Désolé, ce n'etait pas le mot")
                tentatives -= 1
        else:
            print("La longueur du mot n'est pas le même.")
            tentatives -=1
        
        if devine == False:
            status=""
            for lettre in word:
                if lettre in devine_lettre:
                    status += lettre
                else:
                    status += "_"
            print(status)
        if status == word:
            print("Great Job! Vous avez deviné le mot correctement!")
            devine = True
        if tentatives == 0:
            print("Oupps! Vous avez perdu!")

    play_again()

def main():
    """
    fonction principale du jeu, servant de point d'entrée au programme, elle permet aussi d'effectuer plusieurs manches
    """
    welcome()
    jouer()

if __name__ =="__main__":
    main()