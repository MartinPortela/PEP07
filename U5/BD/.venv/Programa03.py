import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
    host="localhost",
    user="ciudades",
    password="ciudades",
    database="ciudades",
    )
    cursor=conexion.cursor()
    num1=cursor.rowcount
    datos = [
    ("Tokio", "Japón", 37.4),
    ("Delhi", "India", 30.3),
    ("Shanghái", "China", 27.1),
    ("São Paulo", "Brasil", 22.0),
    ("Ciudad de México", "México", 21.7)
    ]
    sql="INSERT INTO ciudades (nombre, pais, poblacion_millones) VALUES (%s, %s, %s);"
    cursor.executemany(sql,datos)
    conexion.commit()
    num2=cursor.rowcount-num1-1
    print(f"Se han puesto {num2} filas")
except Error as e:
    if(e.errno==1050):
        print("Tabla repetida")
    else:
        print(f" Error con MySQL: {e}")
finally:
    cursor.close()
    conexion.close()
