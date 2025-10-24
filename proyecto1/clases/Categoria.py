class Categoria:

    def __init__(self):
        self.__id = 0
        self.__nombre = 0
        self.__descripcion = 0
        self.__cosas = list()
        self.__subCategoria = list()

    def __str__(self): 
        #print("Escritos pertenecientes a la categoria: ")
        #for cosa in self.__cosas:
        #    print(cosa)

        return f"Categoria: ({self.__id}, {self.__nombre}, {self.__descripcion})"

    def getID(self): return self.__id


    def registrar(self):
        try:
            self.__id = int(input("Ingrese el ID de la nueva categoria: "))
            self.__nombre = input("Ingrese el nombre de la nueva categoria: ")
            self.__descripcion = input("Ingrese la descripcion de la nueva categoria: ")

        except ValueError:
            print("Ultimo valor introducido incorrectamente, intente nuevamente")
            return 0
        else: return 1

    def modificar(self):
        try:
            eleccion = int(input("Que apartado desea editar de la categoria?\n1. ID\n2. Nombre\n3. descripcion\n--> "))  
        except ValueError: print("El numero ingresado no es valido")


        if(eleccion == 1): 
            try: 
                self.__id = int(input("Ingresa la nueva ID: "))
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
        print("\tCosas:\n")
        for cosa in self.__cosas:
            print("\t"+cosa)

    def mostrarSubCategorias(self):
        print("\tSubcategorias:\n")
        for subcategoria in self.__subCategoria:
            print("\t"+subcategoria)

