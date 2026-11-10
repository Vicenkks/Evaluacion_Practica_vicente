from modelos import Equipo, Prestamo
from conexion import SessionLocal
from sqlalchemy import select

def crear_equipo():
    try:
        nombre = input("Ingrese el nombre del equipo: ")
        tipo = input("Ingrese el tipo de equipo: ")
        stock_disponible = int(input("Ingrese el stock disponible: "))

        if not nombre or not tipo or stock_disponible < 0:
            print("Nombre, tipo y stock disponible no pueden estar vacíos o negativos.")
            return

        with SessionLocal.begin() as session:
            equipo = Equipo(nombre=nombre, tipo=tipo, stock_disponible=stock_disponible)
            session.add(equipo)
            print(f"Equipo creado: {equipo.nombre} ({equipo.tipo}) con stock {equipo.stock_disponible}")
            return
    except ValueError:
        print("Valores inválidos.")

def listar_equipos():
    with SessionLocal() as session:
        stmt = select(Equipo)
        equipos = session.scalars(stmt)
        for equipo in equipos:
            print(equipo)

def listar_equipo_por_id():
    try:
        equipo_id = int(input("Ingrese el ID del equipo: "))
        with SessionLocal() as session:
            stmt = select(Equipo).where(Equipo.id == equipo_id)
            equipo = session.scalar(stmt)
            if equipo:
                print(equipo)
            else:
                print(f"No se encontró un equipo con ID {equipo_id}")
    except ValueError:
        print("ID inválido. Ingrese un número entero.")

def actualizar_equipo():
    try:
        equipo_id = int(input("Ingrese el ID del equipo a actualizar: "))
        with SessionLocal.begin() as session:
            stmt = select(Equipo).where(Equipo.id == equipo_id)
            equipo = session.scalar(stmt)
            if not equipo:
                print(f"No se encontró un equipo con ID {equipo_id}")
                return

            nombre = input(f"Ingrese el nuevo nombre del equipo (actual: {equipo.nombre}): ") or equipo.nombre
            tipo = input(f"Ingrese el nuevo tipo de equipo (actual: {equipo.tipo}): ") or equipo.tipo
            stock_disponible = int(input(f"Ingrese el nuevo stock disponible"))

            if stock_disponible < 0:
                print("El stock disponible no puede ser negativo.")
                return

            equipo.nombre = nombre
            equipo.tipo = tipo
            equipo.stock_disponible = stock_disponible
            print(f"Equipo actualizado: {equipo.nombre} ({equipo.tipo}) con stock {equipo.stock_disponible}")
    except ValueError:
        print("Valores inválidos.")

def eliminar_equipo():
    try:
        equipo_id = int(input("Ingrese el ID del equipo a eliminar: "))
        with SessionLocal.begin() as session:
            stmt = select(Equipo).where(Equipo.id == equipo_id)
            equipo = session.scalar(stmt)
            if not equipo:
                print(f"No se encontró un equipo con ID {equipo_id}")
                return
            if equipo.prestamos:
                print(f"El equipo tiene préstamos asociados.")
                return

            session.delete(equipo)
            print(f"Equipo eliminado")
    except ValueError:
        print("ID inválido. Ingrese un número entero.")

