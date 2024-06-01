import tkinter as tk
import  customtkinter as ctk
import ctypes as ct
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import ttk
from PIL import Image, ImageTk
import datetime as dt

ctk.set_appearance_mode("light")








def comprar_tiquete():
    ventana_inicio.destroy()
    ventana_compra = ctk.CTk()
    ventana_compra.title("Compra de tiquetes")
    ventana_compra.geometry("500x500+250+80")
    
    label_titulo = ctk.CTkLabel(ventana_compra, text="Comprar Ticket", font=("Arial", 20))
    label_origen = ctk.CTkLabel(ventana_compra, text="Origen:", font=("Arial", 15))
    lugares_origuen= ctk.CTkComboBox(ventana_compra, values=["Bogota", "Medellin", "Cali", "Barranquilla", "Cartagena", "Santa Marta", "San Andres", "Leticia", "Bucaramanga", "Pereira", "Armenia", "Manizales", "Cucuta", "Pasto", "Popayan", "Neiva", "Villavicencio", "Monteria", "Riohacha", "Valledupar", "Tunja", "Yopal" ], font=("Arial", 15),border_color="purple")
    label_destino = ctk.CTkLabel(ventana_compra, text="Destino:", font=("Arial", 15))
    lugares_destino= ctk.CTkComboBox(ventana_compra, values=["Bogota", "Medellin", "Cali", "Barranquilla", "Cartagena", "Santa Marta", "San Andres", "Leticia", "Bucaramanga", "Pereira", "Armenia", "Manizales", "Cucuta", "Pasto", "Popayan", "Neiva", "Villavicencio", "Monteria", "Riohacha", "Valledupar", "Tunja", "Yopal" ], font=("Arial", 15),border_color="purple")
    label_fecha_salida = ctk.CTkLabel(ventana_compra, text="Fecha de salida:", font=("Arial", 15))
    entry_fecha_salida = ctk.CTkEntry(ventana_compra, font=("Arial", 15),border_color="purple")
    label_fecha_regreso = ctk.CTkLabel(ventana_compra, text="Fecha de regreso:", font=("Arial", 15))
    entry_fecha_regreso = ctk.CTkEntry(ventana_compra, font=("Arial", 15),border_color="purple")
    label_numero_pasajeros = ctk.CTkLabel(ventana_compra, text="Numero de pasajeros:", font=("Arial", 15))
    entry_numero_pasajeros = ctk.CTkEntry(ventana_compra, font=("Arial", 15),border_color="purple")
    boton_buscar= ctk.CTkButton(ventana_compra,text="Buscar Vuelo", font=("arial",15),fg_color="purple",corner_radius=32 )

    label_titulo.place(relx=0.5, rely=0.1, anchor="center")
    label_origen.place(relx=0.1, rely=0.3, anchor="center")
    lugares_origuen.place(relx=0.3, rely=0.3, anchor="center")
    label_destino.place(relx=0.6, rely=0.3, anchor="center")
    lugares_destino.place(relx=0.9, rely=0.3, anchor="center")
    label_fecha_salida.place(relx=0.1, rely=0.4, anchor="center")
    entry_fecha_salida.place(relx=0.3, rely=0.4, anchor="center")
    label_fecha_regreso.place(relx=0.6, rely=0.4, anchor="center")
    entry_fecha_regreso.place(relx=0.9, rely=0.4, anchor="center")
    label_numero_pasajeros.place(relx=0.5, rely=0.5, anchor="center")
    entry_numero_pasajeros.place(relx=0.5, rely=0.6, anchor="center")
    boton_buscar.place(relx=0.5,rely=0.7,anchor= "center")
    
    ventana_compra.mainloop()
    
    
    

def condiciones_registro(ventana_registro, entry_nombre, entry_apellido, combo_genero, entry_nacionalidad, entry_documento, entry_fecha_nacimiento, entry_correo, entry_numero_telefono, combo_asistencia):
    if entry_nombre.get()=="" or entry_apellido.get()=="" or combo_genero.get()=="" or entry_nacionalidad.get()=="" or entry_documento.get()=="" or entry_fecha_nacimiento.get()=="" or entry_correo.get()=="" or entry_numero_telefono.get()=="" or combo_asistencia.get()=="" :
        messagebox.showerror("Error","Por favor llena todos los campos")
        
    elif entry_nombre.get().isdigit() or entry_apellido.get().isdigit():
        messagebox.showerror("Error","Los campos de nombre y apellido no deben contener números")
        
    elif entry_nacionalidad.get().isdigit():
        messagebox.showerror("Error","El campo de nacionalidad no debe contener números")
        
    dominios = [".com", ".es", ".co", ".net", ".org", ".gov", ".edu"]
    if entry_correo.get().find("@")==-1 or not any(dominio in entry_correo.get() for dominio in dominios):
        messagebox.showerror("Error","El correo debe tener un formato válido")
    
    try:
        dt.datetime.strptime(entry_fecha_nacimiento.get(), "%d/%m/%Y")
    except ValueError:
        messagebox.showerror("Error","La fecha debe tener el formato dd/mm/aaaa")
        
    try:
        int(entry_documento.get())
        int(entry_numero_telefono.get())
    except ValueError:
        messagebox.showerror("Error","Por favor ingrese datos válidos")
    
    # if entry_nombre.get()=="" or entry_apellido.get()=="" or combo_genero.get()=="" or entry_nacionalidad.get()=="" or entry_documento.get()=="" or entry_fecha_nacimiento.get()=="" or entry_correo.get()=="" or entry_numero_telefono.get()=="" or combo_asistencia.get()=="":
    #     ctk.messagebox.showerror("Error", "Por favor llena todos los campos")
        
    # elif entry_nombre.get()== int or entry_apellido.get()== int or entry_nacionalidad.get()== int :
    #     ctk.messagebox.showerror("Error","Por fabor ingrese datos validos")
        
    # elif entry_documento.get()== str or entry_numero_telefono.get()== str: 
    #     ctk.messagebox.showerror("Error","Por favor ingrese datos validos")
        
# try:
#         # Intenta convertir la fecha a un objeto datetime
#         datetime.datetime.strptime(birthday, '%d/%m/%Y')
#     except ValueError:
#         # Si la conversión falla, muestra un mensaje de error
#         mb.showerror("Error", "La fecha debe tener el formato dd/mm/aaaa")
#         return

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
    
    boton_enviar= ctk.CTkButton(ventana_registro,text="Enviar Datos", font=("arial",15),fg_color="purple",corner_radius=32, command= lambda: condiciones_registro(ventana_registro, entry_nombre, entry_apellido, combo_genero, entry_nacionalidad, entry_documento, entry_fecha_nacimiento, entry_correo, entry_numero_telefono, combo_asistencia))
    
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


boton_registro = ctk.CTkButton(ventana_inicio, text="Registro",fg_color="purple" ,corner_radius=32,command=ventanaregistro)
boton_comprar = ctk.CTkButton(ventana_inicio, text="Comprar tiquete",fg_color="purple",corner_radius=32,command=comprar_tiquete)
boton_checkin = ctk.CTkButton(ventana_inicio, text="Realizar Check-in",fg_color="purple",corner_radius=32)
boton_ver_vuelos = ctk.CTkButton(ventana_inicio, text="Ver nuestros vuelos disponibles",fg_color="purple",corner_radius=32)

#posicion de los elementos
label_titulo.place(x=200, y=50)
label_logo.place(x=230, y=120)
boton_registro.place(x=200, y=300)
boton_comprar.place(x=200, y=350)
boton_checkin.place(x=200, y=400)
boton_ver_vuelos.place(x=165, y=450)




ventana_inicio.mainloop()
