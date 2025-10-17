#Escribe un programa que pida primero un número par (positivo o negativo) y si el valor no
#es correcto, muestre un aviso. Si el valor es correcto, pedirá un número impar (positivo o
#negativo) y si el valor no es correcto, mostrará un aviso.

print("Intrdozuca un número par: ")
par=int(input())
if(par%2!=0):
    print("No ha sido un número par")
else:
    print("Intrdozuca un número impar: ")
    impar=int(input())
    if(impar%2==0):
        print("No ha sido un número impar")