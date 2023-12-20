from os import system
from funciones import *
from models import Nota
from models import Alumno
from models import Materia
from prettytable import PrettyTable

ROJO    = "\x1b[1;31m"

def menu_notas(db):
    while True:

        system("clear")
        print(ROJO + "         Menu notas         ")
        print("1 - Alta")
        print("2 - Baja")
        print("3 - Modificación")
        print("4 - Consulta")
        print("5 - Consulta de Notas de Alumnos")
        print("6 - Consulta de todos los Alumnos")
        print("0 - Salir")

        opcion = input("Ingrese la opcion :")

        if opcion == "1":
            alta_nota(db)
        elif opcion == "2":
            baja_nota(db)
        elif opcion == "3":
            modificacion_nota(db)
        elif opcion == "4":
            consulta_nota(db)
        elif opcion == "5":
            consulta_notas(db)
        elif opcion == "6":
            consulta_notas_total(db)
        elif opcion == "0" or opcion=="":
            system("clear")
            break
        else:
            alerta("Opción inválida")

def alta_nota(db):
    system("clear")
    print("Alta de Notas")
    id_alumno= input("Ingrese Id del alumno :")
    if id_alumno != '':
        id_alumno= int(id_alumno)
        alumno = db.session.query(Alumno).get(id_alumno)
        if alumno != None:
            print("Alumno   : " + alumno.nombre + " " + alumno.apellido)
            id_materia= input("Ingrese Id de la materia :")
            if id_materia != '':
                id_materia= int(id_materia)
                materia = db.session.query(Materia).get(id_materia)
                if materia != None:
                    print("Materia : " + materia.nombre)
                    trimestre = input("Ingrese el trimestre :") or 1
                    valor = input("Ingrese la nota :")
                    valor = int(valor)
                    if valor != None:
                        nota = db.session.query(Nota).filter(Nota.id_alumno == id_alumno). \
                                                filter(Nota.id_materia == id_materia). \
                                                filter(Nota.trimestre == trimestre)
                        if nota.count() == 0:
                            nota = Nota(id_alumno,id_materia,trimestre,valor)
                            db.session.add(nota)
                            db.session.commit()
                            system("clear")
                            alerta("Se dio de alta la nota")
                        else:
                            alerta("La nota ya existe. Verifique o modifíquela de ser necesario")
                    else: 
                        alerta("La nota puede ser 0")
                else:
                    alerta("La materia no existe. Verifique.")
def baja_nota(db):
    system("clear")
    print("Baja de Notas")
    id_alumno= input("Ingrese Id del alumno :")
    if id_alumno != '':
        id_alumno= int(id_alumno)
        alumno = db.session.query(Alumno).get(id_alumno)
        if alumno != None:
            print("Alumno   : " + alumno.nombre + " " + alumno.apellido)
            id_materia= input("Ingrese Id de la materia :")
            if id_materia != '':
                id_materia= int(id_materia)
                materia = db.session.query(Materia).get(id_materia)
                if materia != None:
                    print("Materia : " + materia.nombre)
                    trimestre = input("Ingrese el trimestre :") or 1
                    notas = db.session.query(Nota).where((Nota.id_alumno == id_alumno) & 
                                            (Nota.id_materia == id_materia) & 
                                            (Nota.trimestre == trimestre)).one()
                    if notas != None:
                        print("Nota   : "+str(notas.nota))
                        if pregunta("Desea borrar la nota? "):
                            db.session.delete(notas)
                            db.session.commit()
                            system("clear")
                            alerta("Se dio de baja la nota")
                    else:
                        alerta("La nota no existe. Verifique")
                else:
                    alerta("La nota no existe. Verifique")

def modificacion_nota(db):
    system("clear")
    print("Modificación de Notas")
    id_alumno= input("Ingrese Id del alumno : ")
    if id_alumno != '':
        id_alumno= int(id_alumno)
        alumno = db.session.query(Alumno).get(id_alumno)
        if alumno != None:
            print("Alumno   : " + alumno.nombre + " " + alumno.apellido)
            id_materia= input("Ingrese Id de la materia : ")
            if id_materia != '':
                id_materia= int(id_materia)
                materia = db.session.query(Materia).get(id_materia)
                if materia != None:
                    print("Materia : " + materia.nombre)
                    trimestre = input("Ingrese el trimestre : ") or 1
                    notas = db.session.query(Nota).where((Nota.id_alumno == id_alumno) & 
                                            (Nota.id_materia == id_materia) & 
                                            (Nota.trimestre == trimestre)).one()
                    if notas != None:
                        print("Nota   : "+str(notas.nota))
                        nuevaNota = input("Ingrese la nueva nota : ")
                        if nuevaNota != "":

                            nuevaNota=int(nuevaNota)
                            if pregunta("Desea cambiar la nota? "):
                                notas.nota = nuevaNota
                                db.session.commit()
                                system("clear")
                                alerta("Se modificó la nota")
                    else:
                        alerta("La nota no existe. Verifique")
                else:
                    alerta("La nota no existe. Verifique")


def consulta_nota(db):
    system("clear")
    print("Consulta de Notas")
    id_alumno= input("Ingrese Id del alumno : ")
    if id_alumno != '':
        id_alumno= int(id_alumno)
        alumno = db.session.query(Alumno).get(id_alumno)
        if alumno != None:
            print("Alumno   : " + alumno.nombre + " " + alumno.apellido)
            id_materia= input("Ingrese Id de la materia : ")
            if id_materia != '':
                id_materia= int(id_materia)
                materia = db.session.query(Materia).get(id_materia)
                if materia != None:
                    print("Materia : " + materia.nombre)
                    trimestre = input("Ingrese el trimestre : ") or 1
                    notas = db.session.query(Nota).where((Nota.id_alumno == id_alumno) & 
                                            (Nota.id_materia == id_materia) & 
                                            (Nota.trimestre == trimestre))
                    if notas.count() == 1:
                        print("Nota   : "+str(notas[0].nota))
                        input("Presione una tecla para continuar ...")  
                        
                    else:
                        alerta("La nota no existe. Verifique")
                else:
                    alerta("La nota no existe. Verifique")

def consulta_notas(db):
    system("clear")
    print("Consulta de Notas de un Alumno")
    id_alumno= input("Ingrese Id del alumno : ")
    if id_alumno != '':
        id_alumno= int(id_alumno)
        alumno = db.session.query(Alumno).get(id_alumno)
        if alumno != None:
            print("Alumno   : " + alumno.nombre + " " + alumno.apellido)

            notas = db.session.query(Alumno,Nota, Materia) \
                    .order_by(Nota.id_materia, Nota.trimestre) \
                    .join(Alumno) \
                    .join(Materia) \
                    .where((Nota.id_alumno == id_alumno) & \
                    (Nota.id_alumno == id_alumno)).all()
            if notas != None:
                system("clear")
                tabla = PrettyTable(['Materia','Trimestre','Nota'])
                tabla.align['Nota']='r'
                for n in notas:
                    tabla.add_row([n.Materia.nombre,n.Nota.trimestre, n.Nota.nota])
                print(tabla)
                input("Presione una tecla para seguir")
            else:
                alerta("No hay notas para esa materia.")

def consulta_notas_total(db):
    system("clear")
    print("Consulta de Notas de los Alumno")
    notas = db.session.query(Alumno,Nota, Materia) \
            .order_by(Alumno.apellido + Alumno.nombre,Nota.id_materia, Nota.trimestre) \
            .join(Alumno) \
            .join(Materia).all()
    system("clear")
    tabla = PrettyTable(['Alumno','','Materia','Trimestre','Nota'])
    tabla.align['Nota']='r'
    for n in notas:
        tabla.add_row([n.Alumno.nombre,n.Alumno.apellido,n.Materia.nombre,n.Nota.trimestre, n.Nota.nota])
    print(tabla)
    input("Presione una tecla para seguir")
