# Générateur de Recettes de Cuisine

## Description de l’Application

### Nom du Projet :
**Générateur de Recettes de Cuisine**

### Description Générale :
Le projet consiste à développer une application permettant aux utilisateurs de générer des recettes en fonction des ingrédients qu’ils ont à disposition. L’objectif est d’aider à réduire le gaspillage alimentaire et de simplifier la planification des repas.

### Objectifs :
- Réduire le gaspillage alimentaire en optimisant l’utilisation des ingrédients disponibles.
- Simplifier la planification des repas.
- Proposer une interface claire et intuitive accessible à un large public.

---

## Fonctionnalités

### Fonctionnalités Obligatoires :
1. **Saisie des ingrédients disponibles :**
   - Ajout d’ingrédients via un champ de saisie.
   - Affichage d’une liste des ingrédients saisis.
   - Suppression d’ingrédients de la liste.

2. **Génération de recettes :**
   - Propositions de recettes utilisant majoritairement les ingrédients listés.
   - Chaque recette inclut :
     - Le nom du plat.
     - La liste complète des ingrédients.
     - Les étapes de préparation.

3. **Affichage des recettes :**
   - Consultation des détails d’une recette (ingrédients nécessaires, étapes).
   - Priorisation des recettes utilisant tous les ingrédients disponibles.

4. **Compatibilité multiplateforme :**
   - Utilisable sur ordinateur (application desktop ou via navigateur web).

### Fonctionnalités Utiles :
1. **Filtrage des recettes :**
   - Application de filtres (végétarien, sans gluten, etc.).
   - Exclusion de certaines catégories d’ingrédients (par exemple, "pas de viande").

2. **Suggestions d’ingrédients manquants :**
   - Proposition d’ingrédients à ajouter pour compléter une recette.

3. **Enregistrement des ingrédients :**
   - Sauvegarde des ingrédients pour les réutiliser lors d’une session ultérieure.

### Fonctionnalités Optionnelles :
1. **Création de compte utilisateur :**
   - Sauvegarde des recettes favorites.
   - Accès à un historique des recettes et ingrédients utilisés.

2. **Intégration avec une base de données de recettes en ligne :**
   - Synchronisation régulière pour enrichir le catalogue de recettes.

3. **Mode collaboratif :**
   - Partage de listes d’ingrédients entre utilisateurs.
   - Recherche collaborative de recettes.

---

## Modélisation UML

### Diagramme des Classes :

1. **Classe Ingrédient :**
   - **Attributs :** `nom`, `quantité`
   - **Méthodes :** `ajouter()`, `supprimer()`

2. **Classe Recette :**
   - **Attributs :** `nom`, `listeIngrédients`, `instructions`
   - **Méthodes :** `afficherRecette()`, `vérifierIngrédients()`

3. **Classe GénérateurDeRecettes :**
   - **Attributs :** `listeIngrédientsUtilisateur`, `recettesDisponibles`
   - **Méthodes :** `générerRecettes()`, `filtrerRecettes()`, `proposerRecettes()`

4. **Classe Utilisateur :**
   - **Attributs :** `nom`, `email`, `listeIngrédientsSauvegardée`
   - **Méthodes :** `créerCompte()`, `sauvegarderIngrédients()`, `afficherRecettesFavorites()`

---

## Cas d’Usage

### Cas d’usage 1 : Ajouter un ingrédient
1. L'utilisateur saisit un ingrédient dans un champ de texte.
2. Il clique sur le bouton "Ajouter".
3. L’ingrédient apparaît dans la liste des ingrédients disponibles.

### Cas d’usage 2 : Générer des recettes
1. Après avoir ajouté plusieurs ingrédients, l'utilisateur clique sur "Générer recettes".
2. L’application analyse les ingrédients et propose une liste de recettes réalisables.
3. L’utilisateur peut sélectionner une recette pour afficher les détails.

### Cas d’usage 3 : Filtrer les recettes (fonctionnalité utile)
1. L’utilisateur clique sur "Filtrer".
2. Il sélectionne un filtre, par exemple "végétarien".
3. L’application ne montre que les recettes répondant au filtre.

---

## Contribution
Les contributions sont les bienvenues ! Merci de respecter les bonnes pratiques de développement et de soumettre vos propositions via des pull requests.

---