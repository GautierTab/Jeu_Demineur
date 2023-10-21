import numpy as np


# x (int)
# y (int)
contient_mine = False
est_decouvert = False
est_marquee = False

class Case():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.contient_mine = False
        self.est_decouvert = False
        self.est_marquee = False
