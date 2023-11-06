# Répertoire main.py
# Lancement central des commandes
import numpy as np

import grille as g
import jeu as j

grille = g.Grille()

jeu = grille.initialiser()
jeu = j.jeu()
jeu.lancement_jeu()


# for ligne in jeu:
#     for elem in ligne:
        
        # if isinstance(elem, b.Bombe):
        #     print("L'objet est une instance de la classe Bombe.")
        # else:
        #     print("L'objet n'est pas une instance de la classe Bombe.")
    # print('   '.join(map(str, ligne)))