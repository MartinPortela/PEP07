class Animal:
    def __init__(self, nombre, especie, edad, id_chip, peso):
        self.nombre=nombre
        self.especie=especie
        self.edad=edad
        self.__id_chip=id_chip
        self.__peso=peso
    def saludar(self):
        print(f"Soy un {self.especie} llamado {self.nombre} y tengo {self.edad} años")
    def cumplir_anios(self):
        self.edad=self.edad+1
    @property
    def id_chip(self):
        return self.__id_chip
    @id_chip.getter    
    def id_chip(self):
        return self.__id_chip
    @id_chip.setter
    def id_chip(self, nuevo_id):
        if not isinstance(nuevo_id, str):
            raise TypeError("El id_chip debe ser una cadena de texto")

        if nuevo_id.strip() == "":
            raise ValueError("El id_chip no puede estar vacío")

        self.__id_chip = nuevo_id
    @property
    def peso(self):
        return self.__peso
    @peso.getter
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, nuevo_peso):
        self.__peso=nuevo_peso
    @peso.deleter
    def peso(self):
        del(self.__peso)
def main():
    animal1= Animal("Kuma","Tigre",10, "a123",1)
    animal2= Animal("Miu","Gato",5, "a456",50)
    animal1.saludar()
    animal1.cumplir_anios()
    animal1.edad=animal1.edad+1
    animal1.saludar()
    print(animal2.peso)
    animal2.peso=40
    print(animal2.peso)
    del animal2.peso
if __name__ == "__main__":
    main()