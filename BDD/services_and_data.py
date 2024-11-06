import sqlite3
import os
import mysql.connector


def connection() :
    try :
        conn = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="",
                                       database="pa_data")
        print("Connection établie avec Succès !")

        return conn
    
    except:
        print("Exchec de Connection !")


def ajouter(product):
    conn = connection()
    cursor = conn.cursor()

    valeurs = (product.nom, product.quantity, product.category, 
               product.mesure, product.start_date, product.end_date)
    cursor.execute(""" 
            INSERT INTO personne (nom, quantity, category, mesure, start_date, end_date) VALUES(%s, %s, %s, %s, %s, %s)
        """, valeurs)
    
    conn.close()

def parcourir():
    conn = connection()
    cursor = conn.cursor()

    cursor.execute(""" SELECT * FROM personne """)
    rows = cursor.fetchall()

    return rows
    
    conn.close()









































def create_database () :
    if not os.path.exists("products_db.db"):
        connection = sqlite3.connect("products_data.db")
        cursor = connection.cursor()
        cursor.execute("""

        CREATE TABLE prod_table(
                       id text,
                       nom text,
                       quantite int,
                       category text,
                       mesure text,
                       date_debut text,
                       date_fin text
        )
                       
        """)
        connection.commit()
        connection.close()

def register_products(nom, quantite, category,
                       mesure, date_debut,
                       date_fin) :
    try:
        connection = sqlite3.connect("products_db.db")

        cursor = connection.cursor()
        cursor.execute(f"""

                        INSERT INTO prod_table VALUES (
                                                    "{nom}",
                                                    "{quantite}",
                                                    "{category}",
                                                    "{mesure}",
                                                    "{date_debut}",
                                                    "{date_fin}") 
                       
                       """)
        
        connection.commit()

        cursor.execute("""
        SELECT * FROM prod_table
        """)

        connection.commit()
        connection.close()

        return True

    except Exception as error :
        return False
    
def browse_data ():
    connection = sqlite3.connect("products_db.db")
    cursor = connection.cursor()
    cursor.execute(""" SELECT * FROM prod_table """)
    rows = cursor.fetchall()

    return rows
    
    conn.close()

def check_username_exists (id_produit, nom_produit) :
    connection = sqlite3.connect("products_db.db")

    cursor = connection.cursor()
    cursor.execute(f"""

        SELECT id_produit FROM products WHERE id_produit == "{id_produit}"

    """)

    connection.commit()

    response = cursor.fetchall()
    connection.close()
    return response


