import grille as g
import Bombe as b
import Chiffre as ch
import Vide as v

class jeu():
    def __init__(self):
        self.jeu_fini = False
        self.grille = g.Grille()
        
    def lancement_jeu(self):
        """
        Cette fonction permet de lancer le jeu.
        L'algo prend en compte les input du joueur, et envoie les informations à grille.py
        """
        print("================================")
        print("Bienvenu dans le jeu du démineur")
        print("Réalisé par Gautier TABORDET, ING3 - ENSG / Université Gustave Eiffel")
        print("Version 1.0")
        print("================================")
        self.grille.initialiser()
        print(self.grille)
        while self.jeu_fini == False:
            print('Nombre de cases à découvrir : ', self.grille.nb_case_decouvertes())
            print('Nombre de mines restantes : ', self.grille.nb_case_minees())
            print('---------------------------------------------------')
            x = int(input('Quelle ligne ? '))
            y = int(input('Quelle colonne ? '))
            print('\n')
            if x<0 or y<0 or x>self.grille.taille_x-1 or y>self.grille.taille_y-1:
                print('Veuillez indiquer un chiffre compris dans la grille')
            else:
                action = int(input('Découvrir (1), Marquer (2) ou Démarquer (3) ? '))
                print('\n')
                if action == 1 :
                    if self.grille.grille[x,y].est_marquee :
                        print('Cette case est marquée, elle ne peut pas être découverte')
                        print(self.grille)
                        pass
                    else:
                        if self.grille.clic_case(x,y): 
                            print(self.grille)
                            break
                        else:
                            print(self.grille)
                elif action == 2:
                    if not self.grille.grille[x,y].est_marquee and not self.grille.grille[x,y].est_decouvert:
                        self.grille.marquer_case(self.grille.grille[x,y])
                        print(self.grille)
                    elif self.grille.grille[x,y].est_marquee :
                        print("La case est déjà marquée")
                        print(self.grille)
                        pass
                    elif self.grille.grille[x,y].est_decouvert :
                        print("La case est déjà découverte")
                        print(self.grille)
                        pass
                elif action == 3:
                    if self.grille.grille[x,y].est_marquee :
                        self.grille.demarquer_case(self.grille.grille[x,y])
                        print(self.grille)
                    else:
                        print("La case n'est pas marquée")
                        print(self.grille)
                        pass
                else:
                    print('Veuillez indiquer quelle action faire')
                    print(self.grille)
        return

