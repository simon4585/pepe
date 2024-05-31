import tkinter as tk
import  customtkinter as ctk
import ctypes as ct
from tkinter import PhotoImage
from tkinter import ttk
from PIL import Image, ImageTk

ctk.set_appearance_mode("light")


def ventanaregistro():
    ventana_inicio.destroy()
    ventana_registro = ctk.CTk()
    ventana_registro.title("Registro")
    ventana_registro.geometry("1200x1200+250+80")
    
    
    label_titulo = ctk.CTkLabel(ventana_registro, text="Registro en Stellar Airways", font=("Arial", 20))
    label_texto = ctk.CTkLabel(ventana_registro, text="Por favor ingresa tus datos", font=("Arial", 15))
    label_nombre = ctk.CTkLabel(ventana_registro, text="Primer nombre:", font=("Arial", 15))
    entry_nombre = ctk.CTkEntry(ventana_registro, font=("Arial", 15),border_color="purple",border_width=2)
    label_apellido = ctk.CTkLabel(ventana_registro, text="Primer apellido:", font=("Arial", 15))
    entry_apellido = ctk.CTkEntry(ventana_registro, font=("Arial", 15),border_color="purple")
    label_genero = ctk.CTkLabel(ventana_registro, text="Genero:", font=("Arial", 15))
    combo_genero = ctk.CTkComboBox(ventana_registro, values=["Masculino", "Femenino", "Otro"], font=("Arial", 15),border_color="purple")
    label_nacionalidad = ctk.CTkLabel(ventana_registro, text="Nacionalidad:", font=("Arial", 15))
    entry_nacionalidad = ctk.CTkEntry(ventana_registro, font=("Arial", 15),border_color="purple")
    numero_documento = ctk.CTkLabel(ventana_registro, text="Numero de documento:", font=("Arial", 15))
    entry_documento = ctk.CTkEntry(ventana_registro, font=("Arial", 15),border_color="purple")
    label_fecha_nacimiento = ctk.CTkLabel(ventana_registro, text="Fecha de nacimiento:", font=("Arial", 15))
    entry_fecha_nacimiento = ctk.CTkEntry(ventana_registro, font=("Arial", 15),border_color="purple")
    label_correo = ctk.CTkLabel(ventana_registro, text="Correo electronico:", font=("Arial", 15))
    entry_correo = ctk.CTkEntry(ventana_registro, font=("Arial", 15),border_color="purple")
    label_numero_telefono = ctk.CTkLabel(ventana_registro, text="Numero de telefono:", font=("Arial", 15))
    entry_numero_telefono = ctk.CTkEntry(ventana_registro, font=("Arial", 15),border_color="purple")
    label_asistencia = ctk.CTkLabel(ventana_registro, text="¿Necesitas asistencia especial?", font=("Arial", 15))
    combo_asistencia = ctk.CTkComboBox(ventana_registro, values=["Si", "No"], font=("Arial", 15),border_color="purple")
    
    boton_enviar= ctk.CTkButton(ventana_registro,text="Enviar Datos", font=("arial",15),fg_color="purple",corner_radius=32 )
    
    label_titulo.place(relx=0.5, rely=0.1, anchor="center")
    label_texto.place(relx=0.5, rely=0.2, anchor="center")
    label_nombre.place(relx=0.1, rely=0.3, anchor="center")
    entry_nombre.place(relx=0.3, rely=0.3, anchor="center")
    label_apellido.place(relx=0.1, rely=0.4, anchor="center")
    entry_apellido.place(relx=0.3, rely=0.4, anchor="center")
    label_genero.place(relx=0.1, rely=0.5, anchor="center")
    combo_genero.place(relx=0.3, rely=0.5, anchor="center")
    label_nacionalidad.place(relx=0.1, rely=0.6, anchor="center")
    entry_nacionalidad.place(relx=0.3, rely=0.6, anchor="center")
    numero_documento.place(relx=0.6, rely=0.6, anchor="center")
    entry_documento.place(relx=0.9, rely=0.6, anchor="center")
    label_fecha_nacimiento.place(relx=0.6, rely=0.3, anchor="center")
    entry_fecha_nacimiento.place(relx=0.9, rely=0.3, anchor="center")
    label_correo.place(relx=0.6, rely=0.4, anchor="center")
    entry_correo.place(relx=0.9, rely=0.4, anchor="center")
    label_numero_telefono.place(relx=0.6, rely=0.5, anchor="center")
    entry_numero_telefono.place(relx=0.9, rely=0.5, anchor="center")
    label_asistencia.place(relx=0.5, rely=0.7, anchor="center")
    combo_asistencia.place(relx=0.5, rely=0.8, anchor="center")
    boton_enviar.place(relx=0.5,rely=0.85,anchor= "center")
    
    ventana_registro.mainloop()













ventana_inicio = ctk.CTk()
ventana_inicio.title("Aerolinea Stellar Airways")
ventana_inicio.geometry("500x500")

label_titulo = ctk.CTkLabel(ventana_inicio, text="Stellar Airways", font=("Arial", 20),text_color="purple")

#se colocal la imagen del logo
label_logo= Image.open("logoaerolinea-removebg-preview.png")
label_logo=label_logo.resize((200,200))
photo=ImageTk.PhotoImage(label_logo)
label_logo=tk.Label(ventana_inicio, image=photo)
label_logo.image=photo


boton_registro = ctk.CTkButton(ventana_inicio, text="Registro", command=ventanaregistro,fg_color="purple" ,corner_radius=32 )
boton_inicio = ctk.CTkButton(ventana_inicio, text="Iniciar",fg_color="purple",corner_radius=32)


#posicion de los elementos
label_titulo.place(x=200, y=50)
label_logo.place(x=230, y=120)
boton_registro.place(x=200, y=300)
boton_inicio.place(x=200, y=350)




ventana_inicio.mainloop()
