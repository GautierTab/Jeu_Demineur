import numpy as np
from case import Case

class Bombe(Case):
    def __init__(self):
        super().__init__()
        self.valeur = 'bombe'
        # self.explose = False

    # def exploser(self):
    #     self.explose = True