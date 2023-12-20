import db
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey

class Alumno(db.Base):
    __tablename__ = "alumno"
    id_alumno = Column(Integer, primary_key=True, autoincrement=True)
    nombre    = Column(String, nullable=False)
    apellido  = Column(String, nullable=False)
    f_nac     = Column(Date)
    n_doc     = Column(Integer,nullable=False)
    genero    = Column(String)
    baja      = Column(String)

    def __init__(self, nombre, apellido, f_nac, n_doc, genero):
        self.nombre   = nombre
        self.apellido = apellido
        self.f_nac    = f_nac
        self.n_doc    = n_doc
        self.genero   = genero


class Materia(db.Base):
    __tablename__ = "materia"
    id_materia = Column(Integer, primary_key=True, autoincrement=True)
    nombre     = Column(String, nullable=False)
    baja       = Column(String)

    def __init__(self, nombre):
        self.nombre = nombre

class Nota(db.Base):
    __tablename__ = "notas"
    id_alumno  = Column(Integer, ForeignKey(Alumno.id_alumno), nullable=False,  primary_key=True)
    id_materia = Column(Integer, ForeignKey(Materia.id_materia), nullable=False, primary_key=True)
    trimestre  = Column(Integer, primary_key=True, nullable=False)
    nota       = Column(Float, nullable=False)

    def __init__(self, id_alumno, id_materia, trimestre, nota):
        self.id_alumno  = id_alumno
        self.id_materia = id_materia
        self.trimestre  = trimestre
        self.nota       = nota


