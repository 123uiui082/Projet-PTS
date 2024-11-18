class Utilisateur:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email
        self.liste_ingredients_sauvegardes = []

    def creer_compte(self):
        return f"Compte créé pour {self.nom} ({self.email})"

    def sauvegarder_ingredients(self, ingredient):
        self.liste_ingredients_sauvegardes.append(ingredient)
        return f"Ingrédient sauvegardé : {ingredient}"

    def afficher_recettes_favorites(self):
        return "Recettes favorites : Non implémentées"
