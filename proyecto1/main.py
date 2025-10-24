from datetime import date
from clases.Tesis import Tesis
from clases.Autor import Autor
from clases.Categoria import Categoria
from clases.Articulo import Articulo
from clases.Libro import Libro
from clases.Prestamo import Prestamo
from clases.Copia import Copia
from clases.Lector import Lector
from clases.Multa import Multa


listaTesis = list()
listaArticulo = list()  # base de datos
listaLibro = list()
listaCategorias = list()
listaAutores = list()
listaLector = list()
ListaPrestamos = list()
listaCopias = list()
listaMultas = list()


def tesis():
    eleccion = 0

    while (eleccion != 6):
        eleccion = 0

        try:
            eleccion = int(input(
                "\n\nQue desea hacer con la tesis?\n1. Registrar\n2. Consultar\n3. Modificar\n4. Eliminar\n5. Asignar una categoria\n6. Cancelar\n--> "))
        except ValueError:
            print("El numero ingresado no es valido")

        if (eleccion == 1):
            nuevaTesis = Tesis()

            if (nuevaTesis.registrar(listaAutores) == 1):
                nuevaTesis.getAutor().agnadirCosas(nuevaTesis)
                listaTesis.append(nuevaTesis)
            else:
                print()

            for i in listaTesis:
                print(i)

        elif (eleccion == 2):
            try:
                tesisCambiar = int(
                    input("Ingrese la ID de la tesis que desea consultar: "))

            except ValueError:
                print("ID introducida no valida")
            else:
                contador = 1

                for tesis in listaTesis:
                    if (tesisCambiar == tesis.getID()):
                        print(tesis)
                        break
                    contador += 1

                if (contador > len(listaTesis)):
                    print("La ID no fue encontarda")

        elif (eleccion == 3):
            try:
                tesisCambiar = int(
                    input("Ingrese la ID de la tesis que desea modificar: "))

            except ValueError:
                print("ID introducida no valida")
            else:
                contador = 1

                for tesis in listaTesis:
                    if (tesisCambiar == tesis.getID()):
                        tesis.modificar(listaAutores)
                        break
                    contador += 1

                if (contador > len(listaTesis)):
                    print("La ID no fue encontarda")

        elif (eleccion == 4):
            try:
                tesisCambiar = int(
                    input("Ingrese la ID de la tesis que desea eliminar: "))

            except ValueError:
                print("ID introducida no valida")
            else:
                contador = 1

                for tesis in listaTesis:
                    if (tesisCambiar == tesis.getID()):
                        del listaTesis[contador-1]
                        tesis.eliminar()
                        break
                    contador += 1

                if (contador > len(listaTesis)):
                    print("La ID no fue encontarda")

        elif (eleccion == 5):
            try:
                tesisAsignar = int(
                    input("Ingrese la ID de la tesis a la que desea asignar una categoria: "))
                categoriaAsignar = int(
                    input("Ingrese la ID de la categoria a asignar: "))

                contador1 = 1
                contador2 = 1

                for tesis in listaTesis:
                    if (tesisAsignar == tesis.getID()):

                        for categoria in listaCategorias:
                            if (categoriaAsignar == categoria.getID()):
                                categoria.agnadirCosas(tesis)
                                tesis.setCategoria(categoria)
                                break
                            contador2 += 1

                        break
                    contador1 += 1

                if (contador1 > len(listaTesis) | contador2 > len(listaCategorias)):
                    print("La ID no fue encontrada")
            except ValueError:
                print("ID introducida no valida")

        elif (eleccion == 6):
            print("Ejecucion cancelada")

        else:
            print("Opcion introducida no valida")


def articulo():
    eleccion = 0

    while (eleccion != 6):
        eleccion = 0

        try:
            eleccion = int(input(
                "\n\nQue desea hacer con el articulo cientifico?\n1. Registrar\n2. Consultar\n3. Modificar\n4. Eliminar\n5. Asignar una categoria\n6. Cancelar\n--> "))
        except ValueError:
            print("El numero ingresado no es valido")

        if (eleccion == 1):
            nuevoArticulo = Articulo()

            if (nuevoArticulo.registrar(listaAutores) == 1):
                nuevoArticulo.getAutor().agnadirCosas(nuevoArticulo)
                listaArticulo.append(nuevoArticulo)
            else:
                print()

            for i in listaArticulo:
                print(i)

        elif (eleccion == 2):
            articuloCambiar = input(
                "Ingrese el DOI del articulo que desea consultar: ")

            contador = 1

            for articulo in listaArticulo:
                if (articuloCambiar == articulo.getDOI()):
                    print(articulo)
                    break
                contador += 1

            if (contador > len(listaArticulo)):
                print("El DOI no fue encontrado")

        elif (eleccion == 3):
            articuloCambiar = input(
                "Ingrese el DOI del articulo que desea modificar: ")

            contador = 1

            for articulo in listaArticulo:
                if (articuloCambiar == articulo.getDOI()):
                    articulo.modificar(listaAutores)
                    break
                contador += 1

                if (contador > len(listaArticulo)):
                    print("El DOI no fue encontrado")

        elif (eleccion == 4):
            articuloCambiar = input(
                "Ingrese el DOI del articulo que desea eliminar: ")

            contador = 1

            for articulo in listaArticulo:
                if (articuloCambiar == articulo.getDOI()):
                    del listaArticulo[contador-1]
                    articulo.eliminar()
                    break
                contador += 1

                if (contador > len(listaArticulo)):
                    print("El DOI no fue encontrado")

        elif (eleccion == 5):
            try:
                articuloAsignar = input(
                    "Ingrese el DOI del articulo al que desea asignar una categoria: ")
                categoriaAsignar = int(
                    input("Ingrese la ID de la categoria a asignar: "))

            except ValueError:
                print("ID introducida no valida")

            contador1 = 1
            contador2 = 1

            for articulo in listaArticulo:
                if (articuloAsignar == articulo.getDOI()):

                    for categoria in listaCategorias:
                        if (categoriaAsignar == categoria.getID()):
                            categoria.agnadirCosas(articulo)
                            articulo.setCategoria(categoria)
                            break
                        contador2 += 1

                    break
                contador1 += 1

            if (contador1 > len(listaArticulo) | contador2 > len(listaCategorias)):
                print("La ID o el DOI no fue encontrada")

        elif (eleccion == 6):
            print("Ejecucion cancelada")

        else:
            print("Opcion introducida no valida")


def libro():
    eleccion = 0

    while (eleccion != 6):
        eleccion = 0

        try:
            eleccion = int(input(
                "Que desea hacer con los libros?\n1. Registrar\n2. Consultar\n3. Modificar\n4. Eliminar\n5. Asignar Categoria\n6. Cancelar\n--> "))
        except ValueError:
            print("El numero ingresado no es valido")

        if (eleccion == 1):
            nuevoLibro = Libro()

            if nuevoLibro.registrar(listaAutores, listaCopias) == 1:
                nuevoLibro.getAutor().agnadirCosas(nuevoLibro)
                listaLibro.append(nuevoLibro)
            else:
                print()

            for i in listaLibro:
                print(i)

        elif (eleccion == 2):
            libroConsulta = input(
                "Ingrese el ISBN del libro que desea consultar: ")

            contador = 1

            for libro in listaLibro:
                if (libroConsulta == libro.getISBN()):
                    print(libro)
                    break
                contador += 1

            if (contador > len(listaLibro)):
                print("El ISBN no fue encontrado")

        elif (eleccion == 3):
            libroCambiar = input(
                "Ingrese el ISBN del libro que desea modificar: ")

            contador = 1

            for libro in listaLibro:
                if (libroCambiar == libro.getISBN()):
                    libro.modificar()
                    break
                contador += 1

                if (contador > len(listaLibro)):
                    print("El ISBN no fue encontrado")

        elif (eleccion == 4):
            libroEliminar = input(
                "Ingrese el ISBN del libro que desea eliminar: ")

            contador = 1

            for libro in listaLibro:
                if (libroEliminar == libro.getISBN()):
                    del listaLibro[contador-1]
                    libro.eliminar()
                    break
                contador += 1

                if (contador > len(listaLibro)):
                    print("El ISBN no fue encontrado")

        elif (eleccion == 5):
            try:
                libroAsignar = input(
                    "Ingrese el ISBN del libro al que desea asignar una categoria: ")
                categoriaAsignar = int(
                    input("Ingrese la ID de la categoria a asignar: "))

            except ValueError:
                print("ID introducida no valida")

            contador1 = 1
            contador2 = 1

            for libro in listaLibro:
                if (libroAsignar == libro.getISBN()):

                    for categoria in listaCategorias:
                        if (categoriaAsignar == categoria.getID()):
                            categoria.agnadirCosas(libro)
                            libro.setCategoria(categoria)
                            break
                        contador2 += 1

                    break
                contador1 += 1

            if (contador1 > len(listaLibro) | contador2 > len(listaCategorias)):
                print("La ID o el ISBN no fue encontrada")
        elif (eleccion == 6):
            print("Ejecucion cancelada")

        else:
            print("Opcion introducida no valida")


def categoria():
    eleccion = 0

    while (eleccion != 5):
        eleccion = 0

        try:
            eleccion = int(input(
                "Que desea hacer con las categorias?\n1. Registrar\n2. Consultar\n3. Modificar\n4. Eliminar\n5. Cancelar\n--> "))
        except ValueError:
            print("El numero ingresado no es valido")

        if (eleccion == 1):
            try:
                nuevaCategoria = Categoria()

                if (nuevaCategoria.registrar() == 1):

                    siono = input("Es una subcategoria? S/N: ")

                    if (siono.upper() == 'S'):
                        padre = int(
                            input("Ingrese la ID de la categoria padre: "))

                        contador = 1
                        for categoria in listaCategorias:
                            if (padre == categoria.getID()):
                                categoria.agnadirSubCategoria(nuevaCategoria)
                            contador += 1

                            if (contador > len(listaCategorias)):
                                print(
                                    "Padre no encontrado, creada como categoria independiente")

                    else:
                        print()
            except ValueError:
                print("Ultimo valor introducido incorrectamente, intente nuevamente")
            else:
                listaCategorias.append(nuevaCategoria)

            for i in listaCategorias:
                print(i)

        elif (eleccion == 2):
            try:
                categoriaCambiar = int(
                    input("Ingrese la ID de la categoria que desea consultar: "))

            except ValueError:
                print("ID introducida no valida")
            else:
                contador = 1

                for categoria in listaCategorias:
                    if (categoriaCambiar == categoria.getID()):
                        print(categoria)
                        categoria.mostrarCosas()
                        categoria.mostrarSubCategorias()
                        break
                    contador += 1

                if (contador > len(listaCategorias)):
                    print("La ID no fue encontarda")

        elif (eleccion == 3):
            try:
                categoriaCambiar = int(
                    input("Ingrese la ID de la categoria que desea modificar: "))

            except ValueError:
                print("ID introducida no valida")
            else:
                contador = 1

                for categoria in listaCategorias:
                    if (categoriaCambiar == categoria.getID()):
                        categoria.modificar()
                        break
                    contador += 1

                if (contador > len(listaCategorias)):
                    print("La ID no fue encontarda")

        elif (eleccion == 4):
            try:
                categoriaEliminar = int(
                    input("Ingrese la ID de la categoria que desea eliminar: "))

            except ValueError:
                print("ID introducida no valida")
            else:
                contador = 1

                for categoria in listaCategorias:
                    if (categoriaEliminar == categoria.getID()):
                        del listaCategorias[contador-1]
                        categoria.eliminar()
                        break
                    contador += 1

                if (contador > len(listaCategorias)):
                    print("La ID no fue encontarda")

        elif (eleccion == 5):
            print("Operacion cancelada")

        else:
            print("Opcion introducida invalida")


def autor():
    eleccion = 0

    while (eleccion != 3):
        eleccion = 0

        try:
            eleccion = int(input(
                "Que desea hacer con los autores?\n1. Registrar\n2. Modificar\n3. Salir\n--> "))
        except ValueError:
            print("El numero ingresado no es valido")

        if (eleccion == 1):
            nuevoAutor = Autor()

            listaAutores.append(nuevoAutor)
            if (nuevoAutor.registrar() == 1):
                for i in listaAutores:
                    print(i)

            else: 
                print()

            for i in listaAutores:
                print(i)
                i.mostrarCosas()

        elif (eleccion == 2):
            autorCambiar = input(
                "Ingrese el nombre del autor que desea modificar: ")

            contador = 1

            for autor in listaAutores:
                if (autorCambiar == autor.getNombre()):
                    autor.modificar()
                    break
                contador += 1

            if (contador > len(listaAutores)):
                print("La ID no fue encontarda")

        elif (eleccion == 3):
            print("Operacion cancelada")

        else:
            print("Opcion introducida invalida")


def prestamo():
    eleccion = 0

    while (eleccion != 4):
        eleccion = 0

        try:
            eleccion = int(input(
                "Que desea hacer con los prestamos?\n1. Registrar\n2. Consultar\n3. Finalizar\n4. Cancelar\n--> "))
        except ValueError:
            print("El numero ingresado no es valido")

        if (eleccion == 1):
            nuevoPrestamo = Prestamo()
            ListaPrestamos.append(nuevoPrestamo)
            if (nuevoPrestamo.registrar_prestamo() == 1):
                for i in ListaPrestamos:
                    print(i)

            else:
                print()

        elif (eleccion == 2):
            try:
                lectorConsulta = int(
                    input("Ingrese el ID del lector que desea consultar: "))

            except ValueError:
                print("ID introducida no valida")
            else:
                contador = 1

                for lector in listaLector:
                    if (lectorConsulta == lector.getID()):
                        print(lector)
                        break
                    contador += 1

                if (contador > len(listaLector)):
                    print("La ID no fue encontarda")

        elif (eleccion == 3):
            try:
                prestamoFinalizar = int(input("Ingrese el ID del prestamo que desea finalizar: "))
                fecha_entrega_real = int(input("Ingrese la fecha real de entrega (YYYYMMDD): "))

            except ValueError:
                print("ID introducida no valida")
            else:
                contador = 1

                for prestamo in ListaPrestamos:
                    if (prestamoFinalizar == prestamo.get_id_prestamo()):
                        prestamo.finalizar_prestamo()
                        if (fecha_entrega_real > prestamo.get_fecha_entrega_estimada()):
                            multa = Multa()
                            id_multa = int(input("Ingrese el ID para la multa: "))
                            multa.generar_multa(id_multa, prestamo.get_id_prestamo(), prestamo.get_id_cliente(), prestamo.get_fecha_entrega_estimada(), fecha_entrega_real, listaLector)
                            print(multa)
                        else:
                            print("No se generó multa: entrega a tiempo.")
                        break
                    contador += 1

                if (contador > len(ListaPrestamos)):
                    print("La ID no fue encontarda")

        elif (eleccion == 4):
            print("Operacion cancelada")

        else:
            print("Opcion introducida invalida")

def copia():
    eleccion = 0

    while (eleccion != 5):
        eleccion = 0
        try:
            eleccion = int(input(
                "Que desea hacer con las copias?\n1. Registrar\n2. Consultar\n3. Eliminar\n4. Actualizar estado\n5. Cancelar\n--> "))
        except ValueError:
            print("El numero ingresado no es valido")
        
        if (eleccion == 1):
            nuevaCopia = Copia()
            listaCopias.append(nuevaCopia)
            if (nuevaCopia.registrar() == 1):
                for i in listaCopias:
                    print(i)

            else:
                print()

        elif (eleccion == 2):
            consultacopia = int(input("Ingrese el ID de la copia del libro que desea consultar: "))

            contador = 1

            for copia in listaCopias:
                if (consultacopia == copia.getID()):
                    print(copia)
                    break
                contador += 1

            if (contador > len(listaCopias)):
                print("El ID no fue encontrado")

        elif (eleccion == 3):
            try:
                eliminarCopia = int(
                    input("Ingrese la ID de la copia del libro que desea eliminar: "))

            except ValueError:
                print("ID introducida no valida")
            else:
                contador = 1

                for copia in listaCopias:
                    if (eliminarCopia == copia.getID()):
                        del listaCopias[contador-1]
                        copia.eliminar()
                        break
                    contador += 1

                if (contador > len(listaCopias)):
                    print("La ID no fue encontarda")

        elif(eleccion == 4):
            try:
                modificarCopia = int(
                    input("Ingrese la ID de la copia del libro: "))

            except ValueError:
                print("ID introducida no valida")
            else:
                contador = 1

                for copia in listaCopias:
                    if (modificarCopia == copia.getID()):
                        copia.actualizar_estado()
                        break
                    contador += 1

                if (contador > len(listaCopias)):
                    print("La ID no fue encontarda")

        elif (eleccion == 5):
            print("Operacion cancelada")

        else:
            print("Opcion introducida invalida")

def lector():
    eleccion = 0

    while (eleccion != 5):
        eleccion = 0
        try:
            eleccion = int(input(
                "Que desea hacer con el lector?\n1. Registrar\n2. Modificar\n3. Consultar prestamo y multas\n4. Inhabilitar\n5. Cancelar\n--> "))
        except ValueError:
            print("El numero ingresado no es valido")
        
        if (eleccion == 1):
            nuevolector = Lector()
            listaLector.append(nuevolector)
            if (nuevolector.crear() == 1):
                for i in listaLector:
                    print(i)

            else:
                print()

        elif (eleccion == 2):
            try:
                modlector = int(
                    input("Ingrese la ID del lector que desea modificar: "))

            except ValueError:
                print("ID introducida no valida")
            else:
                contador = 1

                for lector in listaLector:
                    if (modlector == lector.getID()):
                        if(lector.getestado() == "inactivo"):
                            print("lector inhabilitado, no se puede modificar")
                        else:
                            lector.modificar()
                        break
                    contador += 1

                if (contador > len(listaLector)):
                    print("La ID no fue encontarda")

        elif (eleccion == 3):

            consultalector = int(input("Ingrese el ID del lector para consultar prestamos y multas: "))

            enprestamos = 1
            enmultas = 1

            print("\nPréstamos del lector:")
            for prestamo in ListaPrestamos:
                if (consultalector == prestamo.get_id_cliente()):
                    print(prestamo)
                    enprestamos += 1

            if (enprestamos > len(ListaPrestamos)):
                print("No se encontraron préstamos para este lector.")

            print("\nMultas del lector:")
            for multa in listaMultas:
                for prestamo in ListaPrestamos:
                    if multa.get_id_prestamo() == prestamo.get_id_prestamo() and prestamo.get_id_cliente() == consultalector:
                        print(multa)
                        enmultas += 1

            if (enmultas > len(listaMultas)):
                print("No se encontraron multas para este lector.")


        elif(eleccion == 4):
            try:
                inlector = int(
                    input("Ingrese la ID del lector: "))

            except ValueError:
                print("ID introducida no valida")
            else:
                contador = 1

                for lector in listaLector:
                    if (inlector == lector.getID()):
                        lector.inhabilitar()
                        break
                    contador += 1

                if (contador > len(listaLector)):
                    print("La ID no fue encontarda")

        elif (eleccion == 5):
            print("Operacion cancelada")

        else:
            print("Opcion introducida invalida")
            

def multa():
    eleccion = 0

    while (eleccion != 5):
        eleccion = 0
        try:
            eleccion = int(input(
                "Multa: \n1. Consultar\n2. Cancelar\n--> "))
        except ValueError:
            print("El numero ingresado no es valido")
        
        if (eleccion == 1):
            consultarr = int(input("Ingrese el ID de la multa: "))

            contador = 1
            for multa in listaMultas:
                if (consultarr == multa.get_id_multa()):
                    print(multa)
                    contador+= 1

            if (contador > len(listaMultas)):
                print("No existen multas con ese ID.")

        elif (eleccion == 2):
            print("Operacion cancelada")

        else:
            print("Opcion introducida invalida")


eleccion = 0

while (eleccion != 10):

    try:
        eleccion = int(input("\n\n\nBienvenido al sistema de gestion de la biblioteca La Roma\n\nIngrese sobre que quiere operar\n1. Tesis\n2. Articulo Cientifico\n3. Libro\n4. Categoria\n5. Autores\n6. Prestamos\n7. Copia\n8. Lector\n9. Multa\n10. Salir\n--> "))

    except ValueError:
        print("Ingrese un numero")
        eleccion == 0

    else:
        if (eleccion == 1):
            tesis()

        elif (eleccion == 2):
            articulo()

        elif (eleccion == 3):
            libro()

        elif (eleccion == 4):
            categoria()

        elif (eleccion == 5):
            autor()

        elif (eleccion == 6):
            prestamo()

        elif (eleccion == 7):
            copia()

        elif (eleccion == 8):
            lector()

        elif (eleccion == 9):
            multa()

        elif (eleccion == 10):
            print("Gracias por usar el sistema de gestion. Hasta pronto")

        else:
            print("Opcion introducida no valida")
