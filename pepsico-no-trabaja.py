#principal
import tkinter as Tk
from tkinter import messagebox
from tkinter import*
from tkinter import ttk

def pantalla_inicio ():
    global pantalla
    pantalla = Tk()
    pantalla.geometry("500x500")
    pantalla.title("Escuela tecnica N°1 Manuel Belgrano")
    pantalla.configure(bg='#000')

    Label (text ="Bienvenido a nuestro sistema", bg= "#111", fg= "#eee", width = "300", height= "3",font= ("monserrat", 15),bd=2,relief='ridge').pack()
    Label (text= "", bg='#000').pack()

    Button(text="acceder",bg="#111", height=3, width=20, fg="#eee", bd=2,relief='sunken').pack()

    pantalla.mainloop()
pantalla_inicio()