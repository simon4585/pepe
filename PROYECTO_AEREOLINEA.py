import tkinter as tk
import  customtkinter as ctk
import ctypes as ct
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import ttk
from PIL import Image, ImageTk
import datetime as dt
import csv
import random as rd
ctk.set_appearance_mode("light")


def vuelos_recomendados(ventana_compra):
    y= 510
    with open("vuelos.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                frame_vuelos = ctk.CTkFrame(ventana_compra,fg_color="white",corner_radius=32,width=800, height=100, border_color="purple",border_width=3)
                frame_vuelos.place(x=350, y=y)
                vuelos= ctk.CTkLabel(frame_vuelos, text=row, font=("Arial", 15))
                vuelos.place(x=50, y=50)
                y += 100 


def condicion_inicio_sesion(entry_codigo_u,codigos_usuarios,ventana_inicio_sesion,nombre_usuario):
    codigo= entry_codigo_u.get()
    if codigo=="":
        messagebox.showerror("Error","Por favor ingrese un codigo de inicio de sesion")
        return
    with open("datos_usuarios.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and len(row) >= 10 and row[9] == codigo:
                messagebox.showinfo("Informacion","Inicio de sesion exitoso")
                nombre_usuario=row[0]
                comprar_tiquete(ventana_inicio_sesion,nombre_usuario)
                return nombre_usuario
                
    messagebox.showerror("Error", "El código de inicio de sesión no es válido")
                
    
        




def ventana_inicio_sesion(ventana_inicio,codigos_usuarios,nombre_usuario):
    ventana_inicio.destroy()
    ventana_inicio_sesion = ctk.CTk()
    ventana_inicio_sesion.title("Inicio de sesion")
    ventana_inicio_sesion.geometry("500x500+250+80")
    
    label_titulo = ctk.CTkLabel(ventana_inicio_sesion, text="Inicio de sesion", font=("Arial", 20))
    label_codigo = ctk.CTkLabel(ventana_inicio_sesion, text="Codigo de inicio de sesion:", font=("Arial", 15))
    entry_codigo_u = ctk.CTkEntry(ventana_inicio_sesion, font=("Arial", 15),border_color="purple")
    boton_iniciar_sesion= ctk.CTkButton(ventana_inicio_sesion,text="Iniciar Sesion", font=("arial",15),fg_color="purple",corner_radius=32,hover_color="purple4",command= lambda: condicion_inicio_sesion(entry_codigo_u,codigos_usuarios,ventana_inicio_sesion,nombre_usuario))
    
    label_titulo.place(relx=0.5, rely=0.1, anchor="center")
    label_codigo.place(relx=0.5, rely=0.3, anchor="center")
    entry_codigo_u.place(relx=0.5, rely=0.4, anchor="center")
    boton_iniciar_sesion.place(relx=0.5,rely=0.5,anchor= "center")
    
    ventana_inicio_sesion.mainloop()





def comprar_tiquete(ventana_inicio_sesion,nombre_usuario):
    ventana_inicio_sesion.destroy()
    ventana_compra = ctk.CTk()
    ventana_compra.title("Compra de tiquetes")
    ventana_compra.geometry("1800x800+0+0")
    
    #se crea un frame para los botones
    frame_botones = ctk.CTkFrame(ventana_compra,fg_color="white",corner_radius=32,width=900, height=250, border_color="purple",border_width=3)
    frame_botones.place(x=300, y=150)
    
    label_nombre_usuario = ctk.CTkLabel(ventana_compra, text="Bienvenid@, "+nombre_usuario ,font=("Arial", 20),text_color="purple")
    label_titulo = ctk.CTkLabel(ventana_compra, text="Stellar Airways", font=("ERAS DEMIS ITC", 20),text_color="purple")
    labelsubtitulo = ctk.CTkLabel(ventana_compra, text="Compra de tickets", font=("Arial", 15))
    label_texto = ctk.CTkLabel(ventana_compra, text="Empieza a buscar las mejores opciones:", font=("Arial", 20))
    label_origen = ctk.CTkLabel(frame_botones, text="Origen:", font=("Arial", 15))
    lugares_origuen= ctk.CTkComboBox(frame_botones, values=["Bogota", "Medellin", "Cali", "Barranquilla", "Cartagena", "Santa Marta", "San Andres", "Leticia", "Bucaramanga", "Pereira", "Armenia", "Manizales", "Cucuta", "Pasto", "Popayan", "Neiva", "Villavicencio", "Monteria", "Riohacha", "Valledupar", "Tunja", "Yopal" ], font=("Arial", 15),border_color="purple",button_color="purple",button_hover_color="purple4")
    label_destino = ctk.CTkLabel(frame_botones, text="Destino:", font=("Arial", 15))
    lugares_destino= ctk.CTkComboBox(frame_botones, values=["Bogota", "Medellin", "Cali", "Barranquilla", "Cartagena", "Santa Marta", "San Andres", "Leticia", "Bucaramanga", "Pereira", "Armenia", "Manizales", "Cucuta", "Pasto", "Popayan", "Neiva", "Villavicencio", "Monteria", "Riohacha", "Valledupar", "Tunja", "Yopal" ], font=("Arial", 15),border_color="purple",button_color="purple",button_hover_color="purple4")
    label_fecha_salida = ctk.CTkLabel(frame_botones, text="Fecha de salida:", font=("Arial", 15))
    entry_fecha_salida = ctk.CTkEntry(frame_botones, font=("Arial", 15),border_color="purple")
    label_fecha_regreso = ctk.CTkLabel(frame_botones, text="Fecha de regreso:", font=("Arial", 15))
    entry_fecha_regreso = ctk.CTkEntry(frame_botones, font=("Arial", 15),border_color="purple")
    label_numero_pasajeros = ctk.CTkLabel(frame_botones, text="Numero de pasajeros:", font=("Arial", 15))
    entry_numero_pasajeros = ctk.CTkEntry(frame_botones, font=("Arial", 15),border_color="purple")
    boton_buscar= ctk.CTkButton(ventana_compra,text="Buscar Vuelo", font=("arial",15),fg_color="purple",corner_radius=32,hover_color="purple4",command= lambda: vuelos_recomendados(ventana_compra))

    
    label_nombre_usuario.place(x=30, y=30)
    label_titulo.place(relx=0.5, rely=0.05, anchor="center")
    labelsubtitulo.place(relx=0.5, rely=0.1, anchor="center")
    label_texto.place(relx=0.5, rely=0.15, anchor="center")
    label_origen.place(x=140, y=50)
    lugares_origuen.place(x=240, y=50)
    label_destino.place(x=540, y=50)
    lugares_destino.place(x=640, y=50)
    label_fecha_salida.place(x=120, y=100)
    entry_fecha_salida.place(x=240, y=100)
    label_fecha_regreso.place(x=500, y=100)
    entry_fecha_regreso.place(x=640, y=100)
    label_numero_pasajeros.place(x=370, y=150)
    entry_numero_pasajeros.place(x=380, y=183)
    
    boton_buscar.place(x=680, y=400)

    vuelos_recomendados(ventana_compra)
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

    codigos_usuarios= rd.randint(1000,9999)
    messagebox.showinfo("informacion","Datos guardados exitosamente, su codigo de inicio de sesion es: "+str(codigos_usuarios))
    
    # Si el documento no existe, agregar el nuevo registro
    with open("datos_usuarios.csv", "a") as f:
        f.write(f"\n{entry_nombre.get()},{entry_apellido.get()},{combo_genero.get()},{entry_nacionalidad.get()},{documento},{entry_fecha_nacimiento.get()},{entry_correo.get()},{entry_numero_telefono.get()},{valor_seleccionado.get()},{codigos_usuarios}\n")


    
def ventanaregistro(ventana_inicio):
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








def main(codigos_usuarios,nombre_usuario):

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
    boton_registro = ctk.CTkButton(frame_botones, text="Registro",fg_color="purple" ,border_color="black",border_width=2,corner_radius=32,hover_color="purple4",command= lambda: ventanaregistro(ventana_inicio))
    boton_comprar = ctk.CTkButton(frame_botones, text="Comprar tiquete",fg_color="purple",border_color="black",border_width=2,corner_radius=32,hover_color="purple4",command= lambda:ventana_inicio_sesion(ventana_inicio,codigos_usuarios,nombre_usuario))
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

if __name__ == "__main__":
    codigos_usuarios = []  
    main(codigos_usuarios,nombre_usuario="")