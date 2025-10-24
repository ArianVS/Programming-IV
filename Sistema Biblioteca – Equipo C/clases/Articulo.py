from datetime import date
from clases.Autor import Autor
from clases.AutorArticulo import AutorArticulo


class Articulo:
    def __init__(self):
        self.__doi = 0
        self.__autores = list()
        self.__editor = 0
        self.__fechaPub = 0
        self.__revista = 0
        self.__periodicidad = 0
        self.__nVolumen = 0
        self.__campo = 0
        self.__categoria = 0
        self.__estado = "Disponible"

    def getDOI(self): return self.__doi
    def setDOI(self, doi): self.__doi = doi
    def getAutor(self): return self.__autores
    def setAutor(self, autores): self.__autores = autores
    def getEditor(self): return self.__editor
    def setEditor(self, editor): self.__editor = editor
    def getFechaPub(self): return self.__fechaPub
    def setFechaPub(self, fechaPub): self.__fechaPub = fechaPub
    def getRevista(self): return self.__revista
    def setRevista(self, revista): self.__revista = revista
    def getPeriodicidad(self): return self.__periodicidad
    def setPeriodicidad(self, periodicidad): self.__periodicidad = periodicidad
    def getNVolumen(self): return self.__nVolumen
    def setCategoria(self, categoria): self.__categoria = categoria

    def __str__(self): 
        autores = ", ".join(autor.Autor.getNombre() for autor in self.__autores)
        return f"Articulo: {self.__doi}, {self.__editor}, {autores}, {self.__fechaPub}, {self.__revista}, {self.__periodicidad}, {self.__nVolumen}, {self.__campo}, {self.__categoria},{self.__estado}"

    def registrar(self, listaAutores, listaArticulos):
        try:
            Doi = input("Ingrese el DOI del nuevo articulo: ")

            contador = 1
            for articulo in listaArticulos:
                if(Doi == articulo.getDOI()):
                    print("El DOI ya existe, intente nuevamente")
                    return 0
                contador += 1

            if(contador > len(listaArticulos)):
                self.__doi = Doi

            siono2 = 'S'
            while (siono2.upper() == 'S'):
                autorID = int(input("Ingrese el ID del autor de la nueva tesis: "))
                contador = 1

                for autor in listaAutores:
                    if (autorID == autor.getID()):
                        AutorArticulo(autor, self)
                        break
                    contador += 1

                if (contador > len(listaAutores)):
                    siono = input(
                        "Autor no encontrado desea crear un nuevo autor? S/N: ")

                    if (siono.upper() == 'S'):
                        nuevoAutor = Autor()

                        if (nuevoAutor.registrar(listaAutores) == 1):
                            listaAutores.append(nuevoAutor)
                            AutorArticulo(nuevoAutor, self)
                        else:
                            return 0

                siono2 = input("Desea añadir otro autor? S/N: ")

            if (len(self.getAutor()) == 0):
                print("Ningun autor registrado, creacion de tesis cancelada")
                return 0

            self.__editor = input("Ingrese el nombre del editor del nuevo articulo: ")
            fechaPubArticulo = int(input("Ingrese la fecha de publicacion del nuevo articulo(aaaa/mm/dd): "))
            self.__fechaPub = date(fechaPubArticulo//10000, (fechaPubArticulo//100) % 100, fechaPubArticulo % 100)
            self.__revista = input("Ingrese la revista del nuevo articulo: ")
            self.__periodicidad = input("Ingrese la periodicidad del nuevo articulo: ")
            self.__nVolumen = int(input("Ingrese el numero de volumen del articulo: "))
            self.__campo = input("Ingrese el campo de interes del articulo: ")

        except ValueError:
            print("Ultimo valor introducido incorrectamente, articulo no creado, intente nuevamente")
            return 0
        else:
            return 1

    def modificar(self, listaAutores, listaArticulos):
        try:
            eleccion = int(input("Que apartado desea editar del articulo?\n1. DOI\n2. Titulo\n3. Editor\n4. Fecha de publicacion\n5. revista\n6. Periodicidad\n7. Numero de volumen\n8. Campo de interes\n9. Estado\n--> "))
        except ValueError:
            print("El numero ingresado no es valido")

        if (eleccion == 1):
            self.__doi = input("Ingresa la nueva DOI: ")
            contador = 1
            for articulo in listaArticulos:
                if (self.__doi == articulo.getDOI()):
                    print("El DOI ya existe, intente nuevamente")
                    return 0
                contador += 1
            if (contador > len(listaArticulos)):
                self.__doi = self.__doi
                print("DOI modificado exitosamente")

        elif (eleccion == 2):
            temp = self.__autores.copy()
            siono2 = 'S'
            while (siono2.upper() == 'S'):
                autorID = int(input("Ingrese el ID del autor de la nueva tesis: "))
                contador = 1

                for autor in listaAutores:
                    if (autorID == autor.getID()):
                        AutorArticulo(autor, self)
                        break
                    contador += 1

                if (contador > len(listaAutores)):
                    siono = input(
                        "Autor no encontrado desea crear un nuevo autor? S/N: ")

                    if (siono.upper() == 'S'):
                        nuevoAutor = Autor()

                        if (nuevoAutor.registrar(listaAutores) == 1):
                            listaAutores.append(nuevoAutor)
                            AutorArticulo(nuevoAutor, self)
                        else:
                            return 0

                siono2 = input("Desea añadir otro autor? S/N: ")

            if (len(self.getAutor()) == 0):
                print("Ningun autor registrado, modificación de tesis cancelada")
                self.__autores = temp
                return 0
            
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

    def mostrarAutores(self):
        for autores in self.__autores:
            print("\t" + str(autores))

