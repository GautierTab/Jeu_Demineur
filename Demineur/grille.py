import numpy as np
import jeu
import case as c

class Grille():
    def __init__(self):
        self.grille = np.array([])
        self.mines = []
        self.taille_x = 0
        self.taille_y = 0

    def initialiser(self):

        while (self.taille_x==0)&(self.taille_y==0):
            print("Choisissez une difficultée : 'facile', 'moyen', 'difficile', 'personnalisee' : ")
            niveau = input()

            if niveau =='personnalisee':
                print('Entrer les dimensions de la grille.')
                self.taille_x = int(input('Nombre de lignes : '))
                self.taille_y = int(input('Nombre de colonnes : '))
            if niveau =='difficile':
                self.taille_x,self.taille_y = 24,24
            if niveau =='moyen':
                self.taille_x,self.taille_y = 16,16
            if niveau =='facile':
                self.taille_x,self.taille_y = 8,8
            else:
                print('/!\ Veuillez entrer une des propositions cités ci-dessus.')
        # self.grille = np.ones((x,y))
        self.grille = np.array([[c.Case() for _ in range(self.taille_x)] for _ in range(self.taille_y)])
        return self.grille

    def decouvrir_case(self,x,y):
        case = self.grille[x,y]
        case.est_decouvert = True

    def marquer_case(self,x,y):
        case = self.grille[x,y]
        case.est_marque = True

    def demarquer_case(self,x,y):
        case = self.grille[x,y]
        case.est_marquee = False