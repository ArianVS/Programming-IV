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

    while (eleccion != 7):
        eleccion = 0

        try:
            eleccion = int(input(
                "\n\nQue desea hacer con la tesis?\n1. Registrar\n2. Consultar\n3. Modificar\n4. Eliminar\n5. Asignar una categoria\n6. Mostrar Tesis\n7. Cancelar\n--> "))
        except ValueError:
            print("El numero ingresado no es valido")

        if (eleccion == 1):
            nuevaTesis = Tesis()

            if (nuevaTesis.registrar(listaAutores, listaTesis) == 1):
                listaTesis.append(nuevaTesis)
            else:
                print()

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
                        tesis.modificar(listaAutores, listaTesis)
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
            for i in listaTesis:
                print(i)

        elif (eleccion == 7):
            print("Ejecucion cancelada")

        else:
            print("Opcion introducida no valida")


def articulo():
    eleccion = 0

    while (eleccion != 7):
        eleccion = 0

        try:
            eleccion = int(input(
                "\n\nQue desea hacer con el articulo cientifico?\n1. Registrar\n2. Consultar\n3. Modificar\n4. Eliminar\n5. Asignar una categoria\n6. Mostrar Articulos\n7. Cancelar\n--> "))
        except ValueError:
            print("El numero ingresado no es valido")

        if (eleccion == 1):
            nuevoArticulo = Articulo()

            if (nuevoArticulo.registrar(listaAutores, listaArticulo) == 1):

                listaArticulo.append(nuevoArticulo)
            else:
                print()

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
                    articulo.modificar(listaAutores, listaArticulo)
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
            for i in listaArticulo:
                print(i)

        elif (eleccion == 7):
            print("Ejecucion cancelada")

        else:
            print("Opcion introducida no valida")


def libro():
    eleccion = 0

    while (eleccion != 7):
        eleccion = 0

        try:
            eleccion = int(input(
                "Que desea hacer con los libros?\n1. Registrar\n2. Consultar\n3. Modificar\n4. Eliminar\n5. Asignar Categoria\n6. Mostrar Libros\n7. Cancelar\n--> "))
        except ValueError:
            print("El numero ingresado no es valido")

        if (eleccion == 1):
            nuevoLibro = Libro()

            if nuevoLibro.registrar(listaAutores, listaCopias, listaLibro) == 1:
                listaLibro.append(nuevoLibro)
            else:
                print()

        elif (eleccion == 2):
            libroConsulta = int(input(
                "Ingrese el ISBN del libro que desea consultar: "))

            contador = 1

            for libro in listaLibro:
                if (libroConsulta == libro.getISBN()):
                    print(libro)
                    break
                contador += 1

            if (contador > len(listaLibro)):
                print("El ISBN no fue encontrado")

        elif (eleccion == 3):
            libroCambiar = int(input(
                "Ingrese el ISBN del libro que desea modificar: "))

            contador = 1

            for libro in listaLibro:
                if (libroCambiar == libro.getISBN()):
                    libro.modificar(listaAutores, listaLibro)
                    break
                contador += 1

                if (contador > len(listaLibro)):
                    print("El ISBN no fue encontrado")

        elif (eleccion == 4):
            libroEliminar = int(input(
                "Ingrese el ISBN del libro que desea eliminar: "))

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
                libroAsignar = int(input(
                    "Ingrese el ISBN del libro al que desea asignar una categoria: "))
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
            for i in listaLibro:
                print(i)
        elif (eleccion == 7):
            print("Ejecucion cancelada")

        else:
            print("Opcion introducida no valida")


def categoria():
    eleccion = 0

    while (eleccion != 6):
        eleccion = 0

        try:
            eleccion = int(input(
                "Que desea hacer con las categorias?\n1. Registrar\n2. Consultar\n3. Modificar\n4. Eliminar\n5. Mostrar Categorias\n6. Cancelar\n--> "))
        except ValueError:
            print("El numero ingresado no es valido")

        if (eleccion == 1):
            try:
                nuevaCategoria = Categoria()

                if (nuevaCategoria.registrar(listaCategorias) == 1):

                    siono = input("Es una subcategoria? S/N: ")

                    if (siono.upper() == 'S'):
                        padre = int(
                            input("Ingrese la ID de la categoria padre: "))

                        contador = 1
                        for categoria in listaCategorias:
                            if (padre == categoria.getID()):
                                listaCategorias.append(nuevaCategoria)
                                categoria.agnadirSubCategoria(nuevaCategoria)
                                break
                            contador += 1

                            if (contador > len(listaCategorias)):
                                listaCategorias.append(nuevaCategoria)
                                print(
                                    "Padre no encontrado, creada como categoria independiente")

                    else:
                        listaCategorias.append(nuevaCategoria)

            except ValueError:
                print("Ultimo valor introducido incorrectamente, intente nuevamente")

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
            for i in listaCategorias:
                print(i)
                i.mostrarCosas()
                i.mostrarSubCategorias()

        elif (eleccion == 6):
            print("Operacion cancelada")

        else:
            print("Opcion introducida invalida")


def autor():
    eleccion = 0

    while (eleccion != 4):
        eleccion = 0

        try:
            eleccion = int(input(
                "Que desea hacer con los autores?\n1. Registrar\n2. Modificar\n3. Mostrar Autores\n4. Salir\n--> "))
        except ValueError:
            print("El numero ingresado no es valido")

        if (eleccion == 1):
            nuevoAutor = Autor()

            if (nuevoAutor.registrar(listaAutores) == 1):
                listaAutores.append(nuevoAutor)

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
            for i in listaAutores:
                print(i)

        elif (eleccion == 4):
            print("Operacion cancelada")

        else:
            print("Opcion introducida invalida")


def prestamo():
    eleccion = 0

    while (eleccion != 5):
        eleccion = 0

        try:
            eleccion = int(input(
                "Que desea hacer con los prestamos?\n1. Registrar\n2. Consultar\n3. Finalizar\n4. Mostrar Prestamos\n5. Cancelar\n--> "))
        except ValueError:
            print("El numero ingresado no es valido")

        if (eleccion == 1):
            nuevoPrestamo = Prestamo()
            if (nuevoPrestamo.registrar_prestamo(listaCopias, listaArticulo, listaTesis, listaLector,ListaPrestamos) == 1):

                ListaPrestamos.append(nuevoPrestamo)
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
                prestamoFinalizar = int(
                    input("Ingrese el ID del prestamo que desea finalizar: "))
                fecha_entrega_real = int(
                    input("Ingrese la fecha real de entrega (YYYYMMDD): "))
                fecha_entrega_real = date(fecha_entrega_real//10000, (fecha_entrega_real//100) % 100, fecha_entrega_real % 100)

            except ValueError:
                print("ID introducida no valida")
            else:
                contador = 1

                for prestamo in ListaPrestamos:
                    if (prestamoFinalizar == prestamo.get_id_prestamo()):
                        prestamo.finalizar_prestamo()
                        
                        if (fecha_entrega_real > prestamo.get_fecha_entrega_estimada()):
                            multa = Multa()
                            id_multa = int(
                                input("Ingrese el ID para la multa: "))
                            id_repetido = False
                            for m in listaMultas:
                                if (id_multa == m.get_id_multa()):
                                    print("El ID ya existe, intente nuevamente")
                                    id_repetido = True
                                    break

                            if not id_repetido:
                                nueva_multa = Multa()
                                if nueva_multa.generar_multa(id_multa, prestamo.get_id_prestamo(), prestamo.get_id_cliente(), prestamo.get_fecha_entrega_estimada(), fecha_entrega_real, listaLector):
                                    print("Multa generada correctamente, guardando en listaMultas.")
                                    listaMultas.append(nueva_multa)
                                else:
                                    print()
                        else:
                            print("No se generó multa: entrega a tiempo.")
                        break
                    contador += 1

                if (contador > len(ListaPrestamos)):
                    print("La ID no fue encontrada")

        elif (eleccion == 4):
            for i in ListaPrestamos:
                print(i)

        elif (eleccion == 5):
            print("Operacion cancelada")

        else:
            print("Opcion introducida invalida")


def copia():
    eleccion = 0

    while (eleccion != 6):
        eleccion = 0
        try:
            eleccion = int(input(
                "Que desea hacer con las copias?\n1. Registrar\n2. Consultar\n3. Eliminar\n4. Actualizar estado\n5. Mostrar copias\n6. Cancelar\n--> "))
        except ValueError:
            print("El numero ingresado no es valido")

        if (eleccion == 1):
            nuevaCopia = Copia()
            listaCopias.append(nuevaCopia)
            if (nuevaCopia.registrar(listaCopias) == 1):
                for i in listaCopias:
                    print(i)

            else:
                print()

        elif (eleccion == 2):
            consultacopia = int(
                input("Ingrese el ID de la copia del libro que desea consultar: "))

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

        elif (eleccion == 4):
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
            for i in listaCopias:
                print(i)

        elif (eleccion == 6):
            print("Operacion cancelada")

        else:
            print("Opcion introducida invalida")


def lector():
    eleccion = 0

    while (eleccion != 6):
        eleccion = 0
        try:
            eleccion = int(input(
                "Que desea hacer con el lector?\n1. Registrar\n2. Modificar\n3. Consultar prestamo y multas\n4. Inhabilitar\n5. Mostrar Lectores\n6. Cancelar\n--> "))
        except ValueError:
            print("El numero ingresado no es valido")

        if (eleccion == 1):
            nuevolector = Lector()
            listaLector.append(nuevolector)
            if (nuevolector.crear(listaLector) == 1):
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
                        if (lector.getestado() == "inactivo"):
                            print("lector inhabilitado, no se puede modificar")
                        else:
                            lector.modificar()
                        break
                    contador += 1

                if (contador > len(listaLector)):
                    print("La ID no fue encontarda")

        elif (eleccion == 3):

            consultalector = int(
                input("Ingrese el ID del lector para consultar prestamos y multas: "))

            enprestamos = False
            enmultas = False

            print("\nPréstamos del lector:")
            for prestamo in ListaPrestamos:
                if (consultalector == prestamo.get_id_cliente()):
                    print(prestamo)
                    enprestamos = True

            if not enprestamos:
                print("No se encontraron préstamos para este lector.")

            print("\nMultas del lector:")
            for multa in listaMultas:
                for prestamo in ListaPrestamos:
                    if (multa.get_idlector() == consultalector):
                        print(multa)
                        enmultas = True

            if not enmultas: 
                print("No se encontraron multas para este lector.")

        elif (eleccion == 4):
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
            for i in listaLector:
                print(i)

        elif (eleccion == 6):
            print("Operacion cancelada")

        else:
            print("Opcion introducida invalida")


def multa():
    eleccion = 0

    while (eleccion != 4):
        eleccion = 0
        try:
            eleccion = int(input(
                "Multa: \n1. Consultar\n2. Mostrar Multas\n3. Levantar Multas\n4. Cancelar\n--> "))
        except ValueError:
            print("El numero ingresado no es valido")

        if (eleccion == 1):
            consultarr = int(input("Ingrese el ID de la multa: "))

            multa_encontrada = False 
            for multa in listaMultas:
                if (consultarr == multa.get_id_multa()):
                    print(multa)
                    multa_encontrada = True

            if not multa_encontrada:
                print("No existen multas con ese ID.")

        elif (eleccion == 2):
            for i in listaMultas:
                print(i)

        elif (eleccion == 3):
            consultarr = int(input("Ingrese el ID de la multa: "))
            id = int(input("Ingrese el ID del lector: "))

            multa_encontrada = False 
            for multa in listaMultas:
                if (consultarr == multa.get_id_multa()):
                    print(multa)
                    multa.levantar_multa()
                    multa.levantar_multas_auto(date.today(), id, listaLector)
                    multa_encontrada = True

            if not multa_encontrada:
                print("No existen multas con ese ID.")

        elif (eleccion == 4):
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
