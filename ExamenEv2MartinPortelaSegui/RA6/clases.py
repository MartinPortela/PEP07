from abc import ABC, abstractmethod
class Producto(ABC):
    def __init__(self,nombre,precios):
        self.__nombre=nombre
        self.__precios=[precios]
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nuevo):
        self.__nombre=nuevo
    @property
    def precio_actual(self):
        ultimo_indice = len(self.__precios) - 1
        return self.__precios[ultimo_indice]
    def añadir_precio(self,precio):
        if(precio>=0):
            self.__precios.append(precio)
        else:
            print("No se permiten precios negativos")
    @abstractmethod
    def calcular_precio_final(self):
        raise NotImplementedError

class DiscoDuro(Producto):
    def __init__(self, nombre,tipo,precios):
        super().__init__(nombre,precios)
        self.__nombre=nombre
        self.__precios=[]
        self.__tipo=tipo
    def calcular_precio_final(self):
        if(self.__tipo=="SSD"):
            precio=(self.precio_actual*0.20)+self.precio_actual
            return precio
        else:
            return precio
    def __str__(self):
        return f"Nombre: {self.__nombre} Tipo: {self.__tipo}"

class Memoria(Producto):
    def __init__(self, nombre, capacidad,precios):
        super().__init__(nombre,precios)
        self.__nombre=nombre
        self.__precios=[]
        self.__capacidad=capacidad
    def calcular_precio_final(self):
        if(self.__capacidad==16):
            precio=(self.precio_actual*0.50)+self.precio_actual
            return precio
        else:
            return precio
    def __str__(self):
        return f"Nombre: {self.__nombre} Tipo: {self.__capacidad}"

def main():
    try:

       disco=DiscoDuro("Logario","SSD",30)
       memoria=Memoria("Ludwig",16,20)
       disco.añadir_precio(50)
       disco.añadir_precio(70)
       disco.añadir_precio(90)
       disco.añadir_precio(80)
       memoria.añadir_precio(100)
       memoria.añadir_precio(130)
       memoria.añadir_precio(150)
       memoria.añadir_precio(120)
       inventario=[disco,memoria]

       for i in inventario:
           print(i)
           print(f"Precio actual: {i.precio_actual}")
           print(f"Precio final: {i.calcular_precio_final()}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
