#Escribe un programa que realice las siguientes operaciones:

#Leer por teclado un número comprendido entre 1 y 10. Se vuelve a pedir hasta que
#no se introduzca el número correcto.

#Una vez que ha leído el número se tiene que mostrar su tabla de multiplicar.

#Después de mostrar la tabla de multiplicar se tiene que preguntar al usuario si
#desea introducir otro número o no. Si el usuario selecciona que quiere continuar el
#programa tendrá que volver a ejecutarse y repetir los mismos pasos. Si el usuario
#indica que no quiere continuar el programa finaliza.
comprobar=True
while(comprobar):
    print("Introduzca un número del 1 al 10")
    numero=int(input())
    while (numero<1 or numero>10):
        print("Rango no válido, solo del 1 al 10")
        numero=int(input())
    print("Tabla de multiplicar:\n")
    for i in range(1, 11):
        print(numero,"*",i,"=",numero*i,"\n")
    print("¿Desea continuar? Pulse 0 en caso negativo y 1 en caso positivo: ")
    comprobar=int(input())