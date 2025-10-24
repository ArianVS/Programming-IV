from datetime import date

class Autor:
    def __init__(self):
        self.__id = 0
        self.__nombre = 0
        self.__nacionalidad = 0
        self.__nacimiento = 0
        self.__cosas = list()


    def __str__(self): return f"Autor: ({self.__id}, {self.__nombre}, {self.__nacionalidad}, {self.__nacimiento})"

    def getNombre(self): return self.__nombre


    def registrar(self):
        try:
            self.__id = int(input("Ingrese el ID del nuevo autor: "))
            self.__nombre = input("Ingrese el nombre del nuevo autor: ")
            self.__nacionalidad = input("Ingrese la nacionalidad del nuevo autor: ")
            nacimiento = int(input("Ingrese la fecha de nacimiento del nuevo autor(aaaa/mm/dd): "))
            self.__nacimiento = date(nacimiento//10000, (nacimiento//100)%100, nacimiento%100)

        except ValueError: 
            print("Ultimo valor introducido incorrectamente, intente nuevamente")
            return 0
        else: return 1

    def modificar(self):
        try:
            eleccion = int(input("Que apartado desea editar del autor?\n1. ID\n2. Nombre\n3. nacionalidad\n4. Fecha de nacimiento\n--> "))  
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
            self.__nacionalidad = input("Ingresa la nueva nacionalidad: ")
            print("Nacionalidad modificada exitosamente")

        elif(eleccion == 4):
            try: 
                fecha = int(input("Ingresa la nueva fecha de nacimiento: "))
                self.__nacimiento = date(fecha//10000, (fecha//100)%100, fecha%100)
            except ValueError: print("Fecha introducida incorrectamente intente nuevamente")
            else: print("Fecha de nacimiento modificada exitosamente")
        
        else: print("Opcion introducida no valida")

    def agnadirCosas(self, cosa):
        self.__cosas.append(cosa)

    def mostrarCosas(self):
        for cosa in self.__cosas:
            print(cosa)

