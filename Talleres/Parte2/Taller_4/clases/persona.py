class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
