#Escribe un programa que pida números hasta que se introduzca un cero. Debe imprimir la
#suma y la media de todos los números introducidos. Realiza dos versiones: una que utiliza
#la instrucción break y otra no.
cont=0
suma=0
print("Introduzca números, excepto el 0")
numero=int(input())
while(numero!=0):
    cont+=1
    suma+=numero
    print("Introduzca números, excepto el 0")
    numero=int(input())

print("Suma: ",suma,"\nMedia: ",suma/cont)

cont=0
suma=0
print("Introduzca números, excepto el 0")
numero=int(input())
while(numero>=0):
    cont+=1
    suma+=numero
    print("Introduzca números, excepto el 0")
    numero=int(input())
    if(numero==0):
        break

print("Suma: ",suma,"\nMedia: ",suma/cont)