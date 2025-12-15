from Programa05 import AnimalTerrestre, Mamifero, Ave
from Programa03 import AnimalMarino, Tiburon

class Veterinario:
    def __init__(self,nombre):
        self.__nombre=nombre
    @property
    def nombre(self):
        return self.__nombre
    @nombre.getter
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo):
        self.__nombre=nuevo
    def revisar(self,animal):
        print(f"Revisando a {animal.nombre}")

class ReservaNatural:
    def __init__(self,lista_animales):
        self.lista_animales=lista_animales
    def añadir(self, animal):
        self.lista_animales.append(animal)
        
class Corazon:
    def __init__(self,tamaño):
        self.tamaño=tamaño

    def latidos(self):
        print("Estoy latiendo")
class Pulmones:
    def __init__(self,tamaño):
        self.tamaño=tamaño

    def respira(self):
        print("Estoy respirando")
class Tiburon(AnimalMarino):
    def __init__(self,nombre):
        super().__init__(nombre)
        self.corazon=Corazon("Grandes")
        self.pulmones=Pulmones("Grandes")
    def nadar(self):
        self.corazon.latidos()
        self.pulmones.respira()
        print("El tiburón está nadando")
    def saluda(self):
        print(f"Soy un tiburon llamado {self.nombre}")

    def sonido(self):
        print("No tiene un sonido audible característico")
    
def main():
    try:
        
        # Dependencia
        vet = Veterinario("Laura")
        animal = AnimalTerrestre("Kuma", 5, 120)
        vet.revisar(animal)

        # Agregación
        reserva = ReservaNatural([])
        reserva.añadir(animal)

        # Composición
        tiburon = Tiburon("Mai")
        tiburon.nadar()


    except Exception as e:
        print(e)
if __name__ == "__main__":
    main()