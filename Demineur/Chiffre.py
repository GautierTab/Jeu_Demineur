import numpy as np
from case import Case

class Chiffre(Case):
    def __init__(self):
        super().__init__()
        self.valeur = 0

    def ajouter_chiffre(self):
        self.valeur +=1
