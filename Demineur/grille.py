import numpy as np
import random
import time

import jeu as j
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
        self.densite_mines = 0.25
        self.debut = 0
        self.fin = 0
        self.nb_case_jouable = self.taille_x * self.taille_y - self.nb_mines
        
    def initialiser(self):
        """
        Cette fonction permet d'initialiser la grille de départ
        :return grille(Grille): renvoie la grille de jeu
        """
        self.debut = time.time()
        while (self.taille_x==0)&(self.taille_y==0):
            print("Choisissez une difficultée. 0 : facile, 1: moyen, 2 : difficile, 3 : personnalisé")
            niveau = input()

            if int(niveau) == 3:
                print('Entrer les dimensions de la grille.')
                self.taille_x = int(input('Nombre de lignes : '))
                self.taille_y = int(input('Nombre de colonnes : '))
                self.nb_mines = int(self.taille_x*self.taille_y*self.densite_mines)
            elif int(niveau) == 2:
                self.taille_x,self.taille_y = 24,24
                self.nb_mines = 99
            elif int(niveau) == 1:
                self.taille_x,self.taille_y = 16,16
                self.nb_mines = 40
            elif int(niveau) == 0:
                self.taille_x,self.taille_y = 8,8
                self.nb_mines = 10
            else:
                print('/!\ Veuillez entrer une des propositions cités ci-dessus.')

        # Initialisation de la grille
        self.grille = np.array([[c.Case() for _ in range(self.taille_x)] for _ in range(self.taille_y)])

        # Initialisation de la première case cliquée
        premier_x = int(input('Quelle ligne ? '))
        premier_y = int(input('Quelle colonne ? '))
        self.grille[premier_x,premier_y] = v.Vide()

        # On attribue à n case le nombre de mines de la partie
        n = self.nb_mines  

        indices_x = []
        indices_y = []

        # Tirer au hasard des coordonnées dans la grille
        while (len(indices_x)) < n:
            x = random.randint(0, self.taille_x-1)
            y = random.randint(0, self.taille_y-1)

            # Vérifier si les éléments tirés ne sont pas égaux à premier_x et premier_y
            if (x != premier_x) and (y != premier_y) and not ((premier_x - 1 <= x <= premier_x + 1) and (premier_y - 1 <= y <= premier_y + 1)):
       
                indices_x.append(x)
                indices_y.append(y)

        for i in range(len(indices_x)):
            self.mines.append([indices_x[i],indices_y[i]])
            # Changement en type : Bombe
            self.grille[indices_x[i]][indices_y[i]] = b.Bombe()
            self.attribution_mine(self.grille[indices_x[i]][indices_y[i]])

            # Création des cases avec les chiffres
            coordonnees, fenetre = self.proche_voisins(indices_x[i],indices_y[i])[0], self.proche_voisins(indices_x[i],indices_y[i])[1]
            k=0
            for voisin in fenetre:
                if isinstance(voisin, b.Bombe):
                    pass
                elif isinstance(voisin,ch.Chiffre):
                    self.attribution_chiffre(self.grille[coordonnees[k][0],coordonnees[k][1]])
                else:
                    self.grille[coordonnees[k][0],coordonnees[k][1]] = ch.Chiffre()
                    self.attribution_chiffre(self.grille[coordonnees[k][0],coordonnees[k][1]])
                k+=1

        # Attribution des cases vides
        for i in range(self.taille_x):
            for j in range(self.taille_y):
                if isinstance(self.grille[i][j], b.Bombe) or isinstance(self.grille[i][j], ch.Chiffre):
                    pass
                else:
                    self.grille[i,j] = v.Vide()

        # Clique sur la première case 
        self.clic_case(premier_x,premier_y)

        return self.grille
    


    def attribution_mine(self,case):
        """
        Cette fonction permet de basculer l'attribut self.contient_mine de case.py vers True
        :param case (Case) : Case de la grille
        """
        case.ajoute_mine()

    def attribution_chiffre(self,case_chiffre):
        """
        Cette fonction permet d'ajouter 1 à l'attribut self.valeur (dans Chiffre.py) 
        :param case (Case) : Case de la grille
        """
        case_chiffre.ajouter_chiffre()

    def decouvrir_case(self,case):
        """
        Cette fonction permet de basculer l'attribut découvert (dans Case.py) vers True.
        :param case (Case) : Case de la grille
        """
        case.decouvre_case()

    def marquer_case(self,case):
        """
        Cette fonction permet de marquer une case.
        :param case (Case) : Case de la grille
        """
        case.marque_case() 

    def demarquer_case(self,case):
        """
        Cette fonction permet de demarquer une case.
        :param case (Case) : Case de la grille
        """
        case.demarque_case()

    def case_decouverte(self,case):
        """
        Cette fonction permet de retourner True si la case demandée à déjà été découverte.
        :param case (Case) : Case de la grille
        :return: (bool) 
        """
        return case.est_decouvert

    def proche_voisins(self,x,y):
        """
        Cette fonction permet de retourner l'ensemble des 8 cases adjacentes à la case sélectionnée. 
        Les effets de bords sont pris en compte.

        :param x (int) : numéro de la ligne 
        :param y (int) : numéro de la colonne
        :return: coord2 (list) : position des cases adjacentes dans la grille
        :return: fenetre (list) : ensemble des cases (type case) ajdacentes
        """        

        coordonnees = [(x-1, y-1), (x-1, y), (x-1, y+1),
                   (x, y-1),             (x, y+1),
                   (x+1, y-1), (x+1, y), (x+1, y+1)]
        
        fenetre = []
        coord2 = []
        for coord in coordonnees:
            
            x, y = coord
            
            if x >= 0 and y >= 0 and x < self.taille_x and y < self.taille_y:
                # print(self.grille[x,y].est_decouvert)
                coord2.append((x,y))
                # Vérifiez que les coordonnées sont valides avant d'ajouter l'élément à la fenêtre
                fenetre.append(self.grille[x,y])

        return coord2,fenetre
    
    def __str__(self):
        """
        Cette fonction permet d'afficher la grille dans la console log
 
        :return: result (str) : chaine de caractère
        """
        result = ""
        for ligne in self.grille:
            ligne_affichee = []
            for elem in ligne:
                if elem.est_decouvert:
                    ligne_affichee.append(str(elem.valeur)+' ')
                # if elem.est_marquee:
                #     ligne_affichee.append('F ')
                else:
                    ligne_affichee.append('. ')
            result += ' '.join(ligne_affichee)
            result += '\n'
        return result

    def devoile_case_vide(self,x,y):
        """
        Cette fonction permet dévoiler toutes les cases voisines d'une case vide

        :param x (int) : numéro de la ligne 
        :param y (int) : numéro de la colonne
        :return: Rien
        """
        self.decouvrir_case(self.grille[x,y])
        coord, fenetre = self.proche_voisins(x,y)[0], self.proche_voisins(x,y)[1]
        k = 0
        for case in fenetre:
            if isinstance(case,v.Vide) and not(self.case_decouverte(case)):
                new_x,new_y = coord[k][0],coord[k][1]
                self.clic_case(new_x,new_y)
            self.decouvrir_case(case)
            k+=1

    def clic_case(self,x,y):
        """
        Cette fonction permet de modéliser l'action de cliquer sur une case, 
        et d'agir selon si c'est une case chiffre, vide ou une bombe.

        :param x (int) : numéro de la ligne 
        :param y (int) : numéro de la colonne
        :return: Rien, sauf si c'est une bombe ou que toutes les cases découvrables ont été découvertes, 
                alors renvoie True afin de stopper la boucle while dans jeu.py
        """
        case = self.grille[x,y]
        if case.est_decouvert:
            return

        # Cas d'une case bombe
        if isinstance(case, b.Bombe):
            self.decouvrir_case(case)
            self.jeu_fini = True
            self.fin = time.time()
            duree = self.fin - self.debut
            print('-------------------------------------------------')
            print('Vous avez perdu !')
            print('Votre score : ', duree)
            print('-------------------------------------------------')
            return True
        
        # Cas d'une case vide
        elif isinstance(case,v.Vide):
            self.nb_case_jouable -=1
            self.devoile_case_vide(x,y)

        # Cas d'une case chiffre    
        elif isinstance(case, ch.Chiffre):
            self.decouvrir_case(case)
            self.nb_case_jouable -=1
            
        # Cas où toutes les cases ont été découvertes
        if self.nb_case_jouable == 0:
            self.jeu_fini = True
            self.fin = time.time()
            duree = self.fin - self.debut
            print('-------------------------------------------------')
            print('Vous avez gagné !')
            print('Votre score : ',duree) 
            print('-------------------------------------------------')
            return True
        
        return
    
