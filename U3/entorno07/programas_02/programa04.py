#Escribe un programa que use un bucle while y le pida continuamente al usuario que
#introduzca un número hasta que ingrese 45 como la número de salida secreto, en cuyo
#caso el mensaje "¡Has dejado el bucle con éxito" debe imprimirse en la pantalla y el bucle
#debe terminar.
#Haz dos dos versiones del programa:
#Versión 1: Utiliza el concepto de ejecución condicional y la instrucción break. En
#este caso el bucle no evaluará ninguna condición, es decir, será un bucle infinito.

numero=0

while(numero>=0):
    print("Introduzca número")
    numero=int(input())
    if(numero==45):
        break

print("¡Has dejado el bucle con éxito!")
numero2=0

while(numero2!=45):
    print("Introduzca número")
    numero2=int(input())
print("¡Has dejado el bucle con éxito!")