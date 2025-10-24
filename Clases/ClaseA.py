class Empresa:
    def __init__(self, nit, nombre, dir):
        self.nit = nit
        self.nombre = nombre
        self.dir = dir

    def contrata_a(self, ced):
        self.ced = ced
