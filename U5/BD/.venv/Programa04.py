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
    sql="SELECT nombre from ciudades WHERE poblacion_millones>25"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
except Error as e:
    if(e.errno==1050):
        print("Tabla repetida")
    else:
        print(f" Error con MySQL: {e}")
finally:
    cursor.close()
    conexion.close()