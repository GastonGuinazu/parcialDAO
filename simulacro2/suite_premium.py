from habitacion import Habitacion

class SuitePremium(Habitacion):
    tipo = 3  # Tipo 3 para suite premium
    def __init__(self, numero, huesped, costo_base, noches, jacuzzi):
        super().__init__(numero, huesped, costo_base, noches)
        self.jacuzzi = jacuzzi  # booleano

    def calcular_costo(self):
        if self.jacuzzi:
            return self.costo_base * self.noches * 1.2  # 20% más si tiene jacuzzi
        return self.costo_base * self.noches
    
    def calcular_costo_total(self):
        return self.calcular_costo()

    def __str__(self):
        return super().__str__() + f", Jacuzzi: {self.jacuzzi}"