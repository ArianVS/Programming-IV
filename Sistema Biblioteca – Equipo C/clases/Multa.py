from datetime import date, timedelta
from clases.Lector import Lector

class Multa:
    def __init__(self):
        self._id_multa = 0
        self._id_prestamo = 0
        self._idlector = "Desconocido"  
        self._lector = "Desconocido"  
        self._fecha_entrega_real = 0
        self._dias_retraso = 0
        self._dias_multa = 0
        self._fecha_inicio = 0
        self._fecha_fin = 0
        self._activa = True

    def get_id_prestamo(self): return self._id_prestamo
    def get_id_multa(self): return self._id_multa
    def get_idlector(self): return self._idlector

    def __str__(self):
        estado = "activa" if self._activa else "inactiva"
        return (f"Multa ID: {self._id_multa}, Préstamo ID: {self._id_prestamo}, Lector: {self._lector}, Estado: {estado}, Días multa: {self._dias_multa}, Días retraso: {self._dias_retraso}, Inicio: {self._fecha_inicio}, Fin: {self._fecha_fin}")

    def generar_multa(self, id_multa, id_prestamo, lector_id, fecha_estimada, fecha_real, listaLector):
        self._id_multa = id_multa
        self._id_prestamo = id_prestamo
        self._idlector = lector_id

        for who in listaLector:
            if lector_id == who.getID():
                self._lector = who.getnombre()
                who.setestado("Suspendido")
                break

        self._fecha_entrega_real = fecha_real
        self._dias_retraso = self.calcular_dias_retraso(fecha_estimada, fecha_real)
        self._dias_multa = self.calcular_multa(self._dias_retraso)
        self._fecha_inicio = date.today()
        self._fecha_fin = self._fecha_inicio + timedelta(days=self._dias_multa)
        self._activa = True
        print("Multa generada con éxito.")

        return True

    def calcular_dias_retraso(self, fecha_estimada, fecha_real):
        dias = (fecha_real - fecha_estimada).days
        return max(0, dias)

    def calcular_multa(self, dias_retraso):
        return dias_retraso * 3

    def levantar_multa(self):
        if (date.today() >= self._fecha_fin and self._activa):
            self._activa = False
            print("Multa levantada automáticamente.")
        elif self._activa:
            print("La multa aún está vigente.")

    def levantar_multas_auto(self, fecha_actual: date, lector_id, listaLector):
        if (fecha_actual >= self._fecha_fin and self._activa):
            self._activa = False
            print(f"Multa ID {self._id_multa} levantada automáticamente en fecha: {fecha_actual}")
            for who in listaLector:
                if lector_id == who.getID():
                    who.setestado("Normal")
                    break
        elif self._activa:
            print(f"Multa ID {self._id_multa} aún activa hasta {self._fecha_fin}")

    def consultar_multas(self, lector: str):
        if lector == self._lector:
            print(self)

    

    
