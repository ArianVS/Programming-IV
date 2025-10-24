from clases.AutorLibro import AutorLibro
from clases.Autor import Autor
from clases.Copia import Copia


class Libro:
    def __init__(self):
        self.__isbn = 0
        self.__titulo = 0
        self.__edicion = 0
        self.__year = 0
        self.__editorial = 0
        self.__genero = 0
        self._idioma = 0
        self.__nCopias = 0
        self.__activo = True
        self.__categoria = 0
        self.__Autor = list()
        

    def getISBN(self): return self.__isbn
    def setISBN(self, isbn): self.__isbn = isbn
    def getEdicion(self): return self.__edicion
    def setEdicion(self, edicion): self.__edicion = edicion
    def getYear(self): return self.__year
    def setYear(self, pyear): self.__year = pyear
    def getEditorial(self): return self.__editorial
    def setEditorial(self, editorial): self.__editorial = editorial
    def getGenero(self): return self.__genero
    def setGenero(self, genero): self.__genero = genero
    def getIdioma(self): return self._idioma
    def setIdioma(self, idioma): self._idioma = idioma
    def getNCopias(self): return self.__nCopias
    def setNCopias(self, nCopias): self.__nCopias = nCopias
    def getActivo(self): return self.__activo
    def setActivo(self, activo): self.__activo = activo
    def getCategoria(self): return self.__categoria
    def setCategoria(self, categoria): self.__categoria = categoria
    def getAutor(self): return self.__Autor
    def setAutor(self, autor): self.__Autor
    def getTitulo(self): return self.__titulo
    def setTitulo(self, titulo): self.__titulo = titulo

    def __str__(self):
        autores = ", ".join(autor.Autor.getNombre() for autor in self.__Autor)
        return f"Libro: ({self.__isbn}, {self.__titulo}, {autores}, {self.__edicion}, {self.__year}, {self.__editorial}, {self.__genero}, {self._idioma}, {self.__nCopias})"

    def registrar(self, listaAutores, listaCopias, listaLibros):
        try:
            Isbn = int(input("Ingrese el ISBN del nuevo libro: "))
            contador = 1
            for libro in listaLibros:
                if (Isbn == libro.getISBN()):
                    print("El ISBN ya existe, intente nuevamente")
                    return 0
                contador += 1

            if (contador > len(listaLibros)):
                self.__isbn = Isbn
            autorID = input(
                "Ingrese el ID del autor del nuevo libro: ")
            contador = 1


            siono2 = 'S'
            while (siono2.upper() == 'S'):
                autorID = int(input("Ingrese el ID del autor del nuevo libro: "))
                contador = 1

                for autor in listaAutores:
                    if (autorID == autor.getID()):
                        AutorLibro(autor, self)
                        break
                    contador += 1

                if (contador > len(listaAutores)):
                    siono = input(
                        "Autor no encontrado desea crear un nuevo autor? S/N: ")

                    if (siono.upper() == 'S'):
                        nuevoAutor = Autor()

                        if (nuevoAutor.registrar(listaAutores) == 1):
                            listaAutores.append(nuevoAutor)
                            AutorLibro(nuevoAutor, self)
                        else:
                            return 0

                siono2 = input("Desea añadir otro autor? S/N: ")

            if (len(self.getAutor()) == 0):
                print("Ningun autor registrado, creacion de libro cancelada")
                return 0

            self.__titulo = input("Ingrese el titulo del nuevo libro: ")
            self.__edicion = int(input("Ingrese la edicion del nuevo libro: "))
            self.__year = int(
                input("Ingrese el año de publicación del nuevo libro: "))
            self.__editorial = input("Ingrese la editorial del nuevo libro: ")
            self.__genero = input("Ingrese el genero del nuevo libro: ")
            self._idioma = input("Ingrese el idioma del nuevo libro: ")
            self.__nCopias = int(
                input("Ingrese el numero de copias del nuevo libro: "))
            
            for i in range(self.__nCopias):
                print(f"\nRegistro de la copia {i+1}/{self.__nCopias}")
                copia = Copia()
                copia.registrar_manual(self.__isbn)
                listaCopias.append(copia)

            self.__activo = True
        except ValueError:
            print("Ultimo valor introducido incorrectamente, intente nuevamente")
            return 0
        else:
            return 1

    def modificar(self, listaAutores, listaLibros):
        try:
            eleccion = int(input(
                "Que apartado desea editar del libro?\n1. ISBN\n2. Titulo\n3. Edicion\n4. Año\n5. Editorial\n6. Genero\n7. Idioma\n8. Numero de copias\n9. Autor\n--> "))
        except ValueError:
            print("El numero ingresado no es valido")

        if (eleccion == 1):
            try:
                Isbn = int(input("Ingrese el ISBN del nuevo libro: "))
                contador = 1
                for libro in listaLibros:
                    if (Isbn == libro.getISBN()):
                        print("El ISBN ya existe, intente nuevamente")
                        break
                    contador += 1

                if (contador > len(listaLibros)):
                    self.__isbn = Isbn
            except ValueError:
                print("ISBN introducido incorrectamente intente nuevamente")
            else:
                print("ISBN modificado exitosamente")

        elif (eleccion == 2):
            self.__titulo = input("Ingresa el nuevo titulo: ")
            print("Titulo modificado exitosamente")

        elif (eleccion == 3):
            self.__edicion = int(input("Ingresa la nueva edicion: "))
            print("Edicion modificada exitosamente")

        elif (eleccion == 4):
            self.__year = int(input("Ingresa el nuevo año de publicación: "))
            print("Año modificado exitosamente")

        elif (eleccion == 5):
            self.__editorial = input("Ingresa la nueva editorial: ")
            print("Editorial modificada exitosamente")

        elif (eleccion == 6):
            self.__genero = input("Ingresa el nuevo genero: ")
            print("Genero modificado exitosamente")

        elif (eleccion == 7):
            self._idioma = input("Ingresa el nuevo idioma: ")
            print("Idioma modificado exitosamente")

        elif (eleccion == 8):
            self.__nCopias = int(input("Ingresa el nuevo numero de copias: "))
            print("Numero de copias modificado exitosamente")

        elif (eleccion == 9):
            temp = self.__Autor.copy()
            siono2 = 'S'
            while (siono2.upper() == 'S'):
                autorID = int(input("Ingrese el ID del autor de la nueva tesis: "))
                contador = 1

                for autor in listaAutores:
                    if (autorID == autor.getID()):
                        AutorLibro(autor, self)
                        break
                    contador += 1

                if (contador > len(listaAutores)):
                    siono = input(
                        "Autor no encontrado desea crear un nuevo autor? S/N: ")

                    if (siono.upper() == 'S'):
                        nuevoAutor = Autor()

                        if (nuevoAutor.registrar(listaAutores) == 1):
                            listaAutores.append(nuevoAutor)
                            AutorLibro(nuevoAutor, self)
                        else:
                            return 0

                siono2 = input("Desea añadir otro autor? S/N: ")

            if (len(self.getAutor()) == 0):
                print("Ningun autor registrado, modificación de tesis cancelada")
                self.__Autor = temp
                return 0

    def inhabilitar(self):
        self.__activo = False
        print("Articulo inhabilitado exitosamente")

    def eliminar(self):
        print("Libro eliminado exitosamente")
        del self
