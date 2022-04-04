"""
Ce programme simule un jeu, de base écrit en C par Jerry Peeren
Lien du code C : https://forums.commentcamarche.net/forum/affich-8228608-c-un-petit-jeu-du-pendu
Réécrit en python par =[ Seydina Oumar Cissé / M1 RTSEC ]

Ce jeu est basé sur un concept consistant à deviner les bonnes lettres pour former le bon mot avant la fin des tentatives(chances).
"""

import random
from dico import dico # importer la liste de plusieurs mots

def presentation():
    """Ci-après, un affichage juste pour le fun"""
    joueur =input("Bonjour, quel est votre nom ? >>> ")

    print("*****************************")
    print("*      Jeu de pendu         *")
    print(f"*   Bienvevue {joueur}\U0001F637      *")
    print("*                           *")
    print("*****************************")
    print()

def recup_mot():
    """
    Là on définit une fonction qui renvoie un mot aléatoire d'une liste de plusieurs mots
    """
    word = random.choice(dico)
    return word.upper()


def jouer(word):
    """
    fonction déclenchant une partie du jeu :
     * Affichage du mot à deviner
     * Demander une lettre au joueur
     * Mise à jour de l'affichage
     On répète cela jusqu'a ce que le mot complet soit trouvé / le nombre de tentative soit terminé
    """
    affichage = "_" * len(word)
    deviné = False
    lettre_deviné = []
    mot_deviné = []
    tentatives = 10
    print("Essayez de deviner le mot caché !")
    print(affichage)
    print("\n")
    while not deviné and tentatives > 0:
        joueur = input("Proposez une lettre: ").upper()
        if len(joueur) == 1 and joueur.isalpha():
            if joueur in lettre_deviné:
                print("Vous avez deja deviné la lettre", joueur)
            elif joueur not in word:
                print(f"Le caractère {joueur} n'est pas dans le mot.")
                tentatives -= 1
                lettre_deviné.append(joueur)
            else:
                print(f"Bien joué! {joueur} est dans le mot!")
                lettre_deviné.append(joueur)
                liste_mot = list(affichage)
                indices = [i for i, letter in enumerate(word) if letter == joueur]
                for index in indices:
                    liste_mot[index] = joueur
                affichage = "".join(liste_mot)
                if "_" not in affichage:
                    deviné = True
        elif len(joueur) == len(word) and joueur.isalpha():
            if joueur in mot_deviné:
                print(f"Vous avez deja deviné le mot {joueur}")
            elif joueur != word:
                print(f"{joueur} n'est pas dans le mot.")
                """ Si la lettre proposé n'est pas dans le mot {tentatives} dimunie de 1 """
                tentatives -= 1
                mot_deviné.append(joueur)
            else:
                deviné = True
                affichage = word
        else:
            print("Mauvaise proposition.")
        print(f"Il vous reste {tentatives} tentatives")
        print("\n")
        print(affichage)
        print("\n")
    if deviné:
        print(f"Bravo, vous avez deviné {word}! Vous avez gagné!")
    else:
        print(f"Désolé, vous avez perdu. Le mot était {word}. Une prochaine fois!")


def main():
    """
    fonction principale du jeu, servant de point d'entrée au programme, elle permet aussi d'effectuer plusieurs manches
    """
    presentation()
    word = recup_mot()
    jouer(word)
    while input("Voulez-vouz rejouer ? (O/N) ").upper() == "O":
        word = recup_mot()
        jouer(word)


if __name__ == "__main__":
    main()