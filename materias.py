from os import system
from funciones import *
from models import Materia

VERDE    = "\x1b[1;32m"

def menu_materias(db):
    while True:

        system("clear")
        print(VERDE + "         Menu Materias         ")
        print("1 - Alta")
        print("2 - Baja")
        print("3 - Modificación")
        print("4 - Consulta")
        print("0 - Salir")

        opcion = input("Ingrese la opcion :")

        if opcion == "1":
            alta_materia(db)
        elif opcion == "2":
            baja_materia(db)
        elif opcion == "3":
            modificacion_materia(db)
        elif opcion == "4":
            consulta_materia(db)
        elif opcion == "0" or opcion=="":
            system("clear")
            break
        else:
            alerta("Opción inválida")

def alta_materia(db):
    system("clear")
    print("Alta de Materia")
    nombre= input("Ingrese nombre de la materia :")
    if nombre != "":
        materia = Materia(nombre)
        db.session.add(materia)
        db.session.commit()
        system("clear")
        alerta("La materia " + nombre + " se dió de alta")
    else:
        alerta("La materia NO se dió de alta")

def baja_materia(db):
    system("clear")
    print("Baja de Materia")
    id_materia= input("Ingrese Id de la materia :")
    if id_materia != '':
        id_materia= int(id_materia)
        materia = db.session.query(Materia).get(id_materia)
        print("Materia : " + materia.nombre)
        if materia != None:
            if pregunta("Dese dar de baja la materia "+ materia.nombre +"?(s/n)"):
                materia.baja="S"
                db.session.commit()
                system("clear")
                alerta("La materia " + materia.nombre + " se dió de baja")
            else:
                alerta("La materia " + materia.nombre + " NO se dió de baja")
        else:
            alerta("La materia " + str(id_materia) + " no existe")


def modificacion_materia(db):
    system("clear")
    print("Modificación de Materia")
    id_materia= input("Ingrese Id de la materia :")
    if id_materia != '':
        id_materia= int(id_materia)
        materia = db.session.query(Materia).get(id_materia)
        if materia != None:
            print("Materia : " + materia.nombre)
            nombre = input("Ingrese el nombre de la materia :")
            if nombre != '':
                if pregunta("Desea modificar la materia " + materia.nombre + " por " + nombre + "?(s/n)"):
                    materia.nombre = nombre
                    db.session.commit()
                    system("clear")
                    alerta("La materia " + materia.nombre + " se modificó")
            else:
                alerta("La materia " + materia.nombre + " NO se modificó")
        else:
            alerta("La materia " + str(id_materia) + " no existe")

def consulta_materia(db):
    system("clear")
    print("Consulta de Materia")
    id_materia= input("Ingrese Id de la materia :")
    if id_materia != '':
        id_materia= int(id_materia)
        materia = db.session.query(Materia).get(id_materia)
        if materia != None:
            print("Id      : " + str(materia.id_materia))
            print("Materia : " + materia.nombre)
            input("Presione una tecla para continuar ...")  
        else:
            alerta("La materia con ese Id no existe")