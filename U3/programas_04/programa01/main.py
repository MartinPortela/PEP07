from matematicas import operaciones
from matematicas import conversiones
from matematicas import figuras

def main():
    """Función principal del programa"""
    print("Hola, este es el programa principal")
    print("Presione 1 para operaciones matemáticas y 2 para cálculo de áreas geométricas")
    opcion=int(input())
    match opcion:
        case 1:
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
        case 2:
            print("Introduzca base y altura para rectángulo, en ese orden: ")
            base=float(input())
            altura=float(input())
            print(figuras.area_rectangulo(base, altura))
            print("\n")
            print("Introduzca base y altura para triángulo, en ese orden: ")
            base=float(input())
            altura=float(input())
            print(figuras.area_triangulo(base, altura))
            print("\n")
            print("Introduzca radio para círculo: ")
            radio=float(input())
            print(figuras.area_circulo(radio))
            print("\n")
if __name__ == "__main__":
    main()