from habitacion import Habitacion

class Estandar(Habitacion):
    tipo = 1  # Tipo 1 para estándar
    def __init__(self, numero, huesped, costo_base, noches, extra):
        super().__init__(numero, huesped, costo_base, noches)
        
        self.extra = extra  # siempre false

    def calcular_costo(self):
        return self.costo_base * self.noches