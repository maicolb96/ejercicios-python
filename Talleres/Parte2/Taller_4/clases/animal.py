class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_ruido(self):
        animal = {"Nombre":self.nombre,"Edad":self.edad, "Ruido": "..."}
        return animal
