#Escribe un programa que pida dos numero y muestre su división. Se deben tener en
#cuenta que no se puede dividir por 0 mostrando en ese caso un aviso.
print("Introduzca el dividendo: ")
primero=float(input())
print("Introduzca el divisor: ")
segundo=float(input())
if(segundo==0):
    print("No se puede dividir entre 0")
else:
    print("División:",primero/segundo)