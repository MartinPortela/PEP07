from os import strerror
import csv

patrimonios = [
{"Ciudad": "Roma", "País": "Italia", "Lugar emblemático": "Coliseo"},
{"Ciudad": "El Cairo", "País": "Egipto", "Lugar emblemático": "Pirámides de Guiza"},
{"Ciudad": "Kioto", "País": "Japón", "Lugar emblemático": "Templos históricos"}
]
fieldnames=["Ciudad", "País", "Lugar emblemático"]
try:
    with open("patrimonios.csv", "w") as fichero_csv:
        writer = csv.DictWriter(fichero_csv, fieldnames=fieldnames,
        delimiter=";") 
        writer.writeheader() 
        writer.writerows(patrimonios)
    print("Archivo 'patrimonios.csv' generado correctamente.")
except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)