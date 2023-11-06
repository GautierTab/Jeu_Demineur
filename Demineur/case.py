import numpy as np


# x (int)
# y (int)
# contient_mine = False
# est_decouvert = False
# est_marquee = False

class Case():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.contient_mine = False
        self.est_decouvert = False
        self.est_marquee = False
        

    # def initialiser_case(self):
       

    def ajoute_mine(self):
        self.contient_mine = True

    def decouvre_case(self):
        self.est_decouvert = True

    def marque_case(self):
        self.est_marquee = True

    def demarque_case(self):
        self.est_marquee = False