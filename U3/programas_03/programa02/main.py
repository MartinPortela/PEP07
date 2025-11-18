import operaciones
def main():
    """Función principal del programa"""
    print("Hola, este es el programa principal")
    print("Introduzca los números para sus operaciones en orden: ")
    print("Primer número: ")
    a=float(input())
    print("Segundo número: ")
    b=float(input())
    print(operaciones.suma(a,b))
    print("\n")
    print(operaciones.resta(a,b))
    print("\n")
    print(operaciones.multiplicacion(a,b))
    print("\n")
    print(operaciones.division(a,b))
if __name__ == "__main__":
    main()