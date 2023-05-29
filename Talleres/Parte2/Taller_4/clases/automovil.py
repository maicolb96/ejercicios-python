from clases.vehiculo import Vehiculo

class Automovil(Vehiculo):
    
    def __init__(self,marca,modelo,año,puertas):
        super().__init__(marca,modelo,año)
        self.puertas = puertas

    def obtener_info(self):
        dict = super().obtener_info() 
        dict["Puertas"] = self.puertas
        return dict   
