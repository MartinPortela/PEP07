from os import strerror
import csv

try:
    with open("ciudades.csv") as fichero_csv:
        reader = csv.DictReader(fichero_csv)
        cabeceras = reader.fieldnames
        print(f"Los nombres de las columnas son {cabeceras}")
        for fila in reader:
            if(fila[cabeceras[0]]!="Ciudad"):
                print(f"{fila[cabeceras[0]]} ({fila[cabeceras[1]]}) tiene una población aproximada de {fila[cabeceras[2]]} millones.")
except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)