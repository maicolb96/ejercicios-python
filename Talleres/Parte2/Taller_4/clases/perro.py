from animal import Animal

class Perro(Animal):
    def __init__(self,nombre,edad,raza):
        super().__init__(nombre,edad)
        self.raza = raza

    def hacer_ruido(self):
        perro = super().hacer_ruido() 
        perro["Ruido"] = "Guau Guau..."
        perro["Raza"] = self.raza   
        return perro