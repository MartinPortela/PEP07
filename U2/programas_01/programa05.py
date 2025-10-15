#Escribe un programa que pida dos números y que indique cuál es el menor, cuál el mayor
#o que indique que son iguales.
print("Primer número")
num=float(input())
print("Segundo número")
num2=float(input())
match num:
    case num if num>num2:
        print(num,"es mayor que",num2)
    case num if num<num2:
        print(num,"es menor que",num2)
    case _:
        print("Los números son iguales")    