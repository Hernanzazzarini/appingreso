import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta
from tabulate import tabulate
from conexion import create_db_connection, close_db_connection

def calcular_tiempo_transcurrido(horario_ingreso, horario_salida):
    formato_fecha = "%Y-%m-%d %H:%M:%S"

    if horario_salida:
        inicio = datetime.strptime(horario_ingreso, formato_fecha)
        fin = datetime.strptime(horario_salida, formato_fecha)
        diferencia = fin - inicio
        return str(diferencia)
    else:
        return None

def crear_ingreso(conexion, id_persona, id_sector):
    try:
        cursor = conexion.cursor()

        horario_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        horario_salida = None

        query = "INSERT INTO ingreso (id_persona, id_sector, horario_ingreso, horario_salida) VALUES (%s, %s, %s, %s)"
        data = (id_persona, id_sector, horario_ingreso, horario_salida)
        cursor.execute(query, data)

        conexion.commit()

        print("Ingreso creado exitosamente.")

    except Error as e:
        print(f"Error al crear ingreso: {e}")

    finally:
        if cursor:
            cursor.close()

def actualizar_salida(conexion, id_persona):
    try:
        cursor = conexion.cursor()

        horario_salida = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        query = "UPDATE ingreso SET horario_salida = %s WHERE id_persona = %s AND horario_salida IS NULL"
        data = (horario_salida, id_persona)
        cursor.execute(query, data)

        conexion.commit()

        print("Salida registrada exitosamente.")

    except Error as e:
        print(f"Error al actualizar salida: {e}")

    finally:
        if cursor:
            cursor.close()

def obtener_ingresos_persona(conexion, id_persona):
    try:
        cursor = conexion.cursor(dictionary=True)

        query = """
            SELECT
                ingreso.id,
                personal.nombre_persona,
                sector.nombre_sector,
                ingreso.horario_ingreso,
                ingreso.horario_salida,
                TIMEDIFF(ingreso.horario_salida, ingreso.horario_ingreso) as tiempo_transcurrido
            FROM
                ingreso
                JOIN personal ON ingreso.id_persona = personal.id
                JOIN sector ON ingreso.id_sector = sector.id
            WHERE
                ingreso.id_persona = %s
        """
        data = (id_persona,)
        cursor.execute(query, data)

        ingresos = cursor.fetchall()

        if ingresos:
            headers = ["ID", "Nombre Persona", "Nombre Sector", "Horario Ingreso", "Horario Salida", "Tiempo Transcurrido"]
            table = [
                [
                    ingreso['id'],
                    ingreso['nombre_persona'],
                    ingreso['nombre_sector'],
                    ingreso['horario_ingreso'],
                    ingreso['horario_salida'],
                    ingreso['tiempo_transcurrido']
                ]
                for ingreso in ingresos
            ]
            print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
        else:
            print(f"No hay ingresos registrados para la persona con ID {id_persona}.")

    except Error as e:
        print(f"Error al obtener ingresos: {e}")

    finally:
        if cursor:
            cursor.close()

def menu(conexion):
    while True:
        print("\n--- Menú ---")
        print("1. Registrar ingreso")
        print("2. Registrar salida")
        print("3. Obtener ingresos de una persona")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id_persona = input("ID de la persona: ")
            id_sector = input("ID del sector: ")
            crear_ingreso(conexion, id_persona, id_sector)

        elif opcion == "2":
            id_persona = input("ID de la persona: ")
            actualizar_salida(conexion, id_persona)

        elif opcion == "3":
            id_persona = input("ID de la persona: ")
            obtener_ingresos_persona(conexion, id_persona)

        elif opcion == "4":
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
