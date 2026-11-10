from modelos import Estudiante, Prestamo, Estado, Equipo
from conexion import SessionLocal
from sqlalchemy import select
from datetime import datetime


#verificar existencia de registros, cantidad positiva, stock suficiente, descontar disponibilidad
def registrar_prestamo():
    try:
        estudiante_id = int(input("Ingrese el ID del estudiante: "))
        equipo_id = int(input("Ingrese el ID del equipo: "))
        cantidad = int(input("Ingrese la cantidad a prestar: "))
        fecha = datetime.strptime(input("Fecha AAAA-MM-DD: "), "%Y-%m-%d")

        if cantidad <= 0:
            print("La cantidad debe ser un número positivo.")
            return

        with SessionLocal.begin() as session:
            estudiante = session.scalar(select(Estudiante).where(Estudiante.id == estudiante_id))
            if not estudiante:
                print(f"No se encontró un estudiante con ID {estudiante_id}")
                return

            equipo = session.scalar(select(Equipo).where(Equipo.id == equipo_id))
            if not equipo:
                print(f"No se encontró un equipo con ID {equipo_id}")
                return

            if equipo.stock_disponible < cantidad or equipo.stock_disponible <= 0:
                print(f"No hay suficiente stock disponible. Stock actual: {equipo.stock_disponible}")
                return

            prestamo = Prestamo(fecha=fecha, estado=Estado.ACTIVO.value, cantidad=cantidad, estudiante_id=estudiante_id, equipo_id=equipo_id)
            session.add(prestamo)
            equipo.stock_disponible -= cantidad
            print(f"Prestamo Registrado")
    except ValueError:
        print("Valores inválidos. Ingrese números enteros para IDs y cantidad.")

def listar_prestamos():
    with SessionLocal() as session:
        stmt = select(Prestamo)
        prestamos = session.scalars(stmt)
        for prestamo in prestamos:
            print(prestamo)

def devolver_prestamo():
    try:
        prestamo_id = int(input("Ingrese el ID del prestamo a devolver: "))

        with SessionLocal.begin() as session:
            prestamo = session.scalar(select(Prestamo).where(Prestamo.id == prestamo_id))

            if not prestamo:
                print(f"No se encontró un prestamo con ID {prestamo_id}")
                return

            if prestamo.estado == Estado.DEVUELTO.value:
                print(f"El prestamo ya ha sido devuelto.")
                return

            print(prestamo)
            
            prestamo.estado = Estado.DEVUELTO.value
            equipo = session.scalar(select(Equipo).where(Equipo.id == prestamo.equipo_id))
            equipo.stock_disponible += prestamo.cantidad
            print(f"Prestamo devuelto")
    except ValueError:
        print("ID inválido. Ingrese un número entero.")