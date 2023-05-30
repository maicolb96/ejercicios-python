from clases.animal import Animal

class Perro(Animal):
    def __init__(self,nombre,edad,raza):
        super().__init__(nombre,edad)
        self.raza = raza

    def info_animal(self):
        perro = super().info_animal() 
        perro["Ruido"] = self.hacer_ruido()
        perro["Raza"] = self.raza   
        return perro
    
    def hacer_ruido(self):
        return "Guau Guau..."