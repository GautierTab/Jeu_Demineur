class Case():
    """
    Classe permettant de définir chaque élément de la grille comme étant une case.
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.contient_mine = False
        self.est_decouvert = False
        self.est_marquee = False
       
    def ajoute_mine(self):
        self.contient_mine = True

    def decouvre_case(self):
        self.est_decouvert = True

    def marque_case(self):
        self.est_marquee = True

    def demarque_case(self):
        self.est_marquee = False