class Forma:
    def __init__(self, ancho, alto) -> None:
        self.ancho = ancho
        self.alto = alto

    def calc_area(self):
        return int(self.alto)*int(self.ancho)   
        