import numpy as np
import jeu


class Grille():
    def __init__(self):
        self.grille = np.array([])

    def initialiser(self):

        x,y = 0,0

        while (x==0)&(y==0):
            print("Choisissez une difficultée : 'facile', 'moyen', 'difficile', 'personnalisee' : ")
            niveau = input()

            if niveau =='personnalisee':
                print('Entrer les dimensions de la grille.')
                x = int(input('Nombre de lignes : '))
                y = int(input('Nombre de colonnes : '))
            if niveau =='difficile':
                x,y = 24,24
            if niveau =='moyen':
                x,y = 16,16
            if niveau =='facile':
                x,y = 8,8
            else:
                print('/!\ Veuillez entrer une des propositions cités ci-dessus.')
        # self.grille = np.ones((x,y))
        self.grille = np.array([['?' for _ in range(x)] for _ in range(y)])
        return self.grille
