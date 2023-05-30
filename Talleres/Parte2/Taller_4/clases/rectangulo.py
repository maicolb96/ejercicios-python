from clases.forma import Forma

class Rectangulo(Forma):
    def __init__(self, ancho, alto) -> None:
        super().__init__(ancho, alto)

    def calc_area(self):
        return super().calc_area()

    def calc_perimetro(self):
        return (int(self.alto)*2) + (int(self.ancho)*2)   