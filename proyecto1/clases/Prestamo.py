from datetime import date, timedelta
from clases.Lector import Lector
from clases.Articulo import Articulo
from clases.Tesis import Tesis
from clases.Copia import Copia
from clases.Multa import Multa


class Prestamo:
    def __init__(self):
        self.id_prestamo = 0
        self.tipo_producto = 0
        self.dias_prestamo = 0
        self.fecha_prestamo = 0
        self.fecha_entrega_estimada = 0
        self.activo = True
        self.id_producto = 0
        self.id_lector = 0

    def set_id_prestamo(self, id_prestamo):
        self.id_prestamo = id_prestamo

    def get_id_prestamo(self):
        return self.id_prestamo

    def set_tipo_producto(self, tipo_producto):
        self.tipo_producto = tipo_producto

    def get_tipo_producto(self):
        return self.tipo_producto

    def set_dias_prestamo(self, dias_prestamo):
        self.dias_prestamo = dias_prestamo

    def get_dias_prestamo(self):
        return self.dias_prestamo

    def set_fecha_prestamo(self, fecha_prestamo):
        self.fecha_prestamo = fecha_prestamo

    def get_fecha_prestamo(self):
        return self.fecha_prestamo

    def set_fecha_entrega_estimada(self, fecha_entrega_estimada):
        self.fecha_entrega_estimada = fecha_entrega_estimada

    def get_fecha_entrega_estimada(self):
        return self.fecha_entrega_estimada

    def set_activo(self, activo):
        self.activo = activo

    def get_activo(self):
        return self.activo

    def set_id_producto(self, id_producto):
        self.id_producto = id_producto

    def get_id_producto(self):
        return self.id_producto

    def set_id_cliente(self, id_lector):
        self.id_lector = id_lector

    def get_id_cliente(self):
        return self.id_lector

    def __str__(self):
        return f"Prestamo(id_prestamo={self.id_prestamo}, tipo_producto={self.tipo_producto}, dias_prestamo={self.dias_prestamo}, fecha_prestamo={self.fecha_prestamo}, fecha_entrega_estimada={self.fecha_entrega_estimada}, activo={self.activo}, id_lector={self.id_lector})"

    def calcular_fecha_entrega(self):
        if self.fecha_prestamo and self.dias_prestamo:
            fecha_entrega = self.fecha_prestamo + \
                timedelta(days=self.dias_prestamo)
            self.fecha_entrega_estimada = fecha_entrega
            print(f"Fecha de entrega estimada: {self.fecha_entrega_estimada}")
        else:
            raise ValueError(
                "La fecha de préstamo o los días de préstamo no están establecidos.")

    def registrar_prestamo(self, listacopias, listarticulos, listatesis, listalectores):
        try:
            self.id_prestamo = int(input("Ingrese el ID del prestamo: "))
            lectorID = input(
                "Ingrese el ID del lector: ")
            contador = 1

            for lector in listalectores:
                if (lectorID == lector.getID()):
                    self.id_lector = lectorID
                    break
                contador += 1

            if (contador > len(listalectores)):
                siono = input(
                    "Lector no encontrado desea crear un nuevo lector? S/N: ")

                if (siono.upper() == 'S'):
                    nuevoLector = Lector()

                    if (nuevoLector.crear() == 1):
                        listalectores.append(nuevoLector)
                        self.id_lector = nuevoLector.getID()
                    else:
                        return 0

                    for i in listalectores:
                        print(i)

                else:
                    print("Creación de prestamo cancelada")
                    return 0
            self.tipo_producto = (
                input("Ingrese el tipo de producto (Libro, Articulo Cientifico,Tesis ): "))
            if self.tipo_producto == "Libro":
                idlibro = int(input("Ingrese el ID del libro: "))
                self.id_producto = int(
                    input("Ingrese el ID de la copia del libro: "))
                prestado = Copia()
                for copia in listacopias:
                    if copia.get_id_copia() == self.id_producto and copia.get_id_libro() == idlibro:
                        copia.set_estado("Prestado")
            elif self.tipo_producto == "Articulo Cientifico":
                self.id_producto = int(
                    input("Ingrese el ID del articulo: "))
                prestado = Articulo()
                for articulo in listarticulos:
                    if articulo.get_id_articulo() == self.id_producto:
                        articulo.set_estado("Prestado")
            elif self.tipo_producto == "Tesis":
                self.id_producto = int(input("Ingrese el ID de la tesis: "))
                prestado = Tesis()
                for tesis in listatesis:
                    if tesis.get_id_tesis() == self.id_producto:
                        tesis.set_estado("Prestado")
            else:
                raise ValueError("Tipo de producto no válido.")
            fechaprestamo = int(
                input("Ingrese la fecha de prestamo (YYYYMMDD): "))
            self.fecha_prestamo = date(
                fechaprestamo//10000, (fechaprestamo//100) % 100, fechaprestamo % 100)
            diasprestamo = int(input("Ingrese los dias de prestamo: "))
            if diasprestamo > 30:
                raise ValueError(
                    "Los días de préstamo no pueden ser mayores a 30 días.")
            else:
                self.dias_prestamo = diasprestamo
            self.calcular_fecha_entrega()
        except ValueError:
            print("Ultimo valor introducido incorrectamente, intente nuevamente")
            return 0
        else:
            return 1

    def finalizar_prestamo(self):
        try:
            self.id_prestamo = int(
                input("Ingrese el ID del prestamo a finalizar: "))
            self.activo = False

            print(f"Préstamo con ID {self.id_prestamo} finalizado.")

        except ValueError:
            print("Ultimo valor introducido incorrectamente, intente nuevamente")
            return 0
        else:
            return 1
