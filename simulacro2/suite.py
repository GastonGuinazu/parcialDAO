from habitacion import Habitacion

class Suite(Habitacion):
    tipo = 2  # Tipo 2 para suite
    def __init__(self, numero, huesped, costo_base, noches, vista_mar):
        super().__init__(numero, huesped, costo_base, noches)
        self.vista_mar = vista_mar  # booleano

    def calcular_costo(self):
        if self.vista_mar:
            return self.costo_base * self.noches * 1.1  # 10% más si tiene vista al mar
        return self.costo_base * self.noches
    
    def __str__(self):
        return super().__str__() + f", Vista al Mar: {self.vista_mar}"