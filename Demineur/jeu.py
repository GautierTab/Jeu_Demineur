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

        case = self.grille[x,y]
        if case.est_decouvert:
            return
   

        if isinstance(case, b.Bombe):
            case.decouvre_case()
            self.jeu_fini = True
            print('Vous avez perdu !')
            print('Votre score : ')
    
            # fin du jeu
        if isinstance(case,v.Vide):
            fenetre = self.grille.proche_voisins(x,y)[1]
            self.clic_case(x - 1, y)
            self.clic_case(x + 1, y)
            self.clic_case(x, y - 1)
            self.clic_case(x, y + 1)
            self.clic_case(x - 1, y - 1)
            self.clic_case(x - 1, y + 1)
            self.clic_case(x + 1, y - 1)
            self.clic_case(x + 1, y + 1)
            case.decouvre_case()
            self.nb_case_jouable -=1
        
        if isinstance(case, ch.Chiffre):
            case.decouvre_case()
            self.nb_case_jouable -=1
            
        if self.nb_case_jouable == 0:
            self.jeu_fini = True
            print('Vous avez gagné !')
            print('Votre score : ')         
        
        #self.affichage_grille(self.grille)

    def lancement_jeu(self):
        while self.jeu_fini == False :
            x = int(input('Quelle colonne ? '))
            y = int(input('Quelle ligne ? '))
            self.clic_case(x,y)


    #def affichage_grille(self,grille):

