import numpy as np
import grille as g
import Bombe as b
import Chiffre as ch
import Vide as v

class jeu():
    def __init__(self):
        self.jeu_fini = False
        self.grille = g.Grille()
        
    def lancement_jeu(self):
        self.grille.initialiser()
        print(self.grille)
        while self.jeu_fini == False:
            x = int(input('Quelle ligne ? '))
            y = int(input('Quelle colonne ? '))
            if x<0 or y<0 or x>self.grille.taille_x or y>self.grille.taille_y:
                print('Veuillez indiquer un chiffre compris dans la grille')
            else:
                # action = int(input('Découvrir (1) ou Marquer (2) ou Démarquer (3) ? '))
                # if action == 1 :
                #     if self.grille.grille[x,y].est_marquee :
                #         print('Cette case est marquée, elle ne peut pas être découverte')
                #         pass
                #     else:
                #       Découvrir la case
                self.grille.clic_case(x,y)
                print(self.grille)
                # if action == 2:
                #     if not self.grille.grille[x,y].est_marquee :
                #         self.grille.marquer_case(self.grille.grille[x,y])
                #     else:
                #         print("La case est déjà marquée")
                #         pass
                # if action == 3:
                #     if self.grille.grille[x,y].est_marquee :
                #         self.grille.demarquer_case(self.grille.grille[x,y])
                #     else:
                #         print("La case n'est pas marquée")
                #         pass
        return

