from datetime import date
from clases.Autor import Autor


class Articulo:
    def __init__(self):
        self.__doi = 0
        self.__nombreAutor = 0
        self.__editor = 0
        self.__fechaPub = 0
        self.__revista = 0
        self.__periodicidad = 0
        self.__nVolumen = 0
        self.__campo = 0
        self.__categoria = 0
        self.__estado = "Disponible"

    def getDOI(self): return self.__doi
    def getAutor(self): return self.__nombreAutor
    def setCategoria(self, categoria): self.__categoria = categoria

    def __str__(
        self): return f"Articulo: {self.__doi}, {self.__nombreAutor}, {self.__editor}, {self.__fechaPub}, {self.__revista}, {self.__periodicidad}, {self.__nVolumen}, {self.__campo}, {self.__categoria},{self.__estado}"

    def registrar(self, listaAutores):
        try:
            self.__doi = input("Ingrese el DOI del nuevo articulo: ")

            autorNombre = input(
                "Ingrese el nombre del autor del nuevo articulo: ")
            contador = 1

            for autor in listaAutores:
                if (autorNombre == autor.getNombre()):
                    self.__nombreAutor = autor
                    break
                contador += 1

            if (contador > len(listaAutores)):
                siono = input(
                    "Autor no encontrado desea crear un nuevo autor? S/N: ")

                if (siono.upper() == 'S'):
                    nuevoAutor = Autor()

                    if (nuevoAutor.registrar() == 1):
                        listaAutores.append(nuevoAutor)
                        self.__nombreAutor = nuevoAutor
                    else:
                        return 0

                    for i in listaAutores:
                        print(i)

                else:
                    print("Creacion de articulo cancelado")
                    return 0

            self.__editor = input(
                "Ingrese el nombre del editor del nuevo articulo: ")
            fechaPubArticulo = int(
                input("Ingrese la fecha de publicacion del nuevo articulo(aaaa/mm/dd): "))
            self.__fechaPub = date(
                fechaPubArticulo//10000, (fechaPubArticulo//100) % 100, fechaPubArticulo % 100)
            self.__revista = input("Ingrese la revista del nuevo articulo: ")
            self.__periodicidad = input(
                "Ingrese la periodicidad del nuevo articulo: ")
            self.__nVolumen = int(
                input("Ingrese el numero de volumen del articulo: "))
            self.__campo = input("Ingrese el campo de interes del articulo: ")

        except ValueError:
            print("Ultimo valor introducido incorrectamente, intente nuevamente")
            return 0
        else:
            return 1

    def modificar(self, listaAutores):
        try:
            eleccion = int(input(
                "Que apartado desea editar de la tesis?\n1. DOI\n2. Titulo\n3. Editor\n4. Fecha de publicacion\n5. revista\n6. Periodicidad\n7. Numero de volumen\n8. Campo de interes\n9. Estado\n--> "))
        except ValueError:
            print("El numero ingresado no es valido")

        if (eleccion == 1):
            self.__doi = input("Ingresa la nueva DOI: ")
            print("Institucion modificada exitosamente")

        elif (eleccion == 2):
            nuevoAutor = input("Ingresa el nombre del autor: ")

            contadorAu = 1

            for autor in listaAutores:
                if (nuevoAutor == autor.getNombre()):
                    self.__nombreAutor = autor
                    break
                contadorAu += 1

            if (contadorAu > len(listaAutores)):
                print("Autor no encontrado")
            else:
                print("Autor modificado exitosamente")

        elif (eleccion == 3):
            self.__editor = input("Ingresa el nuevo editor: ")
            print("Editor modificado exitosamente")

        elif (eleccion == 4):
            try:
                fecha = int(input("Ingresa la nueva fecha de publicacion: "))
                self.__fechaPub = date(
                    fecha//10000, (fecha//100) % 100, fecha % 100)
            except ValueError:
                print("Fecha introducida incorrectamente intente nuevamente")
            else:
                print("Fecha de publicacion modificada exitosamente")

        elif (eleccion == 5):
            self.__revista = input("Ingresa la nueva revista: ")
            print("Revista modificada exitosamente")

        elif (eleccion == 6):
            self.__periodicidad = input("Ingresa la nueva periodicidad: ")
            print("Periodicidad modificada exitosamente")

        elif (eleccion == 7):
            try:
                self.__nVolumen = int(
                    input("Ingresa el nuevo numero de volumen: "))
            except ValueError:
                print("Numero de volumen introducido incorrectamente intente nuevamente")
            else:
                print("Numero de volumen modificado exitosamente")

        elif (eleccion == 8):
            self.__estado = input("Ingresa el nuevo estado: ")
            print("Estado modificado exitosamente")

        else:
            print("Opcion introducida no valida")

    def eliminar(self):
        print("Articulo eliminado exitosamente")
        del self
