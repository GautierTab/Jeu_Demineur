from case import Case

class Chiffre(Case):
    """
    Classe fille de la classe Case, en précisant le paramètre self.valeur
    """
    def __init__(self):
        super().__init__()
        self.valeur = 0

    def ajouter_chiffre(self):
        """
        Cette fonction permet d'ajouter 1 au paramètre self.valeur    
        """
        self.valeur +=1
