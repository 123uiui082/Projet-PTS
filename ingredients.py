class Ingredient:
    def __init__(self, nom, quantite=None):
        self.nom = nom
        self.quantite = quantite

    def ajouter(self):
        return f"Ajouté : {self.nom} ({self.quantite})"

    def supprimer(self):
        return f"Supprimé : {self.nom}"
