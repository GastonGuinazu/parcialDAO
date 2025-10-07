from material import Material
import math

class Libro(Material):
    tipo = 1

    def __init__(self, codigo, titulo, autor, precio_base, dias_prestados):
        super().__init__(codigo, titulo, autor, precio_base)
        self.dias_prestados = dias_prestados

    def calcular_costo_mantenimiento(self):
        # $100 por cada 30 días (se redondea hacia arriba)
        bloques = math.ceil(self.dias_prestados / 30.0)
        return 100 * bloques
