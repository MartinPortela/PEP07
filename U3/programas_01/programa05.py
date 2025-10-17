#Escribe un programa donde crees varias funciones y pruebes el ámbito de las variables
#en Python (globales, no locales y locales).


def mostrar():
    b=20 #local
    global a
    print(a)
    a=23
    print(a+b)
    print(a)
    c=22 #nonlocal, no cambiará la global
    print(c)
    return

a=15 #variable global
c=30 #variable global
mostrar()
print(c)
