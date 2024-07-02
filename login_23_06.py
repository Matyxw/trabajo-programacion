import pymysql
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import toma as mo

#--- parte de matias gauto ---#
def on_focus_in(event):
    if event.widget.get() == 'Nombre:':
        event.widget.delete(0, tk.END)
        event.widget.config(fg='black')

def on_focus_out(event):
    if not event.widget.get():
        event.widget.insert(0, 'Nombre:')
        event.widget.config(fg='grey')

def on_focus_in2(event):
    if event.widget.get() == 'Usuario:':
        event.widget.delete(0, tk.END)
        event.widget.config(fg='black')

def on_focus_out2(event):
    if not event.widget.get():
        event.widget.insert(0, 'Usuario:')
        event.widget.config(fg='grey')

def on_focus_in3(event):
    if event.widget.get() == 'Contraseña:':
        event.widget.delete(0, tk.END)
        event.widget.config(fg='black')

def on_focus_out3(event):
    if not event.widget.get():
        event.widget.insert(0, 'Contraseña:')
        event.widget.config(fg='grey')

def on_focus_in4(event):
    if event.widget.get() == 'Apellido:':
        event.widget.delete(0, tk.END)
        event.widget.config(fg='black')

def on_focus_out4(event):
    if not event.widget.get():
        event.widget.insert(0, 'Apellido:')
        event.widget.config(fg='grey')

def on_focus_in5(event):
    if event.widget.get() == 'Confirmar Usuario:':
        event.widget.delete(0, tk.END)
        event.widget.config(fg='black')

def on_focus_out5(event):
    if not event.widget.get():
        event.widget.insert(0, 'Confirmar Usuario:')
        event.widget.config(fg='grey')

def on_focus_in6(event):
    if event.widget.get() == 'Confirmar Contraseña:':
        event.widget.delete(0, tk.END)
        event.widget.config(fg='black')

def on_focus_out6(event):
    if not event.widget.get():
        event.widget.insert(0, 'Confirmar Contraseña:')
        event.widget.config(fg='grey')

def on_focus_in7(event):
    if event.widget.get() == 'Email:':
        event.widget.delete(0, tk.END)
        event.widget.config(fg='black')

def on_focus_out7(event):
    if not event.widget.get():
        event.widget.insert(0, 'Email:')
        event.widget.config(fg='grey')

#parte de Belenger
def pantalla_inicial():
    global pantalla
    pantalla = tk.Tk()
    pantalla.title("opciones")
    pantalla.geometry("500x500")
    pantalla.configure(bg="#efefef")

    b1=tk.Frame(pantalla)
    b1.configure(bg="#4141DA")
    b1.place(relx=0,rely=0,relwidth=1,relheight=0.3)

    label=tk.Label(b1,text="BIENVENIDO A NUESTRO SISTEMA",font=("Times New Roman",10,"bold"),bd=1.5,relief='raised',bg="#fff",fg="#4141DA")
    label.place(relx= 0.28, rely=0.7) 

    bt1=tk.Button(pantalla,text="Registro", command= Registro)
    bt1.configure(bd=2,relief="ridge",bg="#efefef",fg="#000")
    bt1.place(relx=0.35,rely=0.50,relwidth=0.25,relheight=0.08)
    bt2=tk.Button(pantalla,text="Iniciar Sesion", command= iniciar_Sesion)
    bt2.configure(bd=2,relief="ridge",bg="#efefef",fg="#000")
    bt2.place(relx=0.35,rely=0.70,relwidth=0.25,relheight=0.08)

    pantalla.mainloop()

#--- parte de matias gauto ---#
def Registro():
    global nombre_entry
    global apellido_entry
    global contraseña_entry
    global usuario_entry
    global email_entry
    pantalla.withdraw()
    root=tk.Toplevel(pantalla)
    root.title("Login")
    root.geometry("500x500")
    
    root.configure(bg="#efefef")
    
    pantallita=tk.Frame(root)
    pantallita.configure(bd=3,relief="raised",bg="#4141DA")
    pantallita.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)
    
    label=tk.Label(pantallita,text="REGISTRO",font=("Times New Roman",20,"bold"),bd=1.5,relief='raised',bg="#fff",fg="#4141DA").pack(pady=12)    
    nombre_entry = tk.Entry(pantallita, fg='grey')
    nombre_entry.insert(0, 'Nombre:')
    nombre_entry.bind("<FocusIn>", on_focus_in)
    nombre_entry.bind("<FocusOut>", on_focus_out)
    nombre_entry.place(relx=0.08, rely=0.19,relheight=0.06)

    usuario_entry = tk.Entry(pantallita, fg='grey')
    usuario_entry.insert(0, 'Usuario:')
    usuario_entry.bind("<FocusIn>", on_focus_in2)
    usuario_entry.bind("<FocusOut>", on_focus_out2)
    usuario_entry.place(relx=0.08, rely=0.29,relheight=0.06)

    contraseña_entry = tk.Entry(pantallita, fg='grey')
    contraseña_entry.insert(0, 'Contraseña:')
    contraseña_entry.bind("<FocusIn>", on_focus_in3)
    contraseña_entry.bind("<FocusOut>", on_focus_out3)
    contraseña_entry.place(relx=0.08, rely=0.39,relheight=0.06)

    apellido_entry = tk.Entry(pantallita, fg='grey')
    apellido_entry.insert(0, 'Apellido:')
    apellido_entry.bind("<FocusIn>", on_focus_in4)
    apellido_entry.bind("<FocusOut>", on_focus_out4)
    apellido_entry.place(relx=0.55, rely=0.19,relheight=0.06)

    confirmar_entry = tk.Entry(pantallita, fg='grey')
    confirmar_entry.insert(0, 'Confirmar Usuario:')
    confirmar_entry.bind("<FocusIn>", on_focus_in5)
    confirmar_entry.bind("<FocusOut>", on_focus_out5)
    confirmar_entry.place(relx=0.55, rely=0.29,relheight=0.06)

    confirmar1_entry = tk.Entry(pantallita, fg='grey')
    confirmar1_entry.insert(0, 'Confirmar Contraseña:')
    confirmar1_entry.bind("<FocusIn>", on_focus_in6)
    confirmar1_entry.bind("<FocusOut>", on_focus_out6)
    confirmar1_entry.place(relx=0.55, rely=0.39,relheight=0.06)    

    email_entry = tk.Entry(pantallita, fg='grey')
    email_entry.insert(0, 'Email:')
    email_entry.bind("<FocusIn>", on_focus_in7)
    email_entry.bind("<FocusOut>", on_focus_out7)
    email_entry.place(relx=0.08, rely=0.53,relwidth=0.78,relheight=0.06)

    bt3=tk.Button(pantallita,text="Volver", command=lambda: volver_a_pantalla(root))
    bt3.configure(bd=2,relief="ridge",bg="#efefef",fg="#000")
    bt3.place(relx=0.13,rely=0.70,relwidth=0.25,relheight=0.08)
    bt4=tk.Button(pantallita,text="Registrarse", command=lambda:registrarUsuario())
    bt4.configure(bd=2,relief="ridge",bg="#efefef",fg="#000")
    bt4.place(relx=0.55,rely=0.70,relwidth=0.25,relheight=0.08)

#parte de Belenger
def registrarUsuario (): 
    nombre= nombre_entry.get()
    apellido= apellido_entry.get()
    usuario= usuario_entry.get()
    contraseña= contraseña_entry.get()
    email= email_entry.get()
    miConexion=pymysql.connect(host='Localhost',user='root',passwd='',db='usuarios')
    cur=miConexion.cursor()
    isertSql="Insert into tusuario (Nombre,Apellido,Usuario,Clave,Email) values(%s, %s, %s, %s, %s)"
    cur.execute(isertSql,(nombre,apellido,usuario,contraseña,email))
    miConexion.commit()
    miConexion.close()

def validaUsuarioPwd ():

    usuario=usuario1_entry.get()
    clave=contraseña1_entry.get()     
    miConexion=pymysql.connect(host='Localhost',user='root',passwd='',db='usuarios')
    cur=miConexion.cursor()
    selectSql="select Usuario,Clave from tusuario where Usuario=%s and Clave=%s"
    cur.execute(selectSql,(usuario,clave))
    if cur.rowcount==0 :
            messagebox.showinfo("Invalido","La contraseña y el usuario son incorectos.")
    else:
            messagebox.showinfo("Login correcto","Felicidades lograste entrar a tu cuenta")
    miConexion.close()
    root = tk.Tk()
    app = mo.CRUDApp(root)
    root.mainloop()



def iniciar_Sesion():
    global usuario1_entry
    global contraseña1_entry
    pantalla.withdraw()
    pantalla1 = tk.Toplevel(pantalla)
    pantalla1.geometry("500x500")
    pantalla1.title("Iniciar sesion")

    b2=tk.Frame(pantalla1)
    b2.configure(bd=3,relief="raised",bg="#4141DA")
    b2.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

    label=tk.Label(b2,text="INICIAR SESION",font=("Times New Roman",15,"bold"),bd=1.5,relief='raised',bg="#fff",fg="#4141DA").pack(pady=12)

    usuario1_entry = tk.Entry(b2, fg='grey')
    usuario1_entry.insert(0, 'Usuario:')
    usuario1_entry.bind("<FocusIn>", on_focus_in2)
    usuario1_entry.bind("<FocusOut>", on_focus_out2)
    usuario1_entry.place(relx=0.10, rely=0.25,relheight=0.06)

    contraseña1_entry = tk.Entry(b2, fg='grey')
    contraseña1_entry.insert(0, 'Contraseña:')
    contraseña1_entry.bind("<FocusIn>", on_focus_in3)
    contraseña1_entry.bind("<FocusOut>", on_focus_out3)
    contraseña1_entry.place(relx=0.10, rely=0.45,relheight=0.06)

    bt5=tk.Button(b2,text="Volver", command=lambda: volver_a_pantalla(pantalla1))
    bt5.configure(bd=2,relief="ridge",bg="#efefef",fg="#000")
    bt5.place(relx=0.13,rely=0.70,relwidth=0.25,relheight=0.08)
    bt6=tk.Button(b2,text="ingresar", command=lambda: validaUsuarioPwd ())
    bt6.configure(bd=2,relief="ridge",bg="#efefef",fg="#000")
    bt6.place(relx=0.55,rely=0.70,relwidth=0.25,relheight=0.08)

def volver_a_pantalla (pantalla_a_ocultar):
    pantalla_a_ocultar.withdraw()
    pantalla.deiconify()
    
pantalla_inicial()