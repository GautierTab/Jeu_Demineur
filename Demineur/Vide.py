from case import Case

class Vide(Case):
    """
    Classe fille de la classe Case, en précisant le paramètre self.valeur
    """
    def __init__(self):
        super().__init__()
        self.valeur = 0
