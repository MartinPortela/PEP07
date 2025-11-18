#Escribe un programa para jugar a una versión muy simplificada del black jack. En primer
#lugar el ordenador obtendrá un número aleatorio entre 17 y 21 (está será su jugada). A
#continuación el jugador ira sacando cartas (con valores entre 1 y 5), que se irán sumando
#para obtener su puntuación, hasta que el quiera. Si se pasa de 21 pierde, si obtiene una
#puntuación igual o menor que la banca pierde, y si obtiene una puntuación superior a la
#banca gana.
import random
ordenador=random.randrange(17, 22)
numero=0
comprobar=1
while(comprobar):
    numero+=random.randrange(1, 6)
    print("Su suma actual es ",numero,". Presione 0 si quiere parar y 1 si quiere seguir\n")
    comprobar=int(input())
if(numero>ordenador and numero<=21):
    print("Has ganado")
else: 
    if(numero>21):
        print("Es mayor que 21 ha perdido")
    else:
        print("Menor que la banca, ha perdido")