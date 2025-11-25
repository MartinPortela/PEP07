from os import strerror
import json

try:
    capitales = [
    {"país": "Francia", "capital": "París"},
    {"país": "Australia", "capital": "Canberra"},
    {"país": "Kenia", "capital": "Nairobi"},
    {"país": "Brasil", "capital": "Brasilia"}
    ]
    with open ("capitales.json","w")as fichero_json:
        json.dump(capitales, fichero_json,ensure_ascii=False, indent=4)
    print("Archivo 'capitales.json' creado correctamente.")
except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)