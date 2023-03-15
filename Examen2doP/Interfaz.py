from tkinter import Tk,Label,Entry,Button,Frame,messagebox
from Alumno import *

def generarMatricula():
    myMatricula = Alumno(EntradaName.get().upper(),EntradaApellidoP.get().upper(),EntradaApellidoM.get().upper(),EntradaAnioNac.get(),EntradaCarrera.get().upper())
    myMatricula.generaMatricula()
    MatriculaNueva = myMatricula.getMatricula()
    messagebox.showinfo("Matricula","Su matricula es:\n"+MatriculaNueva)

ventana = Tk()
ventana.title("Matricula generator")
ventana.geometry("350x350")

FrameEntradas = Frame(ventana,bg="lightblue")
FrameBTN = Frame(ventana,bg="grey")

#Titulo
LabelTittle = Label(FrameEntradas,text="Mi matricula",font=("Arial", 12, "bold"), fg="#333", bg="#f2f2f2", padx=6, pady=6)
LabelTittle.pack()

#Nombre
FrameEntradas.pack(expand=True,fill="both")
FrameBTN.pack(expand=True,fill="both")

NombreLab = Label(FrameEntradas,text="Nombre:")
EntradaName = Entry(FrameEntradas)
NombreLab.pack()
EntradaName.pack()

#Apellidos

ApellidoPLab = Label(FrameEntradas,text="Apellido Paterno:")
EntradaApellidoP = Entry(FrameEntradas)

ApellidoPLab.pack()
EntradaApellidoP.pack()

ApellidoMLab = Label(FrameEntradas,text="Apellido Materno:")
EntradaApellidoM = Entry(FrameEntradas)

ApellidoMLab.pack()
EntradaApellidoM.pack()
#Anio nacimiento
AnioNacLab = Label(FrameEntradas,text="Año de nacimiento:")
EntradaAnioNac = Entry(FrameEntradas)

AnioNacLab.pack()
EntradaAnioNac.pack()

#Carrera
CarreraLab = Label(FrameEntradas,text="Carrera:")
EntradaCarrera = Entry(FrameEntradas)

CarreraLab.pack()
EntradaCarrera.pack()

#Botones
BtnGenerar = Button(FrameBTN,text="Matricula",command=generarMatricula)
BtnGenerar.pack()

ventana.mainloop()

