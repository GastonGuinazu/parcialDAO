from abc import ABC, abstractmethod


class Habitacion(ABC):
    tipo = None  # Debe ser definido en las subclases
    def __init__(self,numero, huesped, costo_base, noches):
        self.numero = numero
        self.huesped = huesped
        self.costo_base = costo_base
        self.noches = noches

    @abstractmethod
    def calcular_costo(self):
        pass

    def __str__(self):
        return f"Tipo: {self.tipo}, Numero: {self.numero}, Huesped: {self.huesped}, Costo Base: {self.costo_base}, Noches: {self.noches}"