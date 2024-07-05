# esto dsp va ser de donde conecte todo, por el momento es un intento con pruebas mias na mas
# import tkinter as tk
# from PIL import Image,ImageTk


# class ElFrame:
#     #creamos el frame donde va ir dsp la imagen 
#     def __init__(self,aux):
#         self.frame=tk.Frame(aux,width=300,height=500,bg="red")
#         self.frame.pack_propagate(False) 
        
#     #esto sirve para luego cuando le pasamos la posicion en parametros se ubique
#     def colocar(self,x,y):
#         self.frame.place(x=x,y=y)
        
#     def colocarImg(self,imagensita):
#         self.image=Image.open(imagensita)
#         self.photo=ImageTk.PhotoImage(self.image)
#         self.label=tk.Label(self.frame,image=self.photo)
        
#         self.label.place(x=x,y=y)
        
#     def colocarIzquierda(self):
#         self.frame.pack(side=tk.LEFT)
        
    
# #creamos la ventana
# def window(ancho,alto):
#     root=tk.Tk()
#     root.title("Ventana principal")
#     root.geometry(f"{ancho}x{alto}")
#     frameLogo=ElFrame(root)
#     frameLogo.colocar(0,0)
#     frameLogo.colocarImg("imagenes/imagensita.png")
#     # frame=tk.Frame(root,bg="#f00",bd=5,relief="groove")
#     # frame.place(x=0,y=0,width=350,relheight=1.0)

#     root.mainloop()

# window(800,500)

