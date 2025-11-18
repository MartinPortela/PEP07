def a_binario(n):
    binario=f"{bin(n)}"
    return binario
def a_hexadecimal(n):
    binario=f"{hex(n)}"
    return binario
def a_entero(texto):
    if(texto.isnumeric()):
        cadena=int(texto)
        return cadena
    else:
        print("No se puede convertir")