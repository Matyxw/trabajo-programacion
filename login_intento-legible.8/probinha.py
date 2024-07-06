import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Botón Moderno con ttk")
root.geometry("300x200")

# Crear un estilo para el botón
style = ttk.Style()
style.theme_use('clam')  # Usar el tema 'clam' como base

# Configurar el estilo del botón
style.configure('Modern.TButton',
                font=('Helvetica', 12, 'bold'),
                foreground='#ffffff',
                background='#4CAF50',
                borderwidth=0,
                padding=10)
style.map('Modern.TButton',
          foreground=[('pressed', '#ffffff'), ('active', '#4CAF50')],
          background=[('pressed', '!disabled', '#388E3C'), ('active', '#81C784')],
          relief=[('pressed', 'flat'), ('!pressed', 'flat')])

# Función que se ejecutará cuando se haga clic en el botón
def on_button_click():
    print("¡El botón ha sido clicado!")

# Crear el botón usando ttk y aplicar el estilo
ttk_button = ttk.Button(root, text="Haz clic aquí", command=on_button_click, style='Modern.TButton')

# Colocar el botón en la ventana
ttk_button.pack(pady=20)

# Iniciar el bucle principal de la ventana
root.mainloop()
