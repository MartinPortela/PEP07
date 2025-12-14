class Animal:
    def __init__(self, nombre, especie, edad, id_chip):
        self.nombre=nombre
        self.especie=especie
        self.edad=edad
        self.__id_chip=id_chip
    def saludar(self):
        print(f"Soy un {self.especie} llamado {self.nombre} y tengo {self.edad} años")
    def cumplir_anios(self):
        self.edad=self.edad+1
    def get_id_chip(self):
        return self.__id_chip
    def set_id_chip(self, nuevo_id):
        if not isinstance(nuevo_id, str):
            raise TypeError("El id_chip debe ser una cadena de texto")

        if nuevo_id.strip() == "":
            raise ValueError("El id_chip no puede estar vacío")

        self.__id_chip = nuevo_id
def main():
    animal1= Animal("Kuma","Tigre",10, "a123")
    animal2= Animal("Miu","Gato",5, "a456")
    animal1.set_id_chip("ABC123")
    animal1.saludar()
    animal1.cumplir_anios()
    animal1.edad=animal1.edad+1
    animal1.saludar()
    print(animal1.get_id_chip())

if __name__ == "__main__":
    main()