from datetime import date
from clases.Autor import Autor
from clases.AutorTesis import AutorTesis


class Tesis:
    def __init__(self):
        self.__id = 0
        self.__autores = list()
        self.__institucion = 0
        self.__fechaInv = 0
        self.__fechaPre = 0
        self.__campo = 0
        self.__paginas = 0
        self.__categoria = 0
        self.__estado = "Disponible"

    def getID(self): return self.__id
    def getAutor(self): return self.__autores
    def setCategoria(self, categoria): self.__categoria = categoria

    def __str__(self):
        autores = ", ".join(autor.Autor.getNombre()for autor in self.__autores)
        return f"Tesis: {self.__id}, {autores}, {self.__institucion}, {self.__fechaInv}, {self.__fechaPre}, {self.__campo}, {self.__paginas}, {self.__categoria}, {self.__estado}"

    def registrar(self, listaAutores, listaTesis):
        try:
            Id = int(input("Ingrese la id de la nueva tesis: "))
            contador = 1
            for tesis in listaTesis:
                if (Id == tesis.getID()):
                    print("El ID ya existe, intente nuevamente")
                    return 0
                contador += 1

            if (contador > len(listaTesis)):
                self.__id = Id

            siono2 = 'S'
            while (siono2.upper() == 'S'):
                autorID = int(
                    input("Ingrese el ID del autor de la nueva tesis: "))
                contador = 1

                for autor in listaAutores:
                    if (autorID == autor.getID()):
                        AutorTesis(autor, self)
                        break
                    contador += 1

                if (contador > len(listaAutores)):
                    siono = input(
                        "Autor no encontrado desea crear un nuevo autor? S/N: ")

                    if (siono.upper() == 'S'):
                        nuevoAutor = Autor()

                        if (nuevoAutor.registrar(listaAutores) == 1):
                            listaAutores.append(nuevoAutor)
                            AutorTesis(nuevoAutor, self)
                        else:
                            return 0

                siono2 = input("Desea añadir otro autor? S/N: ")

            if (len(self.getAutor()) == 0):
                print("Ningun autor registrado, creacion de tesis cancelada")
                return 0

            self.__institucion = input(
                "Ingrese la institucion de la nueva tesis: ")
            fechaInvTesis = int(
                input("Ingrese la fecha de investigacion de la nueva tesis(aaaa/mm/dd): "))
            self.__fechaInv = date(
                fechaInvTesis//10000, (fechaInvTesis//100) % 100, fechaInvTesis % 100)
            fechaPreTesis = int(
                input("Ingrese la fecha de presentacion de la nueva tesis(aaaa/mm/dd): "))
            self.__fechaPre = date(
                fechaPreTesis//10000, (fechaPreTesis//100) % 100, fechaPreTesis % 100)
            self.__campo = input(
                "Ingrese el campo de estudio de la nueva tesis: ")
            self.__paginas = int(
                input("Ingrese la cantidad de paginas de la nueva tesis: "))

        except ValueError:
            print(
                "Ultimo valor introducido incorrectamente, tesis no creada, intente nuevamente")
            return 0
        else:
            return 1

    def modificar(self, listaAutores, listaTesis):
        try:
            eleccion = int(input("Que apartado desea editar de la tesis?\n1. ID\n2. Nombre\n3. Institucion\n4. Fecha de investigacion\n5. Fecha de presentacion\n6. Campo de investigacion\n7. Numero de paginas\n8. Estado\n--> "))
        except ValueError:
            print("El numero ingresado no es valido")

        if (eleccion == 1):
            try:
                Id = int(input("Ingrese la id de la nueva tesis: "))
                contador = 1
                for tesis in listaTesis:
                    if (Id == tesis.getID()):
                        print("El ID ya existe, intente nuevamente")
                        break
                    contador += 1

                if (contador > len(listaTesis)):
                    self.__id = Id
            except ValueError:
                print("ID introducido incorrectamente intente nuevamente")
            else:
                print("ID modificado exitosamente")

        elif (eleccion == 2):
            temp = self.__autores.copy()
            siono2 = 'S'
            while (siono2.upper() == 'S'):
                autorID = int(
                    input("Ingrese el ID del autor de la nueva tesis: "))
                contador = 1

                for autor in listaAutores:
                    if (autorID == autor.getID()):
                        AutorTesis(autor, self)
                        break
                    contador += 1

                if (contador > len(listaAutores)):
                    siono = input(
                        "Autor no encontrado desea crear un nuevo autor? S/N: ")

                    if (siono.upper() == 'S'):
                        nuevoAutor = Autor()

                        if (nuevoAutor.registrar(listaAutores) == 1):
                            listaAutores.append(nuevoAutor)
                            AutorTesis(nuevoAutor, self)
                        else:
                            return 0

                siono2 = input("Desea añadir otro autor? S/N: ")

            if (len(self.getAutor()) == 0):
                print("Ningun autor registrado, modificación de tesis cancelada")
                self.__autores = temp
                return 0

        elif (eleccion == 3):
            self.__institucion = input("Ingresa la nueva institucion: ")
            print("Institucion modificada exitosamente")

        elif (eleccion == 4):
            try:
                fecha = int(input("Ingresa la nueva fecha de investigacion: "))
                self.__fechaInv = date(
                    fecha//10000, (fecha//100) % 100, fecha % 100)
            except ValueError:
                print("Fecha introducida incorrectamente intente nuevamente")
            else:
                print("Fecha de investigacion modificada exitosamente")

        elif (eleccion == 5):
            try:
                fecha = int(input("Ingresa la nueva fecha de presentacion: "))
                self.__fechaPre = date(
                    fecha//10000, (fecha//100) % 100, fecha % 100)
            except ValueError:
                print("Fecha introducida incorrectamente intente nuevamente")
            else:
                print("Fecha de presentacion modificada exitosamente")

        elif (eleccion == 6):
            self.__campo = input("Ingresa el nuevo campo de estudio: ")
            print("Campo de estudio modificado exitosamente")

        elif (eleccion == 7):
            try:
                self.__paginas = int(
                    input("Ingresa el nuevo numero de paginas: "))
            except ValueError:
                print("Numero de paginas introducido incorrectamente intente nuevamente")
            else:
                print("Numero de paginas modificado exitosamente")

        elif (eleccion == 8):
            self.__estado = input("Ingresa el nuevo estado: ")
            print("Estado modificado exitosamente")

        else:
            print("Opcion introducida no valida")

    def eliminar(self):
        print("Tesis eliminada exitosamente")
        del self

    def mostrarAutores(self):
        for autores in self.__autores:
            print("\t" + str(autores))
