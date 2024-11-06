import os
import sqlite3

def create_database () :
    if not os.path.exists("products_data.db"):
        connection = sqlite3.connect("products_data.db")
        cursor = connection.cursor()
        cursor.execute("""

        CREATE TABLE products(
                       id_produit text,
                       nom_produit text,
                       quantite_produit text,
                       category_produit text,
                       mesure_produit text,
                       ajouter_date_debut text,
                       ajouter_date_fin text
        )
                       
        """)
        connection.commit()
        connection.close()

def register_products(id_produit, nom_produit, quantite_produit, category_produit,
                       mesure_produit, ajouter_date_debut,
                       ajouter_date_fin) :
    try:
        connection = sqlite3.connect("products_data.db")

        cursor = connection.cursor()
        cursor.execute(f"""

                        INSERT INTO products VALUES ("{id_produit}",
                                                    "{nom_produit}",
                                                    "{quantite_produit}",
                                                    "{category_produit}",
                                                    "{mesure_produit}",
                                                    "{ajouter_date_debut}",
                                                    "{ajouter_date_fin}") 
                       
                       """)
        
        connection.commit()

        cursor.execute("""
        SELECT * FROM products
        """)

        connection.commit()
        connection.close()

        return True

    except Exception as error :
        return False

def check_username_exists (id_produit, nom_produit) :
    connection = sqlite3.connect("products_data.db")

    cursor = connection.cursor()
    cursor.execute(f"""

        SELECT id_produit FROM products WHERE id_produit == "{id_produit}"

    """)

    connection.commit()

    response = cursor.fetchall()
    connection.close()
    return response
