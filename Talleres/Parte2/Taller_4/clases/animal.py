class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def info_animal(self):
        animal = {"Nombre":self.nombre,"Edad":self.edad, "Ruido": self.hacer_ruido()}
        return animal
    
    def hacer_ruido(self):
        return "..."
