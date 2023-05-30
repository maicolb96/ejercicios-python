from typing import Any
from clases.animal import Animal

class Gato(Animal):
    def __init__(self, nombre, edad, pelaje):
        super().__init__(nombre,edad)
        self.pelaje = pelaje

    def info_animal(self):
        gato = super().info_animal()    
        gato["Pelaje"] = self.pelaje
        gato["Ruido"] = self.hacer_ruido()
        return gato
    
    def hacer_ruido(self):
        return "Miau Miau..."
        