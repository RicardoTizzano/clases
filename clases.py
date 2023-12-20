from os import system
from materias import *
from alumnos import *
from notas import *
import db

AMARILLO = "\x1b[1;33m"

def main_menu():
    while True:
        system("clear")
        print(AMARILLO + "           Menu            ")
        print("1 - Materias")
        print("2 - Alumnos")
        print("3 - Notas")
        print("0 - Salir")
        opcion = input("Ingrese la opcion :")

        if opcion == "1":
            menu_materias(db)
        elif opcion == "2":
            menu_alumnos(db)
            pass
        elif opcion == "3":
            menu_notas(db)
        elif opcion == "0" or opcion=="":
            system("clear")
            break
        else:
            alerta("Opción inválida")

if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)
    main_menu()