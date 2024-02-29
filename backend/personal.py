import mysql.connector
from mysql.connector import Error
from conexion import create_db_connection, close_db_connection
from tabulate import tabulate

def validar_nombre(nombre):
    if not nombre or not nombre.strip():
        print("Error: El nombre no puede estar vacío.")
        return False
    return True

def validar_telefono(telefono):
    # Aquí puedes implementar lógica de validación específica para números de teléfono
    if not telefono or not telefono.strip():
        print("Error: El teléfono no puede estar vacío.")
        return False
    return True

def validar_dni(dni):
    # Aquí puedes implementar lógica de validación específica para números de DNI
    if not dni or not dni.strip():
        print("Error: El DNI no puede estar vacío.")
        return False
    return True

def crear_personal(conexion):
    nombre = input("Nombre: ")
    while not validar_nombre(nombre):
        nombre = input("Nombre: ")

    telefono = input("Teléfono: ")
    while not validar_telefono(telefono):
        telefono = input("Teléfono: ")

    dni = input("DNI: ")
    while not validar_dni(dni):
        dni = input("DNI: ")

    try:
        cursor = conexion.cursor()

        # Utilizar parámetros en lugar de concatenación de cadenas
        query = "INSERT INTO personal (nombre_persona, telefono, dni) VALUES (%s, %s, %s)"
        data = (nombre, telefono, dni)
        cursor.execute(query, data)

        # Confirmar la transacción
        conexion.commit()

        print("Registro de personal creado exitosamente.")

    except Error as e:
        print(f"Error al crear registro de personal: {e}")

    finally:
        if cursor:
            cursor.close()

def obtener_personas(conexion):
    try:
        cursor = conexion.cursor(dictionary=True)

        query = "SELECT * FROM personal"
        cursor.execute(query)

        personas = cursor.fetchall()

        if personas:
            # Utilizar tabulate para imprimir la tabla
            headers = ["ID", "Nombre", "Teléfono", "DNI"]
            table = [[persona['id'], persona['nombre_persona'], persona['telefono'], persona['dni']] for persona in personas]

            print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
        else:
            print("No hay personas registradas.")

    except Error as e:
        print(f"Error al obtener personas: {e}")

    finally:
        if cursor:
            cursor.close()

def menu(conexion):
    while True:
        print("\n--- Menú ---")
        print("1. Crear persona")
        print("2. Obtener personas")
       
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            with create_db_connection() as conexion:
                crear_personal(conexion)

        elif opcion == "2":
            with create_db_connection() as conexion:
                obtener_personas(conexion)
                
        elif opcion == "3":
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    try:
        with create_db_connection() as conexion:
            if conexion:
                menu(conexion)
    except Exception as e:
        print(f"Error: {e}")
