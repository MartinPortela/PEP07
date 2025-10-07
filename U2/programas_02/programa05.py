#Escribe un programa que pida un número y muestre una lista de números desde 1 al
#número. Se debe controlar que el número no se menor que 1 ni mayor que 10, si es así se
#pedirá que si introduzca de nuevo, y así hasta que se introduzca el número correcto.

print("Introduzca un número del 1 al 10")
numero=int(input())
while (numero<1 or numero>10):
    print("Rango no válido, solo del 1 al 10")
    numero=int(input())
for i in range(1, numero+1):
    print("\n",i,"\n")
