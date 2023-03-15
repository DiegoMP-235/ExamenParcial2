from tkinter import Tk,Label,Message,Entry,Button,Frame
from Alumno import *

nuevoAlumno = Alumno("Isay","GUERRA","LOPEZ","1987","SISTEMAS")
nuevoAlumno.generaMatricula()
Matricula = nuevoAlumno.getMatricula()
print(Matricula)

"""
ventana = Tk()
ventana.title("Matricula generator")
ventana.geometry("350x350")

FrameEntradas = Frame()
"""