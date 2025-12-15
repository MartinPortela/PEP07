from abc import ABC, abstractmethod
import random
class Personaje(ABC):
    def __init__(self,nombre,vida):
        self.__nombre=nombre
        self.__vida=vida
    @property
    def nombre(self):
        return self.__nombre
    @property
    def vida(self):
        return self.__vida
    @vida.setter
    def vida(self,otro):
        self.__vida=max(0, otro)
    @property
    def vivo(self):
        return self.__vida > 0
    @abstractmethod
    def atacar(self, objetivo):
        raise NotImplementedError

class Arma:
    def __init__(self,nombre,danio):
        self.__nombre=nombre
        self.__danio=danio
    
    @property
    def nombre(self):
        return self.__nombre
    @property
    def danio(self):
        return self.__danio

class Guerrero(Personaje):
    def __init__(self, nombre, vida,arma):
        super().__init__(nombre, vida)
        self.__arma=arma
    
    @property
    def arma(self):
        return self.__arma
    
    def atacar(self,objetivo):
        danio = self.__arma.danio + random.randint(0, 5)
        objetivo.vida -= danio
        print(f"{self.nombre} causa {danio} de daño.")
class Mago(Personaje):
    def __init__(self, nombre, vida, hechizos):
        super().__init__(nombre, vida)
        self._hechizos = hechizos
    @property
    def hechizos(self):
        return self._hechizos
    def atacar(self, objetivo):
        danio = random.choice(list(self.hechizos.values()))
        objetivo.vida-=danio
        print(f"{self.nombre} causa {danio} de daño.")

def combate(personaje1, personaje2):
            print(f"{personaje1.nombre} tiene {personaje1.vida} \n")
            print(f"{personaje2.nombre} tiene {personaje2.vida} \n")
            while(personaje1.vivo and personaje2.vivo):
                personaje1.atacar(personaje2)
                if(personaje2.vivo):
                    personaje2.atacar(personaje1)
            if(personaje1.vivo):
                print(f"El ganador es el jugador 1 con {personaje1.vida} de vida restante")
            else:
                print(f"El ganador es el jugador 2 con {personaje2.vida} de vida restante")
    
def main():
    try:
        espada = Arma("Espada larga", 15)
        guerrero = Guerrero("Arthur", 100, espada)

        mago = Mago("Merlin", 80, {
            "Bola de fuego": 25,
            "Rayo": 22,
            "Hielo": 20
        })

        combate(guerrero, mago)
        

    except Exception as e:
        print(e)
if __name__ == "__main__":
    main()