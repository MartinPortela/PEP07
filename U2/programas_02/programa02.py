#Escribe un que lea por teclado un número comprendido entre 1 y 10. No se dejara de
#pedir el número hasta que no se introduzca correctamente.

numero=0

while(type(numero)!=int or numero<1 or numero>10):
    print("Introduzca un número entre 1 y 10 solamente: ")
    numero=int(input())
print("El número que ha puesto es ",numero)