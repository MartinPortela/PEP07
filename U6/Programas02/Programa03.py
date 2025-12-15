#Crea un módulo en python que implemete las siguienetes clases:
# Clase abstracta AnimalMarino con:
# Atributos de instancia: nombre.
# Define propiedades (get y set) para el atributo (usando decoradores @property)
# Método abstracto sonido()
# Método abstracto saluda()
# Subclase Delfin.
# Constructor __init__(self, nombre)
# Implementa los métodos abstractos.
# Método sonido(): muestra "Clicks y silbidos"
# Método saluda(): muestra algo como “Soy un delfin llamado
# Alex.”
# Subclase Tiburón.
# Constructor __init__(self, nombre)
# Implementa los métodos abstractos
# Método sonido(): muestra "No tiene un sonido audible
# característico"
# Método saluda(): muestra algo como ”Soy un tiburón
# llamado Mai.”
# Escribe un programa que importe el módulo y crre una función main que.
# Cree una lista con varios objetos Delfin y Tiburón.
# Recorra la lista y llame a los métodos saluda y sonido por cada objeto.

from abc import ABC, abstractmethod

class AnimalMarino(ABC):
    
    def __init__(self, nombre):
        self.__nombre = nombre
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if (isinstance(nuevo_nombre,str)):
            self.__nombre = nuevo_nombre
        else:    
            raise (TypeError("El nombre debe ser un string"))
          
    @abstractmethod
    def saluda(self):
        raise NotImplementedError
    
    @abstractmethod
    def sonido(self):
        raise NotImplementedError
    

class Delfin(AnimalMarino):

    def __init__(self, nombre):
        super().__init__(nombre)
        
    def saluda(self):
        print(f"Soy un delfin llamado {self.nombre}")

    def sonido(self):
        print("Clicks y silbidos")


class Tiburon(AnimalMarino):

    def __init__(self, nombre):
        super().__init__(nombre)
        
    def saluda(self):
        print(f"Soy un tiburon llamado {self.nombre}")

    def sonido(self):
        print("No tiene un sonido audible característico")

def main():
    try:

        animal1 = Delfin("Flipper")
        animal2 = Tiburon("Tiburon Blanco")
        animal3 = Delfin("Alex")
        animal4 = Tiburon("Mai")

        animales=[animal1, animal2, animal3, animal4]
        for animal in animales:
            animal.saluda()
            animal.sonido()

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()