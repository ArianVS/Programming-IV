
class Lector:
    def __init__(self):
        self._id = 0
        self._nombre = 0
        self._telefono = 0
        self._direccion = 0
        self._estado = "Normal" 
        
    def getID(self): return self._id
    def getnombre(self): return self._nombre
    def getestado(self): return self._estado

    def __str__(self): return f"Lector: ({self._id}, {self._nombre}, {self._telefono}, {self._direccion}, {self._estado})"

    def crear(self):
        try:
            self._id = int(input("Ingrese el ID del lector: "))
            self._nombre = input("Ingrese el nombre del lector: ")
            self._telefono = input("Ingrese el telefono del lector: ")
            self._direccion = input("Ingrese la direccion del lector: ")
        except ValueError:
            print("Error en la entrada de datos, intente nuevamente")
            return 0
        else:
            return 1
        
    def modificar(self):
        try:
            eleccion = int(input("¿Qué apartado desea editar del lector?\n1. ID\n2. Nombre\n3. Teléfono\n4. Dirección\n5. Estado\n--> "))
        except ValueError:
            print("El número ingresado no es válido.")
            return 0

        if (eleccion == 1):
            try:
                self._id = int(input("Ingrese el nuevo ID del lector: "))
            except ValueError:
                print("ID introducido incorrectamente.")
            else:
                print("ID modificado exitosamente.")

        elif (eleccion == 2):
            self._nombre = input("Ingrese el nuevo nombre del lector: ")
            print("Nombre modificado exitosamente.")

        elif (eleccion == 3):
            self._telefono = input("Ingrese el nuevo teléfono del lector: ")
            print("Teléfono modificado exitosamente.")

        elif (eleccion == 4):
            self._direccion = input("Ingrese la nueva dirección del lector: ")
            print("Dirección modificada exitosamente.")

        elif (eleccion == 5):
            nuevo_estado = input("Ingrese el nuevo estado (normal, sancionado, suspendido, inactivo): ")
            if nuevo_estado in ["normal", "sancionado", "suspendido", "inactivo"]:
                self._estado = nuevo_estado
                print("Estado modificado exitosamente.")
            else:
                print("Estado no válido. Intente con: normal, sancionado, suspendido o inactivo.")

        else:
            print("Opción no válida.")


    def inhabilitar(self):
        if(self._estado == "inhabilitado"):
            op = input("El lector se encuentra inhabilitado, Desea habilitarlo? (S/N): ")
            if(op.upper() == 'S'):
                self._estado = "normal"
                print("Lector habilitado.")
            else: 
                print("El lector permanece inactivo.")
        else:
            self._estado = "inactivo"
            print("Lector inhabilitado.")