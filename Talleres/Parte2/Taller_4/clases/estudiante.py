from clases.persona import Persona

class Estudiante(Persona):
    def __init__(self,nombre, apellido, edad, carrera):
        super().__init__(nombre, apellido,edad)
        self.carrera = carrera

    def obtener_nombre_completo(self):
        return f"{super().obtener_nombre_completo()}\nCarrera: {self.carrera}"  