import tkinter as tk
import  customtkinter as ctk
import ctypes as ct
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import ttk
from PIL import Image, ImageTk
import datetime as dt
import csv

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
    
    
    

def condiciones_registro(ventana_registro, entry_nombre, entry_apellido, combo_genero, entry_nacionalidad, entry_documento, entry_fecha_nacimiento, entry_correo, entry_numero_telefono,valor_seleccionado):
    if entry_nombre.get()=="" or entry_apellido.get()=="" or combo_genero.get()=="" or entry_nacionalidad.get()=="" or entry_documento.get()=="" or entry_fecha_nacimiento.get()=="" or entry_correo.get()=="" or entry_numero_telefono.get()=="":
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
        
    guardar_datos(entry_nombre, entry_apellido, combo_genero, entry_nacionalidad, entry_documento, entry_fecha_nacimiento, entry_correo, entry_numero_telefono,valor_seleccionado)
  

def guardar_datos(entry_nombre, entry_apellido, combo_genero, entry_nacionalidad, entry_documento, entry_fecha_nacimiento, entry_correo, entry_numero_telefono,valor_seleccionado):
    documento = entry_documento.get()
    
    # Leer el archivo CSV y verificar si el documento ya existe
    with open("datos_usuarios.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and len(row) >= 5 and row[4] == documento:  # Si el documento ya existe, mostrar un mensaje de error y salir de la función
                messagebox.showerror("Error", "El documento ya existe en la base de datos")
                return
            
    messagebox.showinfo("informacion","Datos guardados exitosamente")
    
    # Si el documento no existe, agregar el nuevo registro
    with open("datos_usuarios.csv", "a") as f:
        f.write(f"\n{entry_nombre.get()},{entry_apellido.get()},{combo_genero.get()},{entry_nacionalidad.get()},{documento},{entry_fecha_nacimiento.get()},{entry_correo.get()},{entry_numero_telefono.get()},{valor_seleccionado.get()}\n")

    
    
def ventanaregistro():
    ventana_inicio.destroy()
    ventana_registro = ctk.CTk()
    ventana_registro.title("Registro")
    #poner la ventana en pantalla completa
    ventana_registro.geometry("1800x800+0+0")
    
    
    
    label_titulo = ctk.CTkLabel(ventana_registro, text="Registro en Stellar Airways", font=("Eras Demi ITC", 20),text_color="purple")
    label_texto = ctk.CTkLabel(ventana_registro, text="Por favor ingresa tus datos", font=("Eras Demi ITC", 15))
    label_nombre = ctk.CTkLabel(ventana_registro, text="Primer nombre:", font=("Arial", 15))
    entry_nombre = ctk.CTkEntry(ventana_registro, font=("Arial", 15),border_color="purple",border_width=2)
    label_apellido = ctk.CTkLabel(ventana_registro, text="Primer apellido:", font=("Arial", 15))
    entry_apellido = ctk.CTkEntry(ventana_registro, font=("Arial", 15),border_color="purple")
    label_genero = ctk.CTkLabel(ventana_registro, text="Genero:", font=("Arial", 15))
    combo_genero = ctk.CTkComboBox(ventana_registro, values=["Masculino", "Femenino", "Otro"], font=("Arial", 15),button_color="purple",border_color="purple",button_hover_color="purple4")
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
    
    boton_enviar= ctk.CTkButton(ventana_registro,text="Enviar Datos", font=("arial",15),fg_color="purple",corner_radius=32,hover_color="purple4",command= lambda: condiciones_registro(ventana_registro, entry_nombre, entry_apellido, combo_genero, entry_nacionalidad, entry_documento, entry_fecha_nacimiento, entry_correo, entry_numero_telefono,valor_seleccionado))
    
    label_titulo.place(x=620, y=40)
    label_texto.place(x=650, y=80)
    
    label_nombre.place(x=300, y=150)
    entry_nombre.place(x=500, y=150)
    label_apellido.place(x=300, y=200)
    entry_apellido.place(x=500, y= 200)
    label_genero.place(x=300, y=250)
    combo_genero.place(x=500, y=250)
    label_nacionalidad.place(x=300, y=300)
    entry_nacionalidad.place(x=500, y=300)
    
    numero_documento.place(x=800, y=150)
    entry_documento.place(x=1000, y=150)
    label_fecha_nacimiento.place(x=800, y=200)
    entry_fecha_nacimiento.place(x=1000, y=200)
    label_correo.place(x=800, y=250)
    entry_correo.place(x=1000, y=250)
    label_numero_telefono.place(x=800, y=300)
    entry_numero_telefono.place(x=1000, y=300)
    
    valor_seleccionado = tk.StringVar()

    # Crea los botones de radio
    radio1 = ctk.CTkRadioButton(ventana_registro, text="SI",fg_color="purple" ,variable=valor_seleccionado, value="SI")
    radio2 = ctk.CTkRadioButton(ventana_registro, text="NO",fg_color="purple" ,variable=valor_seleccionado, value="NO")

    # Posiciona los botones de radio
    radio1.place(x=650,y=410)
    radio2.place(x=730,y=410)
    
    
    
    label_asistencia.place(x=610, y=360)
    
    
    boton_enviar.place(x=640,y=470)
    
    ventana_registro.mainloop()










ventana_inicio = ctk.CTk()
ventana_inicio.title("Aerolinea Stellar Airways")
ventana_inicio.geometry("700x500+500+220")

label_titulo = ctk.CTkLabel(ventana_inicio, text="Stellar Airways", font=("Eras Demi ITC", 30),text_color="purple")

#se colocal la imagen del logo
label_logo= Image.open("logoNuevo.png")
label_logo=label_logo.resize((410,625))
photo=ImageTk.PhotoImage(label_logo)
label_logo=tk.Label(ventana_inicio, image=photo)
label_logo.image=photo

#se crea un frame para los botones
frame_botones = ctk.CTkFrame(ventana_inicio,fg_color="white",corner_radius=32,width=300, height=400, border_color="purple",border_width=3)
frame_botones.place(x=360, y=70)


#se crean los botones
boton_registro = ctk.CTkButton(frame_botones, text="Registro",fg_color="purple" ,border_color="black",border_width=2,corner_radius=32,hover_color="purple4",command=ventanaregistro)
boton_comprar = ctk.CTkButton(frame_botones, text="Comprar tiquete",fg_color="purple",border_color="black",border_width=2,corner_radius=32,hover_color="purple4",command=comprar_tiquete)
boton_checkin = ctk.CTkButton(frame_botones, text="Realizar Check-in",fg_color="purple",border_color="black",border_width=2,corner_radius=32,hover_color="purple4")
boton_ver_vuelos = ctk.CTkButton(frame_botones, text="Vuelos disponibles",fg_color="purple",border_color="black",border_width=2,corner_radius=32,hover_color="purple4")

#posicion de los elementos
label_titulo.place(x=400, y=20)
label_logo.place(x=0, y=0)
boton_registro.place(x=80, y=70)
boton_comprar.place(x=80, y=140)
boton_checkin.place(x=80, y=210)
boton_ver_vuelos.place(x=80, y=280)



ventana_inicio.mainloop()
