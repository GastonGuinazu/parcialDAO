from material import Material

class Ebook(Material):
    tipo = 2

    def __init__(self, codigo, titulo, autor, precio_base, valor_venta):
        super().__init__(codigo, titulo, autor, precio_base)
        self.valor_venta = valor_venta

    def calcular_costo_mantenimiento(self):
        # 5% sobre el valor de venta
        return self.valor_venta * 0.05
