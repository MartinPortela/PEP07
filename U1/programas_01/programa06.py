#Escribe un programa que use varias veces la función printf() para

#Mostrar las operaciones del los operadores aritméticos de Python entre dos
#números.

#Mostrar las operaciones de los operadores lógicos de Python con valores
#booleanos.

#Mostrar las operaciones de los operadores de comparación de Python con valores
#booleanos y/o números.

a=5
b=6

print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} & {b} = {a&b}")
print(f"{a} ** {b} = {a**b}\n\n")

x=True
y=False

print(f"{x} and {y} {x and y}")
print(f"{x} or {y} {x or y}")
print(f"not {x} {not x}\n\n")

print(f"{a} == {b} {a==b}")
print(f"{a} != {b} {a!=b}")
print(f"{a} > {b} {a>b}")
print(f"{a} < {b} {a<b}")
print(f"{a} >= {b} {a>=b}")
print(f"{a} <= {b} {a<=b}")