import time
import sqlite3
from datetime import datetime

def connect():
    try:
        cnt = sqlite3.connect("clases.db")
    except:
        alerta("No se conectó la base de datos")
    return cnt, cnt.cursor() 

def alerta(mensaje):
    print(mensaje)
    time.sleep(2)

def pregunta(texto):
    pregunta = input(texto)
    if pregunta == "s" or pregunta=="S":
        salida = True
    else:
        salida=False
    return salida

def valida_alumno(nombre, apellido, f_nac,n_doc,genero):
    salida= False
    try:
        f_nac = datetime.strptime(f_nac, '%d/%m/%Y').date()
        if nombre != "":
            if apellido != "":
                if n_doc != 0:
                    if genero =='F' or genero=='M':
                        salida=True
                    else:
                        alerta("El género debe ser F o M")
                else:
                    alerta("El DNI no puede ser 0")
            else:
                alerta("El apellido no puede estar en blanco")
        else:
            alerta("El nombre no puede estar en blanco")
    except:
        alerta("Formato de fecha inválido")
    return salida

