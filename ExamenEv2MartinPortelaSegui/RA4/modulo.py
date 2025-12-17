def crear_inventario():
    inventario={}
    return inventario
def agregar_producto(inventario,codigo,nombre,precio_inicial):
    if(inventario.get(codigo)==None):
        precioTup=[precio_inicial]
        nombrelist=(f"{nombre}",precioTup)
        prod={f"{codigo}": nombrelist}
        inventario.update(prod)
        return True
    else:
        return False
def actualizar_precio(inventario,codigo,nuevo_precio):
    if(inventario.get(codigo)!=None):
        inventario.get(codigo)[1].append(nuevo_precio)
        return True
    else:
        return False
def obtener_producto(inventario,codigo):
    if(inventario.get(codigo)!=None):
        ultimo_indice=len(inventario.get(codigo)[1])-1
        cadena=f"PRODUCTO: {inventario.get(codigo)[0]} | PRECIO ACTUAL: {inventario.get(codigo)[1][ultimo_indice]}"
    else:
        cadena=""
    return cadena
def analizar_precios_producto(inventario,codigo):
    if(inventario.get(codigo)!=None):
        lista=sorted(inventario.get(codigo)[1])
    else:
        lista=[]
    return lista
        