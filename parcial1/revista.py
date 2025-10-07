from material import Material

class Revista(Material):
    tipo = 3

    def __init__(self, codigo, titulo, autor, precio_base, origen):
        super().__init__(codigo, titulo, autor, precio_base)
        self.origen = origen  # "nacional" o "importada"

    def calcular_costo_mantenimiento(self):
        # $50 por ejemplar, +20% si es importada
        costo = 50
        if str(self.origen).strip().lower() == "importada":
            costo = costo * 1.2
        return costo
