from tkinter import*
import customtkinter
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import os
import sqlite3
from datetime import date

from BDD import database, services_and_data


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")


root = customtkinter.CTk()
root.geometry("1080x640+285+90")
root.title("Planning Application")
root.iconbitmap("D:\PROJEETS\Python\IconDM\DM-Corporation.ico")

nom_prod_var = StringVar()
quantite_prod_var = IntVar()
category_prod_var = StringVar()
mesure_prod_var = StringVar()
date_debut_var = StringVar()
date_fin_var = StringVar()

#Our Images
add_icon = PhotoImage(file="D:\\PROJEETS\\Python\IconDM\\ajouter.png")
evolution_icon = PhotoImage(file="D:\\PROJEETS\\Python\IconDM\\evolution_icon.png")
historique_icon = PhotoImage(file="D:\\PROJEETS\\Python\IconDM\\historique.png")
affichage_icon = PhotoImage(file="D:\\PROJEETS\\Python\IconDM\\affichage.png")
apropos_icon = PhotoImage(file="D:\\PROJEETS\\Python\IconDM\\a_propos.png")
logo_icon = PhotoImage(file="D:\\PROJEETS\\Python\\PA\\img\\logo_pa.png")
logo_icon_black = PhotoImage(file="D:\\PROJEETS\\Python\\PA\\img\\logo_pa_black.png")
presentation_icon = PhotoImage(file="D:\\PROJEETS\\Python\\PA\\img\\folder2X.png")
stat_icon = PhotoImage(file="D:\\PROJEETS\\Python\\PA\\img\\stat_icon.png")


fontMenu = ("helvetica", 12)
#bg_col = ("#131314")
bg_col = ("#0078d7")
dark_white = ("#b4b4b4")
dark_blue_col = "#0078d7"
light_blue_col = "#0068ba"

list_category_prod = ["Fruits", "Graines", "Liquide", "Feuillages", "Autres"]
list_mesure_produit = ["Kilogramme", "Sacs", "Litres", "Gramme", "Autres Mesures"]


#### SI MESSAGE, REGARDER LES POSITIONNEMENTS ICI
def message_box (msg) :

    message_frame = Frame(root, relief=SOLID, 
                          highlightthickness=2,
                          highlightbackground="gray")
    
    close_btn = customtkinter.CTkButton(message_frame, text="X", 
                                        font=("helvetica", 12, "bold"), width=75, height=25,
                                        fg_color=bg_col, corner_radius=1,
                                        command=lambda : message_frame.destroy())
    close_btn.pack(side=TOP, anchor=E)

    message_lb = customtkinter.CTkLabel(message_frame, text=msg,
                                        font=("helvetica", 18, "bold")
                                        )
    message_lb.pack(pady=35)


    message_frame.place(x=550, y=250, width=450, height=320)



########### PAGE AJOUTER UN PRODUIT
def ajouter_prod():

    
    def save_product ():
        today_date = date.today()

        if nom_produit.get() == "":
            message_box("Product Name required !")
        elif quantite_prod.get() == "":
            message_box("Product Quantity required !")
        elif category_prod.get() == "":
            message_box("Product Category required !")
        elif mesure_prod.get() == "":
            message_box("Product Measure required !")
        elif date_debut.get_date() < today_date:
            message_box("Start Date must be\nhigh or Today Date")
        elif date_fin.get_date() <= date_debut.get_date():
            message_box("End Date must be\nhigh or Start Date")
        else:
            services_and_data.ajouter()
            """services_and_data.register_products(nom_produit.get(),
                                                quantite_prod.get(),
                                                category_prod.get(),
                                                mesure_prod.get(),
                                                date_debut.get_date(),
                                                date_fin.get_date()
                                                )"""
            message_box("Successfully Saved !")
                                 

    def func_list_categor (even="") :
        pass

    
    mesure_fruits = "Kilogramme"
    mesure_graines = "Sacs"
    mesure_liquide = "Litres"
    mesure_feuillage = "Gramme"
    autres_mesures = "Autres Mesures"

    ajouter_indication_frame = customtkinter.CTkFrame(main_frame, width=300)
    ajouter_indication_frame.pack(side=LEFT, fill=BOTH)

    ajouter_prod_frame = customtkinter.CTkFrame(main_frame)

    # Le formulaire d'ajout de produit
    formulaire_ajouter_frame = customtkinter.CTkFrame(ajouter_prod_frame, width=1080, height=600)

    form_title = customtkinter.CTkLabel(master=formulaire_ajouter_frame, 
                                        text="Formulaire D'ajout de Produit",
                                        font=("Helvetica", 17, "bold")
                                        )
    form_title.pack(pady=30)
    nom_produit = customtkinter.CTkEntry(master=formulaire_ajouter_frame, 
                                         placeholder_text="Nom du Produit",
                                         fg_color="#efefff",
                                         placeholder_text_color="#848484",
                                         text_color="#121222", border_color=light_blue_col,
                                         width=220)
    nom_produit.pack(pady=10)

    quantite_prod = customtkinter.CTkEntry(master=formulaire_ajouter_frame, 
                                        placeholder_text="Quantité Prévue", fg_color="#efefff", placeholder_text_color="#848484",
                                        text_color="#121222", width=220,
                                        border_color=light_blue_col
                                           )
    quantite_prod.pack(pady=10)

    category_prod = customtkinter.CTkComboBox(master=formulaire_ajouter_frame, 
                                         values=["Fruits",
                                                 "Graines",
                                                 "Liquide",
                                                 "Feuillages",
                                                 "Autres"],
                                         fg_color="#efefff", text_color="#121222", width=220,
                                         border_color=light_blue_col, button_color=light_blue_col,
                                         button_hover_color=dark_blue_col, state="readonly",
                                         dropdown_hover_color=light_blue_col
                                         )
    category_prod.pack(pady=10)
    category_prod.set("Select Category")

    mesure_prod =customtkinter.CTkComboBox(master=formulaire_ajouter_frame, 
                                         values=["Kilogramme",
                                                 "Sacs",
                                                 "Litres",
                                                 "Gramme",
                                                 "Autres Mesures"],
                                         fg_color="#efefff", text_color="#121222", width=220,
                                         border_color=light_blue_col, button_color=light_blue_col,
                                         button_hover_color=dark_blue_col, state="readonly",
                                         dropdown_hover_color=light_blue_col
                                         )
    mesure_prod.pack(pady=10)
    mesure_prod.set("Select Measure")

    date_debut = DateEntry(master=formulaire_ajouter_frame)
    date_debut.pack(pady=10)

    date_fin = DateEntry(master=formulaire_ajouter_frame)
    date_fin.pack(pady=10)

    progressbar = customtkinter.CTkProgressBar(formulaire_ajouter_frame, orientation="horizontal")
    progressbar.pack(pady=15)

    ######## Bouton ENREGISTRER (produit ajouté)
    enregistrer_prod_btn = customtkinter.CTkButton(formulaire_ajouter_frame, text="Enregistrer",
                                                    font=("helvetica", 15, "bold"), width=175, height=35,
                                                    fg_color=bg_col, corner_radius=3,
                                                    command=save_product)

    enregistrer_prod_btn.pack(pady=25)


    formulaire_ajouter_frame.pack(fill=BOTH)

    ajouter_prod_frame.pack(fill=BOTH)



def evolution() :
    evolution_frame = customtkinter.CTkFrame(main_frame)

    test_ajouter = Label(evolution_frame, text="Bienvenue dans la page d'Evolution des activitées", font=("bold", 22))
    test_ajouter.pack(pady=100)

    evolution_frame.pack()
    evolution_frame.pack_propagate(False)
    evolution_frame.configure(width=1920, height=1080)

def affichage() :
    affichage_frame = customtkinter.CTkFrame(main_frame)

    test_ajouter = Label(affichage_frame, text="Bienvenue dans la page d'Affichage des produits", font=("bold", 22))
    test_ajouter.pack(pady=100)
    product_list_canvas = customtkinter.CTkCanvas(affichage_frame)

    title_bg = "#0068ba"
    title_font = ("bold", 12)

    num_title = customtkinter.CTkLabel(product_list_canvas, text="N°", fg_color=title_bg,
                                       font=title_font, text_color="white")
    num_title.grid(row=0, column=0, padx=10, pady=5)
    name_title = customtkinter.CTkLabel(product_list_canvas, text="Nom du Produit", fg_color=title_bg,
                                       font=title_font, text_color="white")
    name_title.grid(row=0, column=1, padx=10, pady=5)
    category_title = customtkinter.CTkLabel(product_list_canvas, text="Catégorie du Produit", fg_color=title_bg,
                                       font=title_font, text_color="white")
    category_title.grid(row=0, column=2, padx=10, pady=5)
    mesure_title = customtkinter.CTkLabel(product_list_canvas, text="Type de mésure", fg_color=title_bg,
                                       font=title_font, text_color="white")
    mesure_title.grid(row=0, column=3, padx=10, pady=5)
    start_title = customtkinter.CTkLabel(product_list_canvas, text="Début Production", fg_color=title_bg,
                                       font=title_font, text_color="white")
    start_title.grid(row=0, column=4, padx=10, pady=5)
    end_title = customtkinter.CTkLabel(product_list_canvas, text="Fin Production", fg_color=title_bg,
                                       font=title_font, text_color="white")
    end_title.grid(row=0, column=5, padx=10, pady=5)

    statuts_titlte = customtkinter.CTkLabel(product_list_canvas, text="Statut :", fg_color=title_bg,
                                       font=title_font, text_color="white")
    statuts_titlte.grid(row=1, column=0, columnspan=6)

    #Show Data
    liste_prod = services_and_data.browse_data()
    if liste_prod:
        r = 2
        for p in liste_prod:

            id = customtkinter.CTkLabel(product_list_canvas, text=p[1], bg_color="white")
            nom = customtkinter.CTkLabel(product_list_canvas, text=p[2], bg_color="white")
            quantity = customtkinter.CTkLabel(product_list_canvas, text=p[3], bg_color="white")
            mesure = customtkinter.CTkLabel(product_list_canvas, text=p[4], bg_color="white")
            start_date = customtkinter.CTkLabel(product_list_canvas, text=p[5], bg_color="white")
            end_date = customtkinter.CTkLabel(product_list_canvas, text=p[6], bg_color="white")

            id.grid(row=r, column=0)
            nom.grid(row=r, column=1)
            quantity.grid(row=r, column=2)
            mesure.grid(row=r, column=3)
            start_date.grid(row=r, column=4)
            end_date.grid(row=r, column=5)

            product_list_canvas.create_line(9, 55, 355, 55, width=1, fill='white')

            r += 1

            statuts_titlte.configure(text="{} Inscrits pour le moment".format(len(liste_prod)))
            statuts_titlte.grid(row=r, column=0, columnspan=6, pady=2)
    


    product_list_canvas.pack()

    affichage_frame.pack()
    affichage_frame.pack_propagate(False)
    affichage_frame.configure(width=1920, height=1080)

def historique() :
    historique_frame = customtkinter.CTkFrame(main_frame)

    test_ajouter = Label(historique_frame, text="Bienvenue dans la page d'Historique des produits", font=("bold", 22))
    test_ajouter.pack(pady=100)

    historique_frame.pack()
    historique_frame.pack_propagate(False)
    historique_frame.configure(width=1920, height=1080)

def apropos() :
    apropos_frame = customtkinter.CTkFrame(main_frame)

    test_ajouter = Label(apropos_frame, text="Bienvenue dans la page d'A propos du Développeur des produits", font=("bold", 22))
    test_ajouter.pack(pady=100)

    apropos_frame.pack()
    apropos_frame.pack_propagate(False)
    apropos_frame.configure(width=1920, height=1080)






def hide_indicate():
    """If not clicked hide indicator"""
    add_lb.config(bg="#0078d7")
    evolution_lb.config(bg="#0078d7")
    affiche_lb.config(bg="#0078d7")
    historique_lb.config(bg="#0078d7")
    apropos_lb.config(bg="#0078d7")

def delete_page():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate (lb, page):
    """If button clicked, change indicator to white"""
    hide_indicate()
    lb.config(bg="white")
    delete_page()
    page()


########### FRAME DES MENUS
menus_frame = Frame(root, bg=bg_col)

logo_img = Label(menus_frame, image=logo_icon, bg=bg_col)
logo_img.pack(pady= 15, anchor=CENTER)
#hauteur_separat = 70


ajouter_prod_btn = customtkinter.CTkButton(menus_frame, text="Ajouter Produit", bg_color=bg_col, 
                                           fg_color=bg_col, command=lambda: indicate(add_lb, ajouter_prod),
                          font=("helvetica", 13), hover_color="#0068ba", text_color="white")
ajouter_prod_btn.place(x=45, y=120)
add_img = Label(menus_frame, image=add_icon, bg=bg_col)
add_img.place(x=35, y=150)
add_lb = Label(menus_frame, bg=bg_col)
add_lb.place(x=1, y=147, width=6, height=40)

evolution_btn = customtkinter.CTkButton(menus_frame, text="Evolution", bg_color=bg_col, fg_color=bg_col,
                          font=("helvetica", 13), hover_color="#0068ba", text_color="white",
                          command=lambda: indicate(evolution_lb, evolution))
evolution_btn.place(x=30, y=176)
evolution_img = Label(menus_frame, image=evolution_icon, bg=bg_col)
evolution_img.place(x=35, y=220)
evolution_lb = Label(menus_frame, bg=bg_col)
evolution_lb.place(x=1, y=217, width=6, height=40)



affichage_btn = customtkinter.CTkButton(menus_frame, text="Afficher", bg_color=bg_col, fg_color=bg_col,
                          font=("helvetica", 13), hover_color="#0068ba", text_color="white",
                          command=lambda: indicate(affiche_lb, affichage))
affichage_btn.place(x=30, y=230)
affichage_img = Label(menus_frame, image=affichage_icon, bg=bg_col)
affichage_img.place(x=35, y=285)
affiche_lb = Label(menus_frame, bg=bg_col)
affiche_lb.place(x=1, y=282, width=6, height=40)


historique_btn = customtkinter.CTkButton(menus_frame, text="Historique", bg_color=bg_col, fg_color=bg_col,
                          font=("helvetica", 13), hover_color="#0068ba", text_color="white",
                          command=lambda: indicate(historique_lb, historique))
historique_btn.place(x=30, y=281)
historique_img = Label(menus_frame, image=historique_icon, bg=bg_col)
historique_img.place(x=35, y=350)
historique_lb = Label(menus_frame, bg=bg_col)
historique_lb.place(x=1, y=347, width=6, height=40)


apropos_btn = customtkinter.CTkButton(menus_frame, text="A Propos",
                                      bg_color=bg_col, fg_color=bg_col,
                                      font=("helvetica", 13), hover_color="#0068ba",
                                      text_color="white",
                                      command=lambda: indicate(apropos_lb, apropos))
apropos_btn.place(x=30, y=333)
apropos_img = Label(menus_frame, image=apropos_icon, bg=bg_col)
apropos_img.place(x=35, y=415)
apropos_lb = Label(menus_frame, bg=bg_col)
apropos_lb.place(x=1, y=412, width=6, height=40)



#########################

app_version = customtkinter.CTkLabel(menus_frame, text="Dieudonné MUHEMEDI\n--------------------\nPlanning Application : 1.0/2023",
                                     bg_color=bg_col, fg_color="#0068ba", text_color="white",
                                     font=("helvetica", 10, "bold"), width=280, height=50)
app_version.pack(side="bottom")

########################




#menus_frame.place(x=0, y=0,width=350, height=1080 )
menus_frame.pack(side=LEFT, fill=X)
menus_frame.pack_propagate(False)
menus_frame.configure(width=350, height=1080)



########## FRAME PRINCIPAL
main_frame = Frame(root)

logo_presentation = Label(main_frame, image=logo_icon_black)
logo_presentation.pack(pady=35, anchor=CENTER)
presentation_img = Label(main_frame, image=presentation_icon)
presentation_img.place(x=35, y=200)
stat_img = Label(main_frame, image=stat_icon)
stat_img.place(x=480, y=200)

phrase_into = Label(main_frame, text="Le résumé de la production \nde l'année 2023",
                    font=("helvetica", 15), justify=LEFT)
phrase_into.place(x=45, y=420)
phrase_into = Label(main_frame, text="", bg=bg_col)
phrase_into.place(x=45, y=485, width=380, height=4)

commencer_btn = customtkinter.CTkButton(main_frame, text="Voir l'Evolution", font=("helvetica", 15, "bold"), width=175, height=35,
                                        fg_color=bg_col, corner_radius=3, command=lambda: indicate(evolution_lb, evolution))
commencer_btn.place(x=380, y=500, anchor=CENTER)







main_frame.pack(side=LEFT, fill=X)
main_frame.pack_propagate(False)
main_frame.configure(width=1920, height=1080)



root.mainloop()