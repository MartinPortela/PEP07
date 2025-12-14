import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
    host="localhost",
    user="ciudades",
    password="ciudades",
    database="ciudades",
    )

    print("Conexión establecida correctamente")
except Error as e:
    print(f" Error con MySQL: {e}")
finally:
    conexion.close()