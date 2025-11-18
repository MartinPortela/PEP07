import operaciones

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