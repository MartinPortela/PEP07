import random
#Escribe un programa para jugar a adivinar un número. En primer lugar la aplicación
#solicita genera un número aleatorio entre 1 y 20. A continuación va pidiendo números y va
#respondiendo si el número a adivinar es mayor o menor que el introducido. El programa
#termina cuando se acierta el número.
#Puedes generar el número usando la función random.randrange(1, 21) para
#obtener un número aleatorio entre 1 y 20 (para ello debes poner import random al inicio
#del programa).
#Mejora el programa de forma que el usuario tenga solo 3 intentos.

numero=random.randrange(1, 21)
cont=3
numero1=0
while(numero1!=numero and cont>0):
    print("Adivine el número del 1 al 21, solo tiene ",cont," intentos")
    numero1=int(input())
    cont=cont-1

if(numero1==numero):
    print("\nHa adivinado con éxito")
else:
    print("\nHa fallado")