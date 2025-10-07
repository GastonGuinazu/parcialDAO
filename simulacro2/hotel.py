from habitacion import Habitacion
from estandar import Estandar
from suite import Suite
from suite_premium import SuitePremium


class Hotel():


    def __init__(self, archivo):
        self.archivo = archivo
        self.habitaciones = self.lector_archivo(archivo)


    def lector_archivo(self, archivo):
        habitaciones = []
        try:
            with open(archivo, 'r') as file:
                
                for linea in file:
                    datos = linea.strip().split(',')
                    tipo = datos[0]
                    numero = int(datos[1])
                    huesped = datos[2]
                    costo_noche = int(datos[3])
                    noches = int(datos[4])
                    extra = datos[5] == "True"  # Para estándar


                    if tipo == "1": 
                        habitacion = Estandar(numero, huesped, costo_noche, noches, extra)
                    elif tipo == "2":
                        habitacion = Suite(numero, huesped, costo_noche, noches, extra)
                    elif tipo == "3":
                        habitacion = SuitePremium(numero, huesped, costo_noche, noches, extra)

                    habitaciones.append(habitacion)

        except Exception as e:
            raise FileNotFoundError(f"Error al leer el archivo: {e}")

        
        return habitaciones

    def cantidad_habitaciones(self):
        return len(self.habitaciones)
    
    def cantidad_por_tipo(self):
        contador = {1: 0, 2: 0, 3: 0}
        for habitacion in self.habitaciones:
            contador[habitacion.tipo] += 1
        return { "Estandar": contador[1], "Suite": contador[2], "SuitePremium": contador[3] }
    
    def obtener_suma_reservas(self):
        return sum(habitacion.calcular_costo() for habitacion in self.habitaciones)
    
    def obtener_reserva_mas_cara(self):
        return max(self.habitaciones, key=lambda habitacion: habitacion.calcular_costo())
    
    def contar_suites_vista_mar(self):
        return sum(1 for habitacion in self.habitaciones if (habitacion.tipo == 2 and habitacion.vista_mar))

    def contar_suites_premium_jacuzzi(self):
        return sum(1 for habitacion in self.habitaciones if (habitacion.tipo == 3 and habitacion.jacuzzi))