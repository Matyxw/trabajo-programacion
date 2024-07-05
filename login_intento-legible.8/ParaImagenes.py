from PIL import ImageTk,Image
import tkinter as tk

#creamos la clase para luego importarla entera 
class frames_imagenes:
    #usamos el metodo init y le asignamos los valores para que despues se pueda trabajar 
    def __init__(self,ventana,aplicacion_ancho,aplicacion_largo):
        self.ventana=ventana
        self.aplicacion_ancho=aplicacion_ancho        
        self.aplicacion_largo=aplicacion_largo

    #centramos la ventana, los argumentos deberian ser entonces:root,el width y el height
    def centrar_ventana(self):
            pantalla_ancho=self.ventana.winfo_screenwidth()
            pantalla_largo=self.ventana.winfo_screenheight()
            x=int((pantalla_ancho/2) - (self.aplicacion_ancho/2))
            y=int((pantalla_largo/2) - (self.aplicacion_largo/2))
            self.ventana.geometry(f"{self.aplicacion_ancho}x{self.aplicacion_largo}+{x}+{y}")

    #damos la ruta y el tamaño de la imagen para luego con un metodo como pack o place ubicarla
    def leer_imagen(self,ruta,tamaño):
        return ImageTk.PhotoImage(Image.open(ruta).resize(tamaño,Image.LANCZOS))
