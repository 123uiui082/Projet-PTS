import sqlite3

class Database:
    def __init__(self, db_name="recettes.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def creer_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS recettes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                ingredients TEXT,
                instructions TEXT
            )
        ''')
        self.conn.commit()

    def ajouter_recette(self, recette):
        self.cursor.execute('''
            INSERT INTO recettes (nom, ingredients, instructions) 
            VALUES (?, ?, ?)
        ''', (recette.nom, ','.join(recette.liste_ingredients), recette.instructions))
        self.conn.commit()

    def recuperer_recettes(self):
        self.cursor.execute("SELECT * FROM recettes")
        return self.cursor.fetchall()

    def fermer(self):
        self.conn.close()
