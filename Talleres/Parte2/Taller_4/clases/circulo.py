import math
from clases.forma import Forma

class Circulo(Forma):
    def __init__(self, radio) -> None:
        super().__init__(radio, radio)
        self.radio = radio

    def calc_area(self):
        return super().calc_area()*math.pi
    
    def calc_circunferencia(self):
        return 2.0*math.pi*float(self.radio)