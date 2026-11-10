from modelos import Estudiante
from conexion import SessionLocal
from sqlalchemy import select

def registrar_estudiante():
    try:
        nombre = input("Ingrese el nombre del estudiante: ")
        correo = input("Ingrese el correo del estudiante: ")

        if not nombre or not correo:
            print("Nombre y correo no pueden estar vacíos.")
            return

        with SessionLocal.begin() as session:
            estudiante_existe = session.scalar(select(Estudiante).where(Estudiante.correo == correo))
            if estudiante_existe:
                print(f"Ya existe un estudiante con el correo {correo}.")
                return

            estudiante = Estudiante(nombre=nombre, correo=correo)
            session.add(estudiante)
            print(f"Estudiante registrado: {estudiante.nombre} ({estudiante.correo})")
    except ValueError:
        print("Valores invalidos.")

def listar_estudiantes():
    with SessionLocal() as session:
        stmt = select(Estudiante)
        estudiantes = session.scalars(stmt)
        for estudiante in estudiantes:
            print(estudiante)

def listar_estudiante_por_id():
    try:
        estudiante_id = int(input("Ingrese el ID del estudiante: "))
        with SessionLocal() as session:
            stmt = select(Estudiante).where(Estudiante.id == estudiante_id)
            estudiante = session.scalar(stmt)
            if estudiante:
                print(estudiante)
            else:
                print(f"No se encontró un estudiante con ID {estudiante_id}")
    except ValueError:
        print("ID inválido. Ingrese un número entero.")