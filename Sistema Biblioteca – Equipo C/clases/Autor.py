from datetime import date

class Autor:
    def __init__(self):
        self.__id = 0
        self.__nombre = 0
        self.__nacionalidad = 0
        self.__nacimiento = 0
        self.__libros = list()
        self.__articulos = list()
        self.__tesis = list()


    def __str__(self): 
        return f"Autor: ({self.__id}, {self.__nombre}, {self.__nacionalidad}, {self.__nacimiento})"

    def getNombre(self): return self.__nombre
    def getID(self): return self.__id
    def getNacionalidad(self): return self.__nacionalidad
    def getNacimiento(self): return self.__nacimiento
    def getLibros(self): return self.__libros
    def getArticulos(self): return self.__articulos
    def getTesis(self): return self.__tesis
    def setID(self, id): self.__id = id
    def setNombre(self, nombre): self.__nombre = nombre
    def setNacionalidad(self, nacionalidad): self.__nacionalidad = nacionalidad
    def setNacimiento(self, nacimiento): self.__nacimiento = nacimiento
    def setLibros(self, libros): self.__libros = libros
    def setArticulos(self, articulos): self.__articulos = articulos
    def setTesis(self, tesis): self.__tesis = tesis


    def registrar(self, listaAutores):
        try:
            Id = int(input("Ingrese el ID del nuevo autor: "))
            contador = 1
            for autor in listaAutores:
                if(Id == autor.getID()):
                    print("El ID ya existe, intente nuevamente")
                    return 0
                contador += 1

            if(contador > len(listaAutores)):
                self.__id = Id
            self.__nombre = input("Ingrese el nombre del nuevo autor: ")
            self.__nacionalidad = input("Ingrese la nacionalidad del nuevo autor: ")
            nacimiento = int(input("Ingrese la fecha de nacimiento del nuevo autor(aaaa/mm/dd): "))
            self.__nacimiento = date(nacimiento//10000, (nacimiento//100)%100, nacimiento%100)

        except ValueError: 
            print("Ultimo valor introducido incorrectamente, autor no creado, intente nuevamente")
            return 0
        else: return 1

    def modificar(self, listaAutores):
        try:
            eleccion = int(input("Que apartado desea editar del autor?\n1. ID\n2. Nombre\n3. nacionalidad\n4. Fecha de nacimiento\n--> "))  
        except ValueError: print("El numero ingresado no es valido")


        if(eleccion == 1): 
            try: 
                Id = int(input("Ingresa la nueva ID: "))
                contador = 1
                for autor in listaAutores:
                    if(Id == autor.getID()):
                        print("El ID ya existe, intente nuevamente")
                        break
                    contador += 1
                if(contador > len(listaAutores)):
                    self.__id = Id
            except ValueError: print("ID introducido incorrectamente intente nuevamente")
            else: print("ID modificado exitosamente")

        elif(eleccion == 2): 
            self.__nombre = input("Ingresa el nuevo nombre: ")
            print("Nombre modificado exitosamente")

        elif(eleccion == 3): 
            self.__nacionalidad = input("Ingresa la nueva nacionalidad: ")
            print("Nacionalidad modificada exitosamente")

        elif(eleccion == 4):
            try: 
                fecha = int(input("Ingresa la nueva fecha de nacimiento: "))
                self.__nacimiento = date(fecha//10000, (fecha//100)%100, fecha%100)
            except ValueError: print("Fecha introducida incorrectamente intente nuevamente")
            else: print("Fecha de nacimiento modificada exitosamente")
        
        else: print("Opcion introducida no valida")

    def mostrarLibros(self):
        print("\tLibros:")
        for libros in self.__libros:
            print("\t" + libros.libro.getTitulo())
            
