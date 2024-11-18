import tkinter as tk
from tkinter import messagebox
from recettes import Recette

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Générateur de Recettes de Cuisine")
        self.geometry("600x400")
        self.ingredients = []

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Entrez un ingrédient:")
        self.label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.add_button = tk.Button(self, text="Ajouter", command=self.ajouter_ingredient)
        self.add_button.pack()

        self.ingredients_listbox = tk.Listbox(self)
        self.ingredients_listbox.pack()

        self.generate_button = tk.Button(self, text="Générer Recettes", command=self.generer_recettes)
        self.generate_button.pack()

    def ajouter_ingredient(self):
        ingredient = self.entry.get()
        if ingredient:
            self.ingredients.append(ingredient)
            self.ingredients_listbox.insert(tk.END, ingredient)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Avertissement", "Veuillez entrer un ingrédient.")

    def generer_recettes(self):
        recettes_exemple = [
            Recette("Salade Verte", ["laitue", "tomate", "concombre"], "Mélanger les ingrédients."),
            Recette("Omelette", ["oeuf", "lait", "sel"], "Battre les oeufs avec le lait et cuire."),
        ]

        recettes_possibles = [
            recette for recette in recettes_exemple
            if recette.verifier_ingredients(self.ingredients)
        ]

        if recettes_possibles:
            for recette in recettes_possibles:
                messagebox.showinfo("Recette", recette.afficher_recette())
        else:
            messagebox.showinfo("Aucune Recette", "Aucune recette trouvée avec les ingrédients fournis.")
