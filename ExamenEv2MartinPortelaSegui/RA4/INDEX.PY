from modulo import crear_inventario, agregar_producto, actualizar_precio,obtener_producto,analizar_precios_producto

inventario=crear_inventario()
agregar_producto(inventario,"P01","Martin",500)
agregar_producto(inventario,"P02","Portela",600)
agregar_producto(inventario,"P02","Portela",600)
actualizar_precio(inventario,"P01",400)
actualizar_precio(inventario,"P02",300)
print(obtener_producto(inventario,"P02"))
lista=analizar_precios_producto(inventario,"P02")
print(lista)