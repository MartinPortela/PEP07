import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
    host="localhost",
    user="series",
    password="series",
    database="series",
    )
    cursor = conexion.cursor()

    sql = "INSERT INTO series (titulo, genero) VALUES ('Breaking Bad', 'Drama')"
    cursor.execute(sql)
    
    conexion.commit()

    print(cursor.rowcount, "fila insertada.")
    cursor.close()
    conexion.close()
except Error as e:
    print(f" Error con MySQL: {e}")