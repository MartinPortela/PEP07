from os import strerror
import csv

try:
    with open("ciudades.csv") as fichero_csv:
        reader = csv.reader(fichero_csv, delimiter=",")
        for fila in reader:
            if(fila[0]!="Ciudad"):
                print(f"La ciudad de {fila[0]} está en {fila[1]} y tiene {fila[2]} millones de habitantes.")
except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)