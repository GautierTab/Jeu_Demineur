# Répertoire main.py
# Lancement central des commandes
import numpy as np
import grille as g

grille = g.Grille()
jeu = grille.initialiser()

for ligne in jeu:
    print('   '.join(map(str, ligne)))
