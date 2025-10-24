class Copia:
    def __init__(self):
        self.__id = 0
        self.__estado = "En biblioteca"
        self.__isbn = 0 

    def __str__(self): return f"Copia: ({self.__id}, {self.__isbn}, {self.__estado})"

    def getISBN(self): return self.__isbn
    def getID(self): return self.__id
    def set_estado(self, estado): self.__estado = estado
    def getEstado(self): return self.__estado

    def registrar_manual(self, isbn):
        self.__id = int(input("Ingrese el ID de esta copia: "))
        self.__isbn = isbn
        self.__estado = "en biblioteca"
    
    def registrar(self, listaCopias):
        try:
            Id = int(input("Ingrese el ID de la copia del libro: "))
            contador = 1
            for copia in listaCopias:
                if(Id == copia.getID()):
                    print("El ID ya existe, intente nuevamente")
                    return 0
                contador += 1
            
            if(contador > len(listaCopias)):
                self.__id = Id

            self.__estado = "en biblioteca"
            if not self.__isbn:
                self.__isbn = input("Ingrese el ISBN del libro asociado: ")
        except ValueError:
            print("Error en la entrada de datos, intente nuevamente")
            return 0
        else:
            print("Copia registrada exitosamente.")
            return 1
    
    def actualizar_estado(self):
        nuevo_estado = input("Ingresa el nuevo estado (en biblioteca, prestada, con retraso, en reparación): ").lower()
        if nuevo_estado in ["en biblioteca", "prestada", "con retraso", "en reparación"]:
            self.__estado = nuevo_estado
            print("Estado modificado exitosamente.")
        else:
            print("Estado no válido.")

    def eliminar(self): 
            print("Copia eliminada exitosamente")
            del self

     

    

         