class Empleado:
    def __init__(self, nombre, apellido, sueldo) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
    
    def calc_salario_neto(self, impuestos, descuentos):
        return float(self.sueldo) - (float(self.sueldo)*impuestos) - descuentos
    

