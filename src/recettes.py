class Recette:
    def __init__(self, nom, liste_ingredients, instructions):
        self.nom = nom
        self.liste_ingredients = liste_ingredients
        self.instructions = instructions

    def afficher_recette(self):
        return f"Recette: {self.nom}\\nIngrédients: {', '.join(self.liste_ingredients)}\\nInstructions: {self.instructions}"

    def verifier_ingredients(self, ingredients_utilisateur):
        return all(ingredient in ingredients_utilisateur for ingredient in self.liste_ingredients)
