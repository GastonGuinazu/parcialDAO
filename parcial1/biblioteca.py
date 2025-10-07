from material import Material
from libro import Libro
from ebook import Ebook
from revista import Revista

class Biblioteca:
    def __init__(self, archivo_csv):
        self.materiales = self.lector_archivo(archivo_csv)

    def lector_archivo(self, archivo):
        materiales = []
        try:
            with open(archivo, 'r', encoding='utf-8') as file:
                for linea in file:
                    linea = linea.strip()
                    if not linea:
                        continue
                    datos = linea.split(',')

                    # tolerar encabezado
                    if datos[0] not in ("1", "2", "3"):
                        continue

                    tipo = datos[0]
                    codigo = datos[1]
                    titulo = datos[2]
                    autor = datos[3]
                    precio_base = float(datos[4]) if '.' in datos[4] else int(datos[4])
                    extra = datos[5]

                    if tipo == "1":
                        dias_prestados = int(extra)
                        material = Libro(codigo, titulo, autor, precio_base, dias_prestados)
                    elif tipo == "2":
                        valor_venta = float(extra) if '.' in extra else int(extra)
                        material = Ebook(codigo, titulo, autor, precio_base, valor_venta)
                    elif tipo == "3":
                        origen = extra.strip().lower()
                        material = Revista(codigo, titulo, autor, precio_base, origen)
                    else:
                        continue

                    materiales.append(material)
        except Exception as e:
            raise FileNotFoundError(f"Error al leer el archivo: {e}")

        return materiales

    # el test usa len(biblioteca.cantidad_materiales())
    def cantidad_materiales(self):
        return self.materiales

    def calcular_promedio_precios_base(self):
        if not self.materiales:
            return 0
        suma = sum(material.precio_base for material in self.materiales)
        promedio = suma / len(self.materiales)
        return int(promedio)  # promedio entero

    def obtener_material_mayor_costo_mantenimiento(self):
        return max(self.materiales, key=lambda material: material.calcular_costo_mantenimiento())

    def calcular_suma_costo_mantenimiento(self):
        return sum(material.calcular_costo_mantenimiento() for material in self.materiales)

    def contar_libros_mas_30_dias(self):
        return sum(
            1 for material in self.materiales
            if isinstance(material, Libro) and material.dias_prestados > 30
        )

    def contar_revistas_importadas(self):
        return sum(
            1 for material in self.materiales
            if isinstance(material, Revista) and str(material.origen).strip().lower() == "importada"
        )

    def cantidad_por_tipo(self):
        conteo = {"Libro": 0, "Ebook": 0, "Revista": 0}
        for material in self.materiales:
            if isinstance(material, Libro):
                conteo["Libro"] += 1
            elif isinstance(material, Ebook):
                conteo["Ebook"] += 1
            elif isinstance(material, Revista):
                conteo["Revista"] += 1
        return conteo
