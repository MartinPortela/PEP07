#Escribe un programa que muestre los números pares que hay entre 0 y 10. Resuelve el
#ejercicio de 4 formas diferentes. Usando los bucles for y while sin y con la sentencia
#continue.

print("For sin continue: \n")
for i in range(0, 11):
    if((i%2)==0):
        print(i)

a=0

print("\nWhile sin continue: \n")
while(a<=10):
    if((a%2)==0):
        print(a)
    a+=1

print("\nFor con continue: \n")
for i in range(0, 11):
    if((i%2)!=0):
        continue
    else:
        print(i)

print("\nWhile con continue: \n")
b=0
while(b<=10):
    if((b%2!=0)):
        b+=1
        continue
    else:
        print(b)
        b+=1