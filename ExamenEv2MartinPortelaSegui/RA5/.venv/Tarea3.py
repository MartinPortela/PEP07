import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
    host="localhost",
    user="planetas",
    password="planetas",
    database="planetas",
    )
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE planetas (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255) NOT NULL, tipo VARCHAR(50), lunas INT);")
    sql="INSERT INTO planetas (nombre,tipo,lunas) VALUES ('Venus','Rocoso',0)"
    sql2="INSERT INTO planetas (nombre,tipo,lunas) VALUES ('Júpiter','Gaseoso',79)"
    cursor.execute(sql)
    cursor.execute(sql2)
    print(cursor.rowcount)
    sql3="SELECT * from planetas WHERE id=1"
    cursor.execute(sql3)
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    cursor.close()
    conexion.close()
except Error as e:
    print(f" Error con MySQL: {e}")