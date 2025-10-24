class Categoria:

    def __init__(self):
        self.__id = 0
        self.__nombre = 0
        self.__descripcion = 0
        self.__cosas = list()
        self.__subCategoria = list()

    def __str__(self): return f"Categoria: ({self.__id}, {self.__nombre}, {self.__descripcion})"

    def getID(self): return self.__id


    def registrar(self, listaCategorias):
        try:
            Id = int(input("Ingrese el ID de la nueva categoria: "))
            contador = 1
            for categoria in listaCategorias:
                if(Id == categoria.getID()):
                    print("El ID ya existe, intente nuevamente")
                    return 0
                contador += 1

            if(contador > len(listaCategorias)):
                self.__id = Id


            self.__nombre = input("Ingrese el nombre de la nueva categoria: ")
            self.__descripcion = input("Ingrese la descripcion de la nueva categoria: ")

        except ValueError:
            print("Ultimo valor introducido incorrectamente, intente nuevamente")
            return 0
        else: return 1

    def modificar(self, listaCategorias):
        try:
            eleccion = int(input("Que apartado desea editar de la categoria?\n1. ID\n2. Nombre\n3. descripcion\n--> "))  
        except ValueError: print("El numero ingresado no es valido")


        if(eleccion == 1): 
            try: 
                Id = int(input("Ingresa la nueva ID: "))
                contador = 1
                for categoria in listaCategorias:
                    if(Id == categoria.getID()):
                        print("El ID ya existe, intente nuevamente")
                        break
                    contador += 1
                if(contador > len(listaCategorias)):
                    self.__id = Id
            except ValueError: print("ID introducido incorrectamente intente nuevamente")
            else: print("ID modificado exitosamente")

        elif(eleccion == 2): 
            self.__nombre = input("Ingresa el nuevo nombre: ")
            print("Nombre modificado exitosamente")

        elif(eleccion == 3): 
            self.__descripcion = input("Ingresa la nueva descripcion: ")
            print("Descripcion modificada exitosamente")

        else: print("Opcion introducida no valida")

    def eliminar(self): 
        print("Categoria eliminada exitosamente")
        del self

    def agnadirCosas(self, cosa):
        self.__cosas.append(cosa)

    def agnadirSubCategoria(self, subCategoria):
        self.__subCategoria.append(subCategoria)

    def mostrarCosas(self):
        print("\tCosas:")
        for cosa in self.__cosas:
            print("\t" + str(cosa))

    def mostrarSubCategorias(self):
        print("\tSubcategorias:")
        for subcategoria in self.__subCategoria:
            print("\t" + str(subcategoria))

