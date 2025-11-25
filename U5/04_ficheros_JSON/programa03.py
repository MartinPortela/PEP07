import json
cadena_json = '''
[
{"nombre": "Chile", "moneda": "Peso chileno"},
{"nombre": "Egipto", "moneda": "Libra egipcia"}
]
'''
data = json.loads(cadena_json)
print(type(data))
for fila in data:
    print(f"{fila["nombre"]} su moneda es {fila["moneda"]}")