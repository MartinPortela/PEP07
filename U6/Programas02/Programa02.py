
#Amplia el programa anterior para que la función main:
# 
# Cree una lista con varios objetos Mamifero y Ave.
# 
# Recorra la lista y llame a saluda por cada objeto.
class AnimalTerrestre:
    
    def __init__(self, nombre, edad, peso):
        self.__nombre = nombre
        self.__edad = edad
        self.__peso = peso
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if (isinstance(nuevo_nombre,str)):
            self.__nombre = nuevo_nombre
        else:    
            raise (TypeError("El nombre debe ser un string"))

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self,nueva_edad):
        if (nueva_edad < 0):
            raise ValueError("La edad debe ser positiva")
        else:
            self.__edad=nueva_edad


    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self,nuevo_peso):
        if (nuevo_peso < 0):
            raise ValueError("El peso debe ser positivo")
        else:
            self.__peso=nuevo_peso
        
    def saluda(self):
        print(f"Soy un animal terrestre llamado {self.nombre} y tengo {self.edad} años ")   
    
     
class Mamifero(AnimalTerrestre):

    def __init__(self, nombre, edad, peso, gestacion_dias):
        super().__init__(nombre, edad, peso)
        self.__gestacion_dias = gestacion_dias

    @property
    def gestacion_dias(self):
        return self.__gestacion_dias
    
    @gestacion_dias.setter
    def gestacion_dias(self,nueva_gestacion_dias):
        if (nueva_gestacion_dias < 0):
            raise ValueError("Los días de gestación deben ser positivos")
        else:
            self.__gestacion_dias=nueva_gestacion_dias

    def saluda(self):
        print(f"Soy un mamimefero llamado {self.nombre}, tengo {self.edad} años  y mi gestación es de {self.__gestacion_dias}")

class Ave(AnimalTerrestre):

    def __init__(self, nombre, edad, peso, puede_volar):
        super().__init__(nombre, edad, peso)
        self.__puede_volar = puede_volar

    @property
    def puede_volar(self):
        return self.__puede_volar
    
    @puede_volar.setter
    def puede_volar(self,nueva_puede_volar):
            self.__puede_volar=nueva_puede_volar

    def saluda(self):
        print(f"Soy un ave llamado {self.nombre}, tengo {self.edad} años")
        if (self.__puede_volar):
            print(" y puedo volar")
        else:
            print(" y no puedo volar")
                            
try:

    animal1 = AnimalTerrestre("Kuma",10, 100)
    animal2 = AnimalTerrestre("Miu", 5,  6)
    animal3 = Mamifero("Log", 10, 90, 200)
    animal4 = Ave("Uff", 4, 3, False)

    animal1.saluda()
    animal2.saluda()
    animal3.saluda()
    animal4.saluda()

    animal5 = [animal1,animal2,animal3,animal4]
    for animal in animal5:
        animal.saluda()
    print(animal1) 


except Exception as e:
    print(e)