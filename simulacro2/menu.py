from hotel import Hotel, SuitePremium, Estandar, Suite, Habitacion

"""
1. Cargar reservas desde el archivo.
2. Calcular y mostrar la suma de costo de todas las reservas.
3. Obtener la reserva más cara.
4. Calcular el ingreso total del hotel.
5. Contar cuántas suites tienen vista al mar.
6. Contar cuántas suites premium tienen jacuzzi.
7. Calcular en un diccionario la cantidad de reservas de cada tipo de habitación.

"""


def main():
    hotel = Hotel("habitaciones.csv")
    
    print(f"2. Suma de costo de todas las reservas: {hotel.obtener_suma_reservas()}")
    print(f"3. Reserva más cara: {hotel.obtener_reserva_mas_cara()}")
    print(f"4. Ingreso total del hotel: {hotel.obtener_suma_reservas()}")
    print(f"5. Cantidad de suites con vista al mar: {hotel.contar_suites_vista_mar()}")
    print(f"6. Cantidad de suites premium con jacuzzi: {hotel.contar_suites_premium_jacuzzi()}")
    print(f"7. Cantidad de reservas por tipo: {hotel.cantidad_por_tipo()}")


if __name__ == "__main__":
    main()