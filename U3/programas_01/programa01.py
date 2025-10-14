#Escribe un programa en Python que haga uso de una función llamada saludar que cumpla
#los siguientes requisitos:
#Entrada: Tiene 3 parámetros de entrada, que serán 3 cadenas de texto: nombre,
# primer apellido, segundo apellido
# Salida: No tiene parámetros de salida.
# Funcionalidad: Imprime por pantalla un mensaje saludando a la persona en función
# de los parámetros de entrada.

print("Introduzca su nombre: ")
nombre=input()
print("Introduzca su primer apellido: ")
apellido=input()
print("Introduzca su segundo apellido: ")
apellido2=input()
def saludar(nombre, apellido, apellido2):
    print(nombre,apellido,apellido2)

saludar(nombre,apellido,apellido2)
