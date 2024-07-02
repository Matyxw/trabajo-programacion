import tkinter as tk
from tkinter import messagebox
import pymysql

# Conectar a la base de datos MySQL
def connect_db():
    try:
        return pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='cruddef'
        )
    except pymysql.MySQLError as err:
        messagebox.showerror("Error", f"Error de conexión: {err}")
        return None

def insertar_usuario(nombre, apellido, grupo, curso):
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO alumnos (nombre, apellido, grupo, curso) VALUES (%s, %s, %s, %s)", (nombre, apellido, grupo, curso))
        conn.commit()
        conn.close()
        messagebox.showinfo("Información", "Usuario insertado con éxito")

def obtener_usuarios():
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM alumnos")
        usuarios = cursor.fetchall()
        conn.close()
        return usuarios

def actualizar_usuario(id, nombre, apellido, grupo, curso):
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("UPDATE alumnos SET nombre=%s, apellido=%s, grupo=%s, curso=%s WHERE id=%s", (nombre, apellido, grupo, curso, id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Información", "Usuario actualizado con éxito")

def eliminar_usuario(id):
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM alumnos WHERE id=%s", (id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Información", "Usuario eliminado con éxito")

class CRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación CRUD")

        # Etiquetas y campos de entrada
        self.nombre_label = tk.Label(root, text="Nombre")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.pack()

        self.apellido_label = tk.Label(root, text="Apellido")
        self.apellido_label.pack()
        self.apellido_entry = tk.Entry(root)
        self.apellido_entry.pack()

        self.grupo_label = tk.Label(root, text="Grupo")
        self.grupo_label.pack()
        self.grupo_entry = tk.Entry(root)
        self.grupo_entry.pack()

        self.curso_label = tk.Label(root, text="Curso")
        self.curso_label.pack()
        self.curso_entry = tk.Entry(root)
        self.curso_entry.pack()

        # Botones
        self.insertar_button = tk.Button(root, text="Insertar", command=self.insertar_usuario)
        self.insertar_button.pack()

        self.actualizar_button = tk.Button(root, text="Actualizar", command=self.actualizar_usuario)
        self.actualizar_button.pack()

        self.eliminar_button = tk.Button(root, text="Eliminar", command=self.eliminar_usuario)
        self.eliminar_button.pack()

        self.listar_button = tk.Button(root, text="Listar Usuarios", command=self.listar_usuarios)
        self.listar_button.pack()

        self.resultados_text = tk.Text(root)
        self.resultados_text.pack()

    def insertar_usuario(self):
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        grupo = self.grupo_entry.get()
        curso = self.curso_entry.get()
        insertar_usuario(nombre, apellido, grupo, curso)
        self.listar_usuarios()

    def actualizar_usuario(self):
        id = self.obtener_id_seleccionado()
        if id is not None:
            nombre = self.nombre_entry.get()
            apellido = self.apellido_entry.get()
            grupo = self.grupo_entry.get()
            curso = self.curso_entry.get()
            actualizar_usuario(id, nombre, apellido, grupo, curso)
            self.listar_usuarios()

    def eliminar_usuario(self):
        id = self.obtener_id_seleccionado()
        if id is not None:
            eliminar_usuario(id)
            self.listar_usuarios()

    def listar_usuarios(self):
        usuarios = obtener_usuarios()
        self.resultados_text.delete('1.0', tk.END)
        for usuario in usuarios:
            self.resultados_text.insert(tk.END, f"ID: {usuario[0]}, Nombre: {usuario[1]}, Apellido: {usuario[2]}, Grupo: {usuario[3]}, Curso: {usuario[4]}\n")

    def obtener_id_seleccionado(self):
        try:
            seleccionado = self.resultados_text.get(tk.SEL_FIRST, tk.SEL_LAST)
            return int(seleccionado.split(",")[0].split(":")[1].strip())
        except:
            messagebox.showerror("Error", "Por favor, seleccione un usuario de la lista.")
            return None

if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDApp(root)
    root.mainloop()
