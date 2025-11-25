from os import strerror
import json
paises=[]
try:
    with open("paises.json", "r", encoding="utf-8") as fichero_json:
        datos = json.load(fichero_json)
        comparar=input(("¿Qué continente será?"))
        for fila in datos:
            if(fila["continente"].lower()==comparar.lower()):
                print(f"{fila["nombre"]} está en {fila["continente"]} y tiene {fila["poblacion"]} millones de habitantes.")
                with open("paises_filtrados.json","w", encoding="utf-8") as paises_json:
                    json.dump(fila,paises_json,ensure_ascii=False, indent=4)
except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)