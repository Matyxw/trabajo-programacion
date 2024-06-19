#son librerias
import tkinter as tk
from tkinter import messagebox
from tkinter import*
from tkinter import ttk 

password =tk.StringVar
#creo la pantalla principal
def pantalla_inicio ():
    #agarro la variable pantalla y la global
    global pantalla
    #defino la pantalla y defino su tamaño
    pantalla = Tk()
    pantalla.geometry("300x380")
    #pongo un titulo
    pantalla.title("Bienvenidos")

    #le digo al programa que me escriba un texto y defino el color, la pocicion, que me remarque y el tamaño
    Label (text = "acceso al sistema", bg= "navy", fg="white", width="300", height="3", font=("calibri", 15)).pack()
    Label (text="").pack()

    #creo el boton y defino la pocicion, el tamaño, el color y donde te va a enviar el voton  
    Button (text= "iniciar sesion", height="3", width="30", command=iniciar_sesion).pack()
    Label(text="").pack()

    #creo el boton y defino la pocicion, el tamaño, el color y donde te va a enviar el voton
    Button (text= "Registro", height="3", width="30", command=Registro).pack()

    pantalla.mainloop()


#creo otra pantalla
def iniciar_sesion ():
    #despues de aqui es lo mismo
    global pantalla1 
    pantalla1 = Toplevel (pantalla)
    pantalla1.geometry("400x450")
    pantalla1.title("inicio de sesion")

    Label (pantalla1, text="Por favor ingrese su usuario y contraseña", bg= "navy", fg="white", width="300", height="3", font=("sans-serif", 15)).pack()
    Label (pantalla1, text="").pack()

    #le digo que me escriba y defino una funcion
    usuario_label = ttk.Label(pantalla1, text="Usuario")
    #defino el tamaño, la uvicacion el color ect. 
    usuario_label.place(x=50, y=100,width=140)
    #aqui estoy pidiendo que se muestre
    usuario_label.pack()
    #defino en donde va aparecer y creo un imput
    pantalla1.entrada=ttk.Entry(pantalla1)
    pantalla1.entrada.place(x=50, y=100,width=140)


    
    #le digo que me escriba y defino una funcion
    contraseña_label = ttk.Label(pantalla1, text="contraseña")
    #defino el tamaño, la uvicacion el color ect.
    contraseña_label.place(x=50, y=200,width=140)
     #aqui estoy pidiendo que se muestre
    contraseña_label.pack()
    #defino en donde va aparecer y creo un imput
    pantalla1.entrada=ttk.Entry(pantalla1)
    pantalla1.entrada.place(x=50, y=200,width=140)



    # email_label = ttk.Label(pantalla1, text="Email Address:")
    # email_label.grid(10,0)
    # email_label.pack()
    # pantalla1.entrada=ttk.Entry(pantalla1)
    # pantalla1.entrada.grid(10,1)


    # password_label = ttk.Label(pantalla1, text="Password:")
    # password_label.pack(fill='x', expand=False)
    # password_entry = ttk.Entry(pantalla1, textvariable=password, show="*")
    # password_entry.pack(fill='x', expand=False)
  

def Registro ():
    global pantalla2
    pantalla2 = Toplevel (pantalla)
    pantalla2.geometry("400x250")
    pantalla2.title("registrarse")

    Label (pantalla2, text="Por favor ingrese un usuario y contraseña \n para registrar", bg= "navy", fg="white", width="300", height="3", font=("calibri", 15))
    Label (pantalla2, text = "").pack()
    

pantalla_inicio()