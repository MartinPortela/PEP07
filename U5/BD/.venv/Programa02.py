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
    sql="CREATE TABLE ciudades (id INT AUTO_INCREMENT PRIMARY KEY,nombre VARCHAR(100) NOT NULL,pais VARCHAR(50),poblacion_millones FLOAT);"
    cursor.execute(sql)
    print("Tabla creada correctamente")
except Error as e:
    if(e.errno==1050):
        print("Tabla repetida")
    else:
        print(f" Error con MySQL: {e}")
finally:
    cursor.close()
    conexion.close()

