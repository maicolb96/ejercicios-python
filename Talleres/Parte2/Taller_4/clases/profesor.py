from clases.persona import Persona

class Profesor(Persona):
    def __init__(self,nombre, apellido, edad, materia):
        super().__init__(nombre, apellido,edad)
        self.materia = materia

    def obtener_nombre_completo(self):
        return f"{super().obtener_nombre_completo()}\nMateria: {self.materia}"  