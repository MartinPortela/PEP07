class Animal:
    def __init__(self, nombre, especie, edad):
        self.nombre=nombre
        self.especie=especie
        self.edad=edad
    def saludar(self):
        print(f"Soy un {self.especie} llamado {self.nombre} y tengo {self.edad} años")
    def cumplir_anios(self):
        self.edad=self.edad+1

def main():
    animal1= Animal("Kuma","Tigre",10, )
    animal2= Animal("Miu","Gato",5)

    animal1.saludar()
    animal1.cumplir_anios()
    animal1.edad=animal1.edad+1
    animal1.saludar()
    animal2.saludar()

if __name__ == "__main__":
    main()