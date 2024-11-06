from tkinter import*
import customtkinter
from PIL import Image, ImageTk
import ttkbootstrap as tb

import index_pa


"""
def ajouter_prod_frame () :

    ajouter_prod_fr = Frame(index_pa.main_frame)
    label_ajouter = customtkinter.CTkLabel(master=ajouter_prod_frame, text="Ajouter un Produit ici !")
    label_ajouter.pack(pady=25)
    ajouter_prod_fr.pack()"""




root = Tk()
root.geometry("500x600+750+160")
root.title("Planning Application")


date_entry = tb.DateEntry(master=root)
date_entry.pack(pady=100)



root.mainloop()