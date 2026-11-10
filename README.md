# Sistema de Gestión de equipos tecnologicos

## Datos del estudiante

- **Nombre:** Vicente Huilcaman
- **Asignatura:** Programacion 2
- **Docente:** Pedro Gaete

### Instalación de uv

En Linux o macOS:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

En Windows:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Instalación del proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/Vicenkks/Evaluacion_Practica_vicente.git
```

### 2. Instalar las dependencias

Ejecutar:

```bash
uv sync
```

### 3. Ejecutar el programa

```bash
uv run python menu.py
```

### Ejecución sin uv (Python normal)

**1. Crear el entorno virtual:**

```bash
python3 -m venv .venv
```

**2. Activar el entorno virtual (Linux/macOS):**

```bash
source .venv/bin/activate
```

**3. Instalar dependencias:**

```bash
python -m pip install sqlalchemy
```

**4. Ejecutar el sistema:**

```bash
python menu.py
```

### Casos de prueba
```

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
        
Seleccione una opción: 4
Ingrese el nombre del equipo: Notebook UCT
Ingrese el tipo de equipo: Computador 
Ingrese el stock disponible: 5
Equipo creado: Notebook UCT (Computador) con stock 5

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
        
Seleccione una opción: 4
Ingrese el nombre del equipo: Proyector
Ingrese el tipo de equipo: Proyector
Ingrese el stock disponible: 3
Equipo creado: Proyector (Proyector) con stock 3

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
        
Seleccione una opción: 1
Ingrese el nombre del estudiante: Vicente
Ingrese el correo del estudiante: vicente@gmail.com
Estudiante registrado: Vicente (vicente@gmail.com)

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
        
Seleccione una opción: 9
Ingrese el ID del estudiante: 1
Ingrese el ID del equipo: 1
Ingrese la cantidad a prestar: 2
Fecha AAAA-MM-DD: 2026-11-10
Prestamo Registrado

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
        
Seleccione una opción: 5

        --- Equipo ---
        ID: 1
        Nombre: Notebook UCT
        Tipo: Computador
        Stock disponible: 3
        

        --- Equipo ---
        ID: 2
        Nombre: Proyector
        Tipo: Proyector
        Stock disponible: 3
        

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
        
Seleccione una opción: 9
Ingrese el ID del estudiante: 1
Ingrese el ID del equipo: 1
Ingrese la cantidad a prestar: 4
Fecha AAAA-MM-DD: 2026-11-10
No hay suficiente stock disponible. Stock actual: 3

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
        
Seleccione una opción: 11
Ingrese el ID del prestamo a devolver: 1

        --- Prestamo ---
        ID: 1
        Fecha: 2026-11-10 00:00:00
        Estado: Activo
        Cantidad: 2
        ID Estudiante: 1
        ID Equipo: 1
        
Prestamo devuelto

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
        
Seleccione una opción: 5

        --- Equipo ---
        ID: 1
        Nombre: Notebook UCT
        Tipo: Computador
        Stock disponible: 5
        

        --- Equipo ---
        ID: 2
        Nombre: Proyector
        Tipo: Proyector
        Stock disponible: 3
        

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
        
Seleccione una opción: 11
Ingrese el ID del prestamo a devolver: 1
El prestamo ya ha sido devuelto.

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
        
Seleccione una opción: 0
Saliendo del programa
(evaluacion) alpaca@alpaca-ASUS-TUF-Gaming-A15-FA506NCQ-FA506NCQ:~/Documents/evaluacion$ /home/alpaca/Documents/evaluacion/.venv/bin/python /home/alpaca/Documents/evaluacion/menu.py

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
        
Seleccione una opción: 2

        --- Estudiante ---
        ID: 1
        Nombre: Vicente
        Correo: vicente@gmail.com
        

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
        
Seleccione una opción: 0
Saliendo del programa
```
