import mysql.connector
from mysql.connector import Error
from tabulate import tabulate
from conexion import create_db_connection, close_db_connection

def crear_sector(conexion, nombre_sector):
    try:
        cursor = conexion.cursor()

        query = "INSERT INTO sector (nombre_sector) VALUES (%s)"
        data = (nombre_sector,)
        cursor.execute(query, data)

        conexion.commit()

        print("Sector creado exitosamente.")

    except Error as e:
        print(f"Error al crear sector: {e}")

    finally:
        if cursor:
            cursor.close()

def obtener_sectores(conexion):
    try:
        cursor = conexion.cursor(dictionary=True)

        query = "SELECT * FROM sector"
        cursor.execute(query)

        sectores = cursor.fetchall()

        if sectores:
            headers = ["ID", "Nombre"]
            table = [[sector['id'], sector['nombre_sector']] for sector in sectores]
            print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
        else:
            print("No hay sectores registrados.")

    except Error as e:
        print(f"Error al obtener sectores: {e}")

    finally:
        if cursor:
            cursor.close()

def menu(conexion):
    while True:
        print("\n--- Menú ---")
        print("1. Crear sector")
        print("2. Obtener sectores")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre_sector = input("Nombre del sector: ")
            crear_sector(conexion, nombre_sector)

        elif opcion == "2":
            obtener_sectores(conexion)

        elif opcion == "3":
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    try:
        conexion = create_db_connection()

        if conexion:
            print("Conexión a la base de datos exitosa")
            menu(conexion)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if conexion:
            close_db_connection(conexion)
