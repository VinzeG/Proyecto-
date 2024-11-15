#Importando librerias
import tkinter as tk

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Importando archivos necesarios
from ConexionBD import *
from personal import *

def Seleccionar_registro(event):
    try:
        Item_seleccionado = tree.focus()
        if Item_seleccionado:
            values = tree.item(Item_seleccionado) ['values']
            textbox_Codigo.delete(0,END)
            textbox_Codigo.insert(0,values[0])

            textbox_Nombre.delete(0,END)
            textbox_Nombre.insert(0,values[1])

            textbox_Apellido.delete(0,END)
            textbox_Apellido.insert(0,values[2])
            
            textbox_Cargo.delete(0,END)
            textbox_Cargo.insert(0,values[3])

            combo.set(values[4])
    except ValueError as error:
        print("Error al seleccionar registro{}".format(error))

def Actualizar_lista():
    global tree
    try:
        tree.delete(*tree.get_children())
        datos = CPersonal.Modificar_personal()

        for row in CPersonal.Modificar_personal():
            tree.insert("","end",values= row)
    except ValueError as error:
            print("Error al mostrar la interfaz grafica, error:{}".format(error))


def Guardar_registro():
    global textbox_Nombre,textbox_Apellido,textbox_Cargo,groupBox,groupBox2,combo
    try:
        #Verificando si los widgets estan inicializados
        if textbox_Nombre is None or textbox_Apellido is None or textbox_Cargo is None or combo is None:
            print("Los widgets no estan inicializados")
            return
        nombre = textbox_Nombre.get()
        apellido = textbox_Apellido.get()
        cargo = textbox_Cargo.get()
        sexo = combo.get()

        CPersonal.Ingresar_personal(nombre,apellido,cargo,sexo)
        messagebox.showinfo("Informacion","Los datos fueron guardados")

        Actualizar_lista()

        textbox_Nombre.delete(0,END)
        textbox_Apellido.delete(0,END)
        textbox_Cargo.delete(0,END)
    
    except ValueError as error:
        print("Error al ingresar datos{}".format(error))


class Formulario_Personal:

    #Globalizando los widgets
    global base
    base = None

    global groupBox
    groupBox = None

    global textbox_Codigo
    textbox_Codigo = None

    global textbox_Nombre
    textbox_Nombre = None

    global textbox_Apellido
    textbox_Apellido = None

    global textbox_Cargo
    textbox_Cargo = None

    global combo
    combo = None

    global groupBox2
    groupBox2 = None

    global tree
    tree = None

    #Formulario
    def Formulario():
        #Llamando variables globales
        global base
        global groupBox
        global textbox_Nombre
        global textbox_Apellido
        global textbox_Cargo
        global textbox_Codigo
        global combo
        global tree

        try:
            base= Tk()
            base.geometry("1500x300")
            base.title("Control de Acceso del Personal")

            groupBox =LabelFrame(base,text="Datos del Personal",padx=5,pady=5)
            groupBox.grid(row=0,column=0,padx=10,pady=10)
            
            label_codigo=Label(groupBox,text="Codigo: ", width=13,font=("arial,12")).grid(row=0,column=0)
            textbox_Codigo=Entry(groupBox)
            textbox_Codigo.grid(row=0,column=1)

            label_nombre=Label(groupBox,text="Nombre: ", width=13,font=("arial,12")).grid(row=1,column=0)
            textbox_Nombre=Entry(groupBox)
            textbox_Nombre.grid(row=1,column=1)

            label_apellido=Label(groupBox,text="Apellido: ", width=13,font=("arial,12")).grid(row=2,column=0)
            textbox_Apellido=Entry(groupBox)
            textbox_Apellido.grid(row=2,column=1)

            label_cargo=Label(groupBox,text="Cargo: ", width=13,font=("arial,12")).grid(row=3,column=0)
            textbox_Cargo=Entry(groupBox)
            textbox_Cargo.grid(row=3,column=1)

            label_sexo=Label(groupBox,text="Sexo: ", width=13,font=("arial,12")).grid(row=4,column=0)
            select_sexo=tk.StringVar()
            combo=ttk.Combobox(groupBox,values=["Masculino","Femenino"],textvariable=select_sexo)
            combo.grid(row=4,column=1)

            select_sexo.set("Masculino")

            Button(groupBox,text="Guardar",width=10,command=Guardar_registro).grid(row=6,column=0)
            Button(groupBox,text="Modificar",width=10).grid(row=6,column=1)
            Button(groupBox,text="Eliminar",width=10).grid(row=6,column=2)

            groupBox2 =LabelFrame(base,text="Lista del Personal",padx=5,pady=5)
            groupBox2.grid(row=0,column=1,padx=5,pady=5)
        
            #Creando Treeview y configurando columnas

            tree=ttk.Treeview(groupBox2,columns=("ID","Nombre","Apellido","Cargo","Sexo"),show='headings',height=5,)
            
            tree.column("# 1",anchor=CENTER)
            tree.heading("# 1",text="ID")
            
            tree.column("# 2",anchor=CENTER)
            tree.heading("# 2",text="Nombre")

            tree.column("# 3",anchor=CENTER)
            tree.heading("# 3",text="Apellido")

            tree.column("# 4",anchor=CENTER)
            tree.heading("# 4",text="Cargo")

            tree.column("# 5",anchor=CENTER)
            tree.heading("# 5",text="Sexo")

            for row in CPersonal.Modificar_personal():
                tree.insert("","end",values= row)

            tree.bind("<<TreeviewSelect>>",Seleccionar_registro)

            tree.pack()

            base.mainloop()

        except ValueError as error:
            print("Error al mostrar la interfaz grafica, error:{}".format(error))

    Formulario()
