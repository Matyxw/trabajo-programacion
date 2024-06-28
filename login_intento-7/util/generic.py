from PIL import ImageTk, Image
import tkinter as tk
#vamos a dar la ruta y el tamaño de la imagen
def leer_imagen (path,size):
        return ImageTk.PhotoImage(Image.open(path).resize(size,Image.LANCZOS))

#centramos la ventana
def centrar_ventana(ventana,aplicacion_ancho,aplicacion_largo):
        pantall_ancho=ventana.winfo_screenwidth()
        pantall_largo=ventana.winfo_screenheight()
        x=int((pantall_largo/2) - (pantall_ancho/2))
        y=int((pantall_ancho/2) - (pantall_largo/2))
        return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")