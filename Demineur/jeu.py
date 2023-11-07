import numpy as np
import grille as g
import Bombe as b
import Chiffre as ch
import Vide as v

class jeu():
    def __init__(self):
        self.jeu_fini = False
        self.grille = g.Grille()
        self.nb_case_jouable = self.grille.taille_x * self.grille.taille_y - self.grille.nb_mines

    def clic_case(self,x,y):

        case = self.grille.grille[x,y]
        if case.est_decouvert:
            return
   

        if isinstance(case, b.Bombe):
            case.decouvre_case()
            self.jeu_fini = True
            print('-------------------------------------------------')
            print('Vous avez perdu !')
            print('Votre score : ')
            print('-------------------------------------------------')
    
            # fin du jeu
        if isinstance(case,v.Vide):
            case.decouvre_case()
            self.nb_case_jouable -=1
            fenetre = self.grille.proche_voisins(x,y)[1]
            # Cas de la case en haut à gauche
            if x==0 and y==0:
                self.clic_case(x + 1, y)
                self.clic_case(x + 1, y + 1)
                self.clic_case(x, y + 1)
            # Cas de la case en bas à gauche
            if x==self.grille.taille_x and y==0:
                self.clic_case(x - 1, y)
                self.clic_case(x - 1, y + 1)
                self.clic_case(x, y + 1)
            # Cas de la case en haut à droite
            if x==0 and y==self.grille.taille_y:
                self.clic_case(x, y - 1)
                self.clic_case(x + 1, y - 1)
                self.clic_case(x + 1, y)
            # Cas de la case en bas à droite
            if x==self.grille.taille_x and y==self.grille.taille_y:
                self.clic_case(x, y - 1)
                self.clic_case(x - 1, y - 1)
                self.clic_case(x - 1, y)
            # Cas pour toutes les autres cases
            if x>0 and y>0 and x<self.grille.taille_x and y<self.grille.taille_y:
                self.clic_case(x - 1, y)
                self.clic_case(x + 1, y)
                self.clic_case(x, y - 1)
                self.clic_case(x, y + 1)
                self.clic_case(x - 1, y - 1)
                self.clic_case(x - 1, y + 1)
                self.clic_case(x + 1, y - 1)
                self.clic_case(x + 1, y + 1)
            
        if isinstance(case, ch.Chiffre):
            case.decouvre_case()
            self.nb_case_jouable -=1
            
        if self.nb_case_jouable == 0:
            self.jeu_fini = True
            print('-------------------------------------------------')
            print('Vous avez gagné !')
            print('Votre score : ') 
            print('-------------------------------------------------')        
        
        #self.affichage_grille(self.grille)

    def lancement_jeu(self):
        # while self.jeu_fini == False :
            # x = int(input('Quelle colonne ? '))
            # y = int(input('Quelle ligne ? '))
            # self.clic_case(x,y)

        self.grille.afficher_grille(self.grille.initialiser())
        while self.jeu_fini == False:
            x = int(input('Quelle colonne ? '))
            y = int(input('Quelle ligne ? '))
            if x<0 or y<0 or x>self.grille.taille_x or y>self.grille.taille_y:
                print('Veuillez indiquer un chiffre compris dans la grille')
            else:
                self.clic_case(x,y)
                self.grille.afficher_grille(self.grille.grille)
        return
    #def affichage_grille(self,grille):

