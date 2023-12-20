from datetime import datetime
from os import system
from funciones import *
from models import Alumno

MORADO    ="\x1b[1;35m"

def menu_alumnos(db):
    while True:

        system("clear")
        print(MORADO + "         Menu Alumnos         ")
        print("1 - Alta")
        print("2 - Baja")
        print("3 - Modificación")
        print("4 - Consulta")
        print("0 - Salir")

        opcion = input("Ingrese la opcion :")

        if opcion == "1":
            alta_alumno(db)
        elif opcion == "2":
            baja_alumno(db)
        elif opcion == "3":
            modificacion_alumno(db)
        elif opcion == "4":
            consulta_alumno(db)
        elif opcion == "0" or opcion=="":
            system("clear")
            break
        else:
            alerta("Opción inválida")

def alta_alumno(db):
    system("clear")
    print("Alta de Materia")
    nombre   = input("Nombre                           : ")
    apellido = input("Apellido                         : ")
    f_nac    = input("Fecha de nacimiento (dd/mm/aaaa) : ")
    n_doc    = input("DNI                              : ")
    genero   = input("Genero (F/M)                     : ")
    if valida_alumno(nombre, apellido, f_nac,n_doc,genero):
        f_nac = datetime.strptime(f_nac, '%d/%m/%Y').date()
        genero = genero.upper()
        alumno = Alumno(nombre, apellido, f_nac,n_doc, genero)
        db.session.add(alumno)
        db.session.commit()
        system("clear")
        alerta("El alumno " + alumno.nombre+" "+alumno.apellido + " se dió de alta")
    else:
        alerta("El alumno NO se dió de alta")

def baja_alumno(db):
    system("clear")
    print("Baja de Alumno")
    id_alumno= input("Ingrese Id del alumno :")
    if id_alumno != '':
        id_alumno= int(id_alumno)
        alumno = db.session.query(Alumno).get(id_alumno)
        if alumno != None:
            print("Nombre   : " + alumno.nombre)
            print("Apellido : " + alumno.apellido)
            print("DNI      : " + str(alumno.n_doc))
            if pregunta("Dese dar de baja el alumno "+ alumno.nombre +"?(s/n)"):
                alumno.baja="S"
                db.session.commit()
                system("clear")
                alerta("El alumno " + alumno.nombre + " se dió de baja")
            else:
                alerta("El alumno " + alumno.nombre + " NO se dió de baja")
        else:
            alerta("El alumno " + str(id_alumno) + " no existe")


def modificacion_alumno(db):
    system("clear")
    id_alumno= int(input("Ingrese Id del alumno :"))
    if id_alumno != '':
        id_alumno= int(id_alumno)
        alumno = db.session.query(Alumno).get(id_alumno)
        if alumno != None:
            print("Alumno :",alumno.nombre,alumno.apellido)
            nombre= input("Ingrese nombre del alumno :") or alumno.nombre
            apellido = input("Ingrese apellido del alumno :") or alumno.apellido
            f_nac    = input("Ingrese fecha de nacimiento del alumno :") or alumno.f_nac
            n_doc    = input("Ingrese DNI del alumno :") or alumno.n_doc
            genero   = input("Ingrese genero del alumno :") or alumno.genero
            if valida_alumno(nombre, apellido, f_nac,n_doc,genero):
                if pregunta("Desea modificar el alumno " + alumno.nombre + " " + alumno.apellido +"(s/n)? "):
                    f_nac = datetime.strptime(f_nac, '%d/%m/%Y').date()
                    genero = genero.upper()
                    alumno.nombre = nombre
                    alumno.apellido = apellido
                    alumno.f_nac = f_nac
                    alumno.n_doc = n_doc
                    alumno.genero = genero
                    db.session.commit()
                    system("clear")
                    alerta("El alumno " + nombre + " " + apellido + " se modificó")
                else:
                    alerta("El alumno NO modificó")
            else:
                alerta("El alumno NO modificó")
        else:
            alerta("El alumno con ese ID no existe. Verfique")

def consulta_alumno(db):
    system("clear")
    print("Consulta de Alumno")
    id_alumno= input("Ingrese Id del alumno :")
    if id_alumno != '':
        id_alumno= int(id_alumno)
        alumno = db.session.query(Alumno).get(id_alumno)
        if alumno != None:
            system("clear")
            print("Nombre                           : "+alumno.nombre)
            print("Apellido                         : "+alumno.apellido)
            print("Fecha de nacimiento (dd/mm/aaaa) : "+alumno.f_nac.strftime('%d/%m/%Y'))
            print("DNI                              : "+str(alumno.n_doc))
            print("Genero                           : "+alumno.genero)
            input("Presione una tecla para continuar ...")  
