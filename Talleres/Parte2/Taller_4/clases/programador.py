from clases.empleado import Empleado
class Programador(Empleado):
    def __init__(self, nombre, apellido, sueldo, lenguaje) -> None:
        super().__init__(nombre, apellido, sueldo)
        self.lenguaje = lenguaje

    def calc_salario_neto(self, impuestos, descuentos):
        
        if str(self.lenguaje).upper() == "HTML": bono = 100000 
        if str(self.lenguaje).upper() == "JAVA": bono = 150000 
        if str(self.lenguaje).upper() == "PHP": bono = 200000 
        if str(self.lenguaje).upper() == "PYTHON": bono = 250000 

        return super().calc_salario_neto(impuestos, descuentos) + bono    