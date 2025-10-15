#Escribe un programa que lea por teclado un número real entre 1 y 10, simulando una
#nota numérica, y muestre un mensaje indicando la calificación obtenida teniendo en
#cuenta los siguientes rangos:
#Insuficiente: [0, 5)
# Suficiente: [5, 6)
# Bien: [6, 7)
# Notable: [7, 9)
# Sobresaliente: [9, 10]
# Si el número introducido no está en ninguno de los rangos anteriores debe mostrar un
# mensaje de error indicando que la nota no es válida.
# Hay que usar la estructura match.

print("Introduzca un número del 0 al 10")
num=float(input())
match num:
    case nota if 0 <= nota < 5:
        print("Insuficiente")
    case nota if 5 <= nota < 6:
        print("Suficiente")
    case nota if 6 <= nota < 7:
        print("Bien")
    case nota if 7 <= nota < 9:
        print("Notable")
    case nota if 9 <= nota <= 10:
        print("Sobresaliente")
    case _ :
        print("No ha introducido una nota válida")