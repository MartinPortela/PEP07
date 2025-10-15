#Escribe un programa que pida primero un número par y luego un número impar (positivos
#o negativos). En caso de que uno o los dos valores no sea correcto (es decir no sea par o
#impar respectivamente), se mostrará un aviso.

print("Intrdozuca un número par: ")
par=int(input())
if(par%2!=0):
    print("No ha sido un número par")
print("Intrdozuca un número impar: ")
impar=int(input())
if(impar%2==0):
    print("No ha sido un número impar")