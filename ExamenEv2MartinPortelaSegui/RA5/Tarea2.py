import json
planetas = [
    {"Nombre": "Marte", "Tipo": "Rocoso", "Lunas": 2},
    {"Nombre": "Júpiter", "Tipo": "Gaseoso", "Lunas": 79},
    {"Nombre": "Venus", "Tipo": "Rocoso", "Lunas": 0}
    ]
with open ("planetas.json","w")as fichero_json:
        json.dump(planetas, fichero_json,ensure_ascii=False, indent=4)
with open("planetas.json","r")as fichero_json:
        datos = json.load(fichero_json)
        for fila in datos:
            print(f"{fila["Nombre"]} es un planeta {fila["Tipo"]} y tiene {fila["Lunas"]} lunas.")