# import mysql.connector
# import tkinter as tk
# from ParaImagenes import frames_imagenes

# # Función para conectar a la base de datos
# def connect_to_database():
#     try:
#         cnx = mysql.connector.connect(user='nuevo_usuario', password='contraseña_segura',
#                                       host='localhost', database='base_datos_definitiva')
#         print("Conexión a la base de datos exitosa.")
#         return cnx
#     except mysql.connector.Error as err:
#         print(f"Error al conectarse a MySQL: {err}")
#         return None

# # Función para insertar los valores en la base de datos
# def insert_data(cnx, nombre, apellido, usuario, confirmar_usuario, contraseña, confirmar_contraseña, email):
#     cursor = cnx.cursor()
#     insert_query = "INSERT INTO usuarios (nombre, apellido, usuario, confirmar_usuario, contraseña, confirmar_contraseña, email) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#     data = (nombre, apellido, usuario, confirmar_usuario, contraseña, confirmar_contraseña, email)
#     try:
#         cursor.execute(insert_query, data)
#         cnx.commit()
#         print("Datos insertados exitosamente.")
#     except mysql.connector.Error as err:
#         print(f"Error al insertar datos: {err}")
#     cursor.close()

# # Creamos la ventana
# ventana = tk.Tk()
# fm_i = frames_imagenes(ventana, 420, 560)
# fm_i.centrar_ventana()
# ventana.title("Registro")

# # Conectar a la base de datos
# cnx = connect_to_database()

# # Función para leer imágenes
# def imagen(i):
#     camino_imagen = [
#         "login_intento-legible.8/imagenes/nombre.png",
#         "login_intento-legible.8/imagenes/apellido.png",
#         "login_intento-legible.8/imagenes/usuario.png",
#         "login_intento-legible.8/imagenes/confirmacion_redonda.png",
#         "login_intento-legible.8/imagenes/contraseña.png",
#         "login_intento-legible.8/imagenes/confirmacion_redonda.png",
#         "login_intento-legible.8/imagenes/email.png"
#     ]
#     img = fm_i.leer_imagen(camino_imagen[i], (20, 20))
#     return img

# # Función para obtener los valores de las entradas y guardarlos en la base de datos
# def obtener_valores(var_entry1, var_entry2, var_entry3, var_entry4, var_entry5, var_entry6, var_entry7):
#     valor_entry1 = var_entry1.get()
#     valor_entry2 = var_entry2.get()
#     valor_entry3 = var_entry3.get()
#     valor_entry4 = var_entry4.get()
#     valor_entry5 = var_entry5.get()
#     valor_entry6 = var_entry6.get()
#     valor_entry7 = var_entry7.get()
    
#     print(f"Valor del Entry 1: {valor_entry1}")
#     print(f"Valor del Entry 2: {valor_entry2}")
#     print(f"Valor del Entry 3: {valor_entry3}")
#     print(f"Valor del Entry 4: {valor_entry4}")
#     print(f"Valor del Entry 5: {valor_entry5}")
#     print(f"Valor del Entry 6: {valor_entry6}")
#     print(f"Valor del Entry 7: {valor_entry7}")
    
#     # Insertar datos en la base de datos
#     insert_data(cnx, valor_entry1, valor_entry2, valor_entry3, valor_entry4, valor_entry5, valor_entry6, valor_entry7)

# # Función principal
# def main():
#     frame_titulo = tk.Frame(ventana, bg="#f0f0f0", width=420, height=100)
#     frame_titulo.pack(side=tk.TOP, fill="x")
#     frame_titulo.pack_propagate(False)

#     label_titulo = tk.Label(frame_titulo, text="Registro", font=("Times", 48), bg="#f0f0f0", fg="#226EAD")
#     label_titulo.pack(expand=False, pady=10)

#     frame_restante = tk.Frame(ventana, bg="#f0f0f0", width=420, height=460)
#     frame_restante.pack(side=tk.BOTTOM, fill="both")
#     frame_restante.pack_propagate(False)

#     var_entry1 = tk.StringVar()
#     var_entry2 = tk.StringVar()
#     var_entry3 = tk.StringVar()
#     var_entry4 = tk.StringVar()
#     var_entry5 = tk.StringVar()
#     var_entry6 = tk.StringVar()
#     var_entry7 = tk.StringVar()

#     # Primer frame
#     new_frame = fm_i.crear_frame_auxiliar(frame_restante, 50)
#     img = imagen(0)
#     label_img = tk.Label(new_frame, image=img)
#     label_img.configure(bg="#f0f0f0")
#     label_img.place(relx=0.01, rely=0.0)
#     label1 = tk.Label(new_frame, text="Nombre:", font=("Times", 12), fg="#666a88", bg="#f0f0f0")
#     label1.place(relx=0.06, rely=0.0)
#     entry1 = tk.Entry(new_frame, textvariable=var_entry1, font=("Times", 11), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
#     entry1.place(relx=0.02, rely=0.5, relwidth=0.95)

#     # Segundo frame
#     new_frame2 = fm_i.crear_frame_auxiliar(frame_restante, 50)
#     img2 = imagen(1)
#     label_img2 = tk.Label(new_frame2, image=img2)
#     label_img2.configure(bg="#f0f0f0")
#     label_img2.place(relx=0.01, rely=0.0)
#     label2 = tk.Label(new_frame2, text="Apellido:", font=("Times", 12), fg="#666a88", bg="#f0f0f0")
#     label2.place(relx=0.06, rely=0.0)
#     entry2 = tk.Entry(new_frame2, textvariable=var_entry2, font=("Times", 11), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
#     entry2.place(relx=0.02, rely=0.5, relwidth=0.95)

#     # Tercer frame
#     new_frame3 = fm_i.crear_frame_auxiliar(frame_restante, 50)
#     img3 = imagen(2)
#     label_img3 = tk.Label(new_frame3, image=img3)
#     label_img3.configure(bg="#f0f0f0")
#     label_img3.place(relx=0.01, rely=0.0)
#     label3 = tk.Label(new_frame3, text="Usuario:", font=("Times", 12), fg="#666a88", bg="#f0f0f0")
#     label3.place(relx=0.06, rely=0.0)
#     entry3 = tk.Entry(new_frame3, textvariable=var_entry3, font=("Times", 11), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
#     entry3.place(relx=0.02, rely=0.5, relwidth=0.95)

#     # Cuarto frame
#     new_frame4 = fm_i.crear_frame_auxiliar(frame_restante, 50)
#     img4 = imagen(3)
#     label_img4 = tk.Label(new_frame4, image=img4)
#     label_img4.configure(bg="#f0f0f0")
#     label_img4.place(relx=0.01, rely=0.0)
#     label4 = tk.Label(new_frame4, text="Confirmar usuario:", font=("Times", 12), fg="#666a88", bg="#f0f0f0")
#     label4.place(relx=0.057, rely=0.0)
#     entry4 = tk.Entry(new_frame4, textvariable=var_entry4, font=("Times", 11), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
#     entry4.place(relx=0.02, rely=0.5, relwidth=0.95)

#     # Quinto frame
#     new_frame5 = fm_i.crear_frame_auxiliar(frame_restante, 50)
#     img5 = imagen(4)
#     label_img5 = tk.Label(new_frame5, image=img5)
#     label_img5.configure(bg="#f0f0f0")
#     label_img5.place(relx=0.01, rely=0.0)
#     label5 = tk.Label(new_frame5, text="Contraseña:", font=("Times", 12), fg="#666a88", bg="#f0f0f0")
#     label5.place(relx=0.06, rely=0.0)
#     entry5 = tk.Entry(new_frame5, textvariable=var_entry5, font=("Times", 11), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
#     entry5.place(relx=0.02, rely=0.5, relwidth=0.95)

#     # Sexto frame
#     new_frame6 = fm_i.crear_frame_auxiliar(frame_restante, 50)
#     img6 = imagen(5)
#     label_img6 = tk.Label(new_frame6, image=img6)
#     label_img6.configure(bg="#f0f0f0")
#     label_img6.place(relx=0.01, rely=0.0)
#     label6 = tk.Label(new_frame6, text="Confirmar contraseña:", font=("Times", 12), fg="#666a88", bg="#f0f0f0")
#     label6.place(relx=0.06, rely=0.0)
#     entry6 = tk.Entry(new_frame6, textvariable=var_entry6, font=("Times", 11), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
#     entry6.place(relx=0.02, rely=0.5, relwidth=0.95)

#     # Séptimo frame
#     new_frame7 = fm_i.crear_frame_auxiliar(frame_restante, 50)
#     img7 = imagen(6)
#     label_img7 = tk.Label(new_frame7, image=img7)
#     label_img7.configure(bg="#f0f0f0")
#     label_img7.place(relx=0.013, rely=0.0)
#     label7 = tk.Label(new_frame7, text="Email:", font=("Times", 12), fg="#666a88", bg="#f0f0f0")
#     label7.place(relx=0.067, rely=0.0)
#     entry7 = tk.Entry(new_frame7, textvariable=var_entry7, font=("Times", 11), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
#     entry7.place(relx=0.02, rely=0.5, relwidth=0.95)

#     # Función para obtener los valores , y que no se ejecute automaticamente en el boton sino qu epueda pasarle parametros y cuando la llame sin parentesis se ejecute solo cuando presione el boton
#     def obt_val():
#         obtener_valores(var_entry1, var_entry2, var_entry3, var_entry4, var_entry5, var_entry6, var_entry7)

#     bt_guardar = tk.Button(frame_restante, text="Crear usuario", width=400, bg="#226EAD", fg="#f0f0f0", font=("Helvetica", 14), bd=0, command=obt_val)
#     bt_guardar.pack(pady=25, padx=7)
#     ventana.mainloop()

# # Llamar a la función principal
# main()

# # Cerrar la conexión a la base de datos al cerrar la aplicación
# if cnx:
#     cnx.close()
#     print("Conexión a la base de datos cerrada.")
