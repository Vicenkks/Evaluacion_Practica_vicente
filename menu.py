from conexion import engine
from modelos import Base
from servicios_equipo import *
from servicios_estudiante import *
from servicios_prestamo import *
from datetime import datetime

if __name__ == "__main__":

    opciones = {
        "1": registrar_estudiante,
        "2": listar_estudiantes,
        "3": listar_estudiante_por_id,
        "4": crear_equipo,
        "5": listar_equipos,
        "6": listar_equipo_por_id,
        "7": actualizar_equipo,
        "8": eliminar_equipo,
        "9": registrar_prestamo,
        "10": listar_prestamos,
        "11": devolver_prestamo,
    }

    Base.metadata.create_all(engine)

    while True:
        print("""
        --- Menú de opciones ---
        1. Registrar estudiante
        2. Listar estudiantes
        3. Listar estudiante por ID
        4. Crear equipo
        5. Listar equipos
        6. Listar equipo por ID
        7. Actualizar equipo
        8. Eliminar equipo
        9. Registrar préstamo
        10. Listar préstamos
        11. Devolver préstamo
        0. Salir
        """)
        opcion = input("Seleccione una opción: ")
        if opcion == "0":
            print("Saliendo del programa")
            break
        elif opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción inválida. Intente nuevamente.")