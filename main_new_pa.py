import tkinter as tk
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk
#import ttkbootstrap as tb
#from ttkbootstrap import datetime, DateEntry
from tkcalendar import DateEntry
import os
import sqlite3



customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")


root = customtkinter.CTk()
root.geometry("1080x640+285+90")
root.title("Planning Application")
root.iconbitmap("D:\PROJEETS\Python\IconDM\DM-Corporation.ico")

nom_prod_var = tk.StringVar()
quantite_prod_var = tk.IntVar()
category_prod_var = tk.StringVar()
mesure_prod_var = tk.StringVar()
date_debut_var = tk.StringVar()
date_fin_var = tk.StringVar()

add_icon = tk.PhotoImage(file="D:\\PROJEETS\\Python\IconDM\\ajouter.png")
evolution_icon = tk.PhotoImage(file="D:\\PROJEETS\\Python\IconDM\\evolution_icon.png")
historique_icon = tk.PhotoImage(file="D:\\PROJEETS\\Python\IconDM\\historique.png")
affichage_icon = tk.PhotoImage(file="D:\\PROJEETS\\Python\IconDM\\affichage.png")
apropos_icon = tk.PhotoImage(file="D:\\PROJEETS\\Python\IconDM\\a_propos.png")
logo_icon = tk.PhotoImage(file="D:\\PROJEETS\\Python\\PA\\img\\logo_pa.png")
logo_icon_black = tk.PhotoImage(file="D:\\PROJEETS\\Python\\PA\\img\\logo_pa_black.png")
presentation_icon = tk.PhotoImage(file="D:\\PROJEETS\\Python\\PA\\img\\folder2X.png")
stat_icon = tk.PhotoImage(file="D:\\PROJEETS\\Python\\PA\\img\\stat_icon.png")


fontMenu = ("helvetica", 12)
#bg_col = ("#131314")
bg_col = ("#0078d7")
dark_white = ("#b4b4b4")

list_category_prod = ["Fruits", "Graines", "Liquide", "Feuillages", "Autres"]
list_mesure_produit = ["Kilogramme", "Sacs", "Litres", "Gramme", "Autres Mesures"]

#### -column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row, -rowspan, or -sticky 


#### SI MESSAGE, REGARDER LES POSITIONNEMENTS ICI
def message_box (msg) :

    message_frame = tk.Frame(root, relief=tk.SOLID, 
                          highlightthickness=2,
                          highlightbackground="gray")
    
    close_btn = customtkinter.CTkButton(message_frame, text="X", 
                                        font=("helvetica", 12, "bold"), width=175, height=35,
                                        fg_color=bg_col, corner_radius=1,
                                        command=lambda : menus_frame.destroy())
    close_btn.pack(side=tk.TOP, anchor=tk.E)

    message_lb = customtkinter.CTkLabel(message_frame, text=msg,
                                        font=("helvetica", 12, "bold"),
                                        )
    message_lb.pack(pady=20)


    message_frame.place(x=400, y=280, width=230, height=180)



########### PAGE AJOUTER UN PRODUIT
def ajouter_prod() :

    
    def verify_for_register () :
        pass                       

    def func_list_categor (even="") : 
       pass


    
    mesure_fruits = "Kilogramme"
    mesure_graines = "Sacs"
    mesure_liquide = "Litres"
    mesure_feuillage = "Gramme"
    autres_mesures = "Autres Mesures"

    # Onglet ajouter produit
    ajouter_prod_frame = tk.Frame(main_frame, bg="#efefef")


    formulaire_ajouter_frame = customtkinter.CTkFrame(ajouter_prod_frame, width=1080, height=600)
    myPadx = 120
    nom_produit = customtkinter.CTkEntry(master=formulaire_ajouter_frame, 
                                         placeholder_text="Nom du Produit",
                                         fg_color="#efefff", 
                                         placeholder_text_color="#848484",
                                         text_color="#121222",
                                         width=220)
    nom_produit.pack()

    quantite_prod = customtkinter.CTkEntry(master=formulaire_ajouter_frame, 
                                         placeholder_text="Quantité Prévue",
                                         fg_color="#efefff", 
                                         placeholder_text_color="#848484",
                                         text_color="#121222",
                                         width=220
                                           )
    quantite_prod.pack()

    category_prod = customtkinter.CTkComboBox(master=formulaire_ajouter_frame, 
                                         values=["Fruits", 
                                                 "Graines", 
                                                 "Liquide", 
                                                 "Feuillages", 
                                                 "Autres"],
                                         fg_color="#efefff", 
                                         text_color="#121222",
                                         width=220)
    category_prod.pack()

    mesure_prod =customtkinter.CTkComboBox(master=formulaire_ajouter_frame, 
                                         values=["Kilogramme", 
                                                 "Sacs", 
                                                 "Litres", 
                                                 "Gramme", 
                                                 "Autres Mesures"],
                                         fg_color="#efefff", 
                                         text_color="#121222",
                                         width=220)
    mesure_prod.pack()

    #Date frame inside form frame
    date_frame = tk.Frame(formulaire_ajouter_frame)
    date_frame.pack(pady=15)

    date_debut_lbl = tk.Label(master=date_frame, text="Date de Début")
    date_debut_lbl.grid(row=0, column=0, padx=10, pady=10)
    date_fin_lbl = tk.Label(master=date_frame, text="Date de Fin")
    date_fin_lbl.grid(row=0, column=1, padx=10, pady=10)

    date_debut = DateEntry(master=date_frame)
    date_debut.grid(row=1, column=0, padx=10, pady=10)

    date_fin = DateEntry(master=date_frame)
    date_fin.grid(row=1, column=1, padx=10, pady=10)

    ######## Bouton ENREGISTRER (produit ajouté)
    enregistrer_prod_btn = customtkinter.CTkButton(formulaire_ajouter_frame, text="Enregistrer",
                                                    font=("helvetica", 15, "bold"), width=175, height=35,
                                                    fg_color=bg_col, corner_radius=3, 
                                                    command=verify_for_register)

    enregistrer_prod_btn.pack(pady=20)



    formulaire_ajouter_frame.pack()
    #formulaire_ajouter_frame.pack_propagate(False)
    #formulaire_ajouter_frame.configure(width=1080, height=600)
    #formulaire_ajouter_frame.place(x=0, y=360, width=1920, height=400)






    ajouter_prod_frame.pack()
    ajouter_prod_frame.pack_propagate(False)
    ajouter_prod_frame.configure(width=1920, height=1080)

def evolution() :
    evolution_frame = (main_frame)

    test_ajouter = tk.Label(evolution_frame, text="Bienvenue dans la page d'Evolution des activitées", font=("bold", 22))
    test_ajouter.pack(pady=100)

    evolution_frame.pack()
    evolution_frame.pack_propagate(False)
    evolution_frame.configure(width=1920, height=1080)

def affichage() :
    affichage_frame = (main_frame)

    test_ajouter = tk.Label(affichage_frame, text="Bienvenue dans la page d'Affichage des produits", font=("bold", 22))
    test_ajouter.pack(pady=100)

    affichage_frame.pack()
    affichage_frame.pack_propagate(False)
    affichage_frame.configure(width=1920, height=1080)

def historique() :
    historique_frame = (main_frame)

    test_ajouter = tk.Label(historique_frame, text="Bienvenue dans la page d'Historique des produits", font=("bold", 22))
    test_ajouter.pack(pady=100)

    historique_frame.pack()
    historique_frame.pack_propagate(False)
    historique_frame.configure(width=1920, height=1080)

def apropos() :
    apropos_frame = (main_frame)

    test_ajouter = tk.Label(apropos_frame, text="Bienvenue dans la page d'A propos du Développeur des produits", font=("bold", 22))
    test_ajouter.pack(pady=100)

    apropos_frame.pack()
    apropos_frame.pack_propagate(False)
    apropos_frame.configure(width=1920, height=1080)






def hide_indicate():
    add_lb.config(bg="#0078d7")
    evolution_lb.config(bg="#0078d7")
    affiche_lb.config(bg="#0078d7")
    historique_lb.config(bg="#0078d7")
    apropos_lb.config(bg="#0078d7")

def delete_page():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate (lb, page):
    hide_indicate()
    lb.config(bg="white")
    delete_page()
    page()


########### FRAME DES MENUS
menus_frame = tk.Frame(root, bg=bg_col)

logo_img = tk.Label(menus_frame, image=logo_icon, bg=bg_col)
logo_img.pack(pady= 15, anchor=tk.CENTER)
#hauteur_separat = 70


ajouter_prod_btn = customtkinter.CTkButton(menus_frame, text="Ajouter Produit", bg_color=bg_col, 
                                           fg_color=bg_col, command=lambda: indicate(add_lb, ajouter_prod),
                          font=("helvetica", 13), hover_color="#0068ba", text_color="white")
ajouter_prod_btn.place(x=45, y=120)
add_img = tk.Label(menus_frame, image=add_icon, bg=bg_col)
add_img.place(x=35, y=150)
add_lb = tk.Label(menus_frame, bg=bg_col)
add_lb.place(x=1, y=147, width=6, height=40)

evolution_btn = customtkinter.CTkButton(menus_frame, text="Evolution", bg_color=bg_col, fg_color=bg_col,
                          font=("helvetica", 13), hover_color="#0068ba", text_color="white",
                          command=lambda: indicate(evolution_lb, evolution))
evolution_btn.place(x=30, y=176)
evolution_img = tk.Label(menus_frame, image=evolution_icon, bg=bg_col)
evolution_img.place(x=35, y=220)
evolution_lb = tk.Label(menus_frame, bg=bg_col)
evolution_lb.place(x=1, y=217, width=6, height=40)



affichage_btn = customtkinter.CTkButton(menus_frame, text="Afficher", bg_color=bg_col, fg_color=bg_col,
                          font=("helvetica", 13), hover_color="#0068ba", text_color="white",
                          command=lambda: indicate(affiche_lb, affichage))
affichage_btn.place(x=30, y=230)
affichage_img = tk.Label(menus_frame, image=affichage_icon, bg=bg_col)
affichage_img.place(x=35, y=285)
affiche_lb = tk.Label(menus_frame, bg=bg_col)
affiche_lb.place(x=1, y=282, width=6, height=40)


historique_btn = customtkinter.CTkButton(menus_frame, text="Historique", bg_color=bg_col, fg_color=bg_col,
                          font=("helvetica", 13), hover_color="#0068ba", text_color="white",
                          command=lambda: indicate(historique_lb, historique))
historique_btn.place(x=30, y=281)
historique_img = tk.Label(menus_frame, image=historique_icon, bg=bg_col)
historique_img.place(x=35, y=350)
historique_lb = tk.Label(menus_frame, bg=bg_col)
historique_lb.place(x=1, y=347, width=6, height=40)


apropos_btn = customtkinter.CTkButton(menus_frame, text="A Propos",
                                      bg_color=bg_col, fg_color=bg_col,
                                      font=("helvetica", 13), hover_color="#0068ba",
                                      text_color="white",
                                      command=lambda: indicate(apropos_lb, apropos))
apropos_btn.place(x=30, y=333)
apropos_img = tk.Label(menus_frame, image=apropos_icon, bg=bg_col)
apropos_img.place(x=35, y=415)
apropos_lb = tk.Label(menus_frame, bg=bg_col)
apropos_lb.place(x=1, y=412, width=6, height=40)



#########################

concepteur = customtkinter.CTkLabel(menus_frame, text="Dieudonné MUHEMEDI",
                                     bg_color=bg_col, fg_color="#0068ba", text_color="white",
                                     font=("helvetica", 11), width=280, height=80)
concepteur.place(x=0, y=580)
app_version = customtkinter.CTkLabel(menus_frame, text="Planning Application : 1.0/2023",
                                     bg_color=bg_col, fg_color="#0068ba", text_color="white",
                                     font=("helvetica", 10, "bold"), width=280, height=20)
app_version.place(x=0, y=590)


########################




#menus_frame.place(x=0, y=0,width=350, height=1080 )
menus_frame.pack(side=tk.LEFT)
menus_frame.pack_propagate(False)
menus_frame.configure(width=350, height=1080)



########## FRAME PRINCIPAL
main_frame = tk.Frame(root)

logo_presentation = tk.Label(main_frame, image=logo_icon_black)
logo_presentation.pack(pady=35, anchor=tk.CENTER)
presentation_img = tk.Label(main_frame, image=presentation_icon)
presentation_img.place(x=35, y=200)
stat_img = tk.Label(main_frame, image=stat_icon)
stat_img.place(x=480, y=200)

phrase_into = tk.Label(main_frame, text="Le résumé de la production \nde l'année 2023",
                    font=("helvetica", 15), justify=tk.LEFT)
phrase_into.place(x=45, y=420)
phrase_into = tk.Label(main_frame, text="", bg=bg_col)
phrase_into.place(x=45, y=485, width=380, height=4)

commencer_btn = customtkinter.CTkButton(main_frame, text="Voir l'Evolution", font=("helvetica", 15, "bold"), width=175, height=35,
                                        fg_color=bg_col, corner_radius=3, command=lambda: indicate(evolution_lb, evolution))
commencer_btn.place(x=380, y=500, anchor=tk.CENTER)







main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=1920, height=1080)



root.mainloop()