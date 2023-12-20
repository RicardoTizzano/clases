import db
from models import Materia
from models import Alumno
import db


def run(db):
    id_alumno = input("Ingrese Id del alumno")
    id_alumno = int(id_alumno)
    alumno = db.session.query(Alumno).get(id_alumno)
    print("Alumno : " + alumno.nombre)

    id_materia = input("Ingrese Id de la materia")
    id_materia = int(id_materia)
    materia = db.session.query(Materia).get(id_materia)
    print("Materia : " + materia.nombre)



if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)
    run(db)