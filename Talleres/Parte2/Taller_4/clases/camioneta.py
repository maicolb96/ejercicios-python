from clases.vehiculo import Vehiculo

class Camioneta(Vehiculo):

    def __init__(self,marca,modelo,año,carga):
        super().__init__(marca,modelo,año)
        self.carga = carga

    def obtener_info(self):
        info_camioneta = super().obtener_info()
        info_camioneta["Carga"] = self.carga
        return info_camioneta    