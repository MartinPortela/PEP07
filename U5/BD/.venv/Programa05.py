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
    sql='INSERT INTO ciudades (nombre, pais, poblacion_millones) VALUES ("Madrid", "España", 6.8);'
    sql2="DELETE FROM ciudades WHERE poblacion_millones < 10;"
    cursor.execute(sql)
    conexion.commit()
    print(f"Se han puesto filas")
except Error as e:
    if(e.errno==1050):
        print("Tabla repetida")
    else:
        print(f"Transacción revertida por error: {e}")
    conexion.rollback()
finally:
    cursor.close()
    conexion.close()
