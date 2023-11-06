import numpy as np
import random
import jeu
import case as c
import Chiffre as ch
import Bombe as b
import Vide as v

class Grille():
    def __init__(self):
        self.grille = np.array([])
        self.mines = []
        self.taille_x = 0
        self.taille_y = 0
        self.nb_mines = 0
        self.densite_mines = 0.175
        

    def initialiser(self):

        while (self.taille_x==0)&(self.taille_y==0):
            print("Choisissez une difficultée : 'facile', 'moyen', 'difficile', 'personnalisee' : ")
            niveau = input()

            if niveau =='personnalisee':
                print('Entrer les dimensions de la grille.')
                self.taille_x = int(input('Nombre de lignes : '))
                self.taille_y = int(input('Nombre de colonnes : '))
                self.nb_mines = int(self.taille_x*self.taille_y*self.densite_mines)
            if niveau =='difficile':
                self.taille_x,self.taille_y = 24,24
                self.nb_mines = 99
            if niveau =='moyen':
                self.taille_x,self.taille_y = 16,16
                self.nb_mines = 40
            if niveau =='facile':
                self.taille_x,self.taille_y = 8,8
                self.nb_mines = 10
            else:
                print('/!\ Veuillez entrer une des propositions cités ci-dessus.')
        # self.grille = np.ones((x,y))
        self.grille = np.array([[c.Case() for _ in range(self.taille_x)] for _ in range(self.taille_y)])

        # On attribue à n case le nombre de mines de la partie

        n = self.nb_mines//2  
        indices_x = random.sample(range(self.taille_x), n)
        indices_y = random.sample(range(self.taille_y), n)
        # print('Indice x : ',indices_x)
        # print('Indice y : ',indices_y)
        
        for i in range(n):
            self.mines.append([indices_x[i],indices_y[i]])
            # Changement en type : Bombe
            self.grille[indices_x[i]][indices_y[i]] = b.Bombe()
            self.attribution_mine(self.grille[indices_x[i]][indices_y[i]])

            # Création des cases avec les chiffres
            
            coordonnees, fenetre = self.proche_voisins(indices_x[i],indices_y[i])[0], self.proche_voisins(indices_x[i],indices_y[i])[1]
            k=0
            for voisin in fenetre:
                # print(coordonnees)
                if isinstance(voisin, b.Bombe):
                    pass
                else:
                    # print(coordonnees[k][0],coordonnees[k][1])
                    self.grille[coordonnees[k][0],coordonnees[k][1]] = ch.Chiffre()
                    self.attribution_chiffre(self.grille[coordonnees[k][0],coordonnees[k][1]])
                k+=1

        for i in range(self.taille_x):
            for j in range(self.taille_y):
                if isinstance(self.grille[i][j], b.Bombe) or isinstance(self.grille[i][j], ch.Chiffre):
                    pass
                else:
                    self.grille[i,j] = v.Vide()




        # Création des cases avec les chiffres

        # for i in range(self.taille_x):
        #     for j in range(self.taille_y):
        #         if isinstance(self.grille[indices_x[i]][indices_y[i]], b.Bombe):
        #             fenetre = self.proche_voisins(self,indices_x[i],indices_y[i])
        #             for voisin in fenetre:

        #                 if isinstance(voisin, b.Bombe):
        #                     pass
        #                 else:
        #                     self.grille[voisin[0],voisin[1]] = ch.Chiffre()
        #                     self.attribution_chiffre(self.grille[voisin[0],voisin[1]])
        #             print("L'objet est une instance de la classe Bombe.")
        #         else:
        #             print("L'objet n'est pas une instance de la classe Bombe.")

        return self.grille


    def attribution_mine(self,case):
        case.ajoute_mine()

    def attribution_chiffre(self,case_chiffre):
        case_chiffre.ajouter_chiffre()

    def decouvrir_case(self,case):
        case.decouvre_case()

    def marquer_case(self,case):
        case.marque_case() 

    def demarquer_case(self,case):
        case.demarque_case()

    def proche_voisins(self,x,y):

        coordonnees = [(x-1, y-1), (x, y-1), (x+1, y-1),
                   (x-1, y),             (x+1, y),
                   (x-1, y+1), (x, y+1), (x+1, y+1)]
        
        fenetre = []
        coord2 = []
        for coord in coordonnees:
            x, y = coord
            if x >= 0 and y >= 0 and x < self.taille_x and y < self.taille_y:
                coord2.append((x,y))
                # Vérifiez que les coordonnées sont valides avant d'ajouter l'élément à la fenêtre
                fenetre.append(self.grille[y,x])

        return coord2,fenetre
    
    def afficher_grille(self,grille):
        for ligne in grille:
            ligne_affichee = []
            for elem in ligne:
                if elem.est_decouvert:
                    ligne_affichee.append(str(elem.valeur))
                else:
                    ligne_affichee.append('?')
            print(' '.join(ligne_affichee))