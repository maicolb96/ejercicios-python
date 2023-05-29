class Vehiculo:
    def __init__(self,marca,modelo,año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def obtener_info(self):
        vehiculo = {
                    "Marca":self.marca,
                    "Modelo":self.modelo,
                    "Año":self.año
                    }   
        return vehiculo