from clases.empleado import Empleado
class Gerente(Empleado):
    def __init__(self, nombre, apellido, sueldo, depto) -> None:
        super().__init__(nombre, apellido, sueldo)
        self.depto = depto

    def calc_salario_neto(self, impuestos, descuentos, bono):
        return super().calc_salario_neto(impuestos, descuentos) + bono    