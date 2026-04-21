from dominio.Pelicula import Pelicula # importamos la clase pelicula para poder crear objetos de tipo pelicula y utilizarlos en el programa
from servicio.CatalogoPeliculas import CatalogoPeliculas as cp # importamos la clase CatalogoPeliculas y le asignamos el alias cp para poder usarla de manera mas sencilla en el programa

opcion = None #variable para almacenar la opcion elegida por el user

while opcion != 4: # mientras la opcion elegida NO sea la 4, q es la opcion de salir, el programa seguira ejecutandose
    try: # uso un bloque try para manejar posibles errores que puedan ocurrir al ingresar la opcion del menu, como por ejemplo ingresar un valor no numerico o un numero fuera del rango de opciones disponibles
        print(''' 
        *** MENÚ DE OPCIONES ***
        1) Agregar película
        2) Listar películas
        3) Eliminar archivo de películas
        4) Salir
        ''') # imprimo el menu de opciones para que el user pueda elegir lo que desea hacer
        opcion = int(input('Elegí una opción (1-4): ')) # pido al user que ingrese una opcion y la convierto a entero para poder compararla con las opciones del menu, si el user ingresa un valor no numerico, se lanzara una excepcion ValueError que sera manejada en el bloque except correspondiente

        if opcion == 1: # si el user elige la opcion 1, se le pedira que ingrese el nombre de la pelicula que desea agregar al catalogo, se creara un objeto de tipo Pelicula con ese nombre y se llamara al metodo agregar_pelicula de la clase CatalogoPeliculas para agregar esa pelicula al archivo del catalogo
            nombre_pelicula = input('Ingrese el nombre de la película: ') # pido al user que ingrese el nombre de la pelicula que desea agregar al catalogo, este valor se almacenara en la variable nombre_pelicula
            pelicula = Pelicula(nombre_pelicula) # creo un objeto de tipo Pelicula usando el nombre ingresado por el user, este objeto se almacenara en la variable pelicula
            cp.agregar_pelicula(pelicula) # llamo al metodo agregar_pelicula de la clase CatalogoPeliculas, usando el alias cp, y le paso el objeto pelicula que acabo de crear para que se agregue al catalogo, este metodo se encargara de escribir el nombre de la pelicula en el archivo correspondiente y mostrar un mensaje de confirmacion
        
        elif opcion == 2: # si el user elige la opcion 2, se llamara al metodo listar_peliculas de la clase CatalogoPeliculas para mostrar en pantalla la lista de peliculas que se encuentran en el catalogo, este metodo se encargara de leer el contenido del archivo y mostrarlo formateado como un catalogo de peliculas
            cp.listar_peliculas() # llamo al metodo listar_peliculas de la clase CatalogoPeliculas, usando el alias cp, para mostrar en pantalla la lista de peliculas que se encuentran en el catalogo, este metodo se encargara de leer el contenido del archivo y mostrarlo formateado como un catalogo de peliculas
            
        elif opcion == 3: # si el user elige la opcion 3, se llamara al metodo eliminar de la clase CatalogoPeliculas para eliminar el archivo que contiene las peliculas del catalogo, este metodo se encargara de intentar eliminar el archivo y manejar las excepciones correspondientes en caso de que el archivo no exista o ocurra algun error al intentar eliminarlo
            cp.eliminar() # llamo al metodo eliminar de la clase CatalogoPeliculas, usando el alias cp, para eliminar el archivo que contiene las peliculas del catalogo, este metodo se encargara de intentar eliminar el archivo y manejar las excepciones correspondientes en caso de que el archivo no exista o ocurra algun error al intentar eliminarlo

    except ValueError: # manejo la excepcion ValueError que se lanzara si el user ingresa un valor no numerico al elegir una opcion del menu, en este caso se le informara al user que debe ingresar un numero entero y se le volvera a mostrar el menu para que pueda elegir una opcion valida
        print('Error: Por favor, ingrese un número entero.') # imprimo un mensaje de error indicando que el user debe ingresar un numero entero para elegir una opcion del menu, este mensaje se mostrara cada vez que el user ingrese un valor no numerico al elegir una opcion del menu
        opcion = None # reinicio la variable opcion a None para que el programa siga ejecutandose y vuelva a mostrar el menu, permitiendo al user elegir una opcion valida en lugar de salir del programa debido a un error de entrada
    except Exception as e: # manejo de cualquier otra excepcion que pueda ocurrir durante la ejecucion del programa, como por ejemplo errores al escribir en el archivo, errores al leer el archivo, errores al eliminar el archivo, etc., en este caso se le informara al user que ocurrio un error inesperado y se mostrara la descripcion del error para que pueda entender lo que paso y tomar las medidas necesarias para solucionarlo
        print(f'Ocurrió un error inesperado: {e}') # imprimo un mensaje de error indicando que ocurrio un error inesperado durante la ejecucion del programa, junto con la descripcion del error para que el user pueda entender lo que paso y tomar las medidas necesarias para solucionarlo, este mensaje se mostrara cada vez que ocurra una excepcion que no sea un ValueError al elegir una opcion del menu o al ejecutar alguna de las funciones relacionadas con el catalogo de peliculas
        opcion = None # reinicio la variable opcion a None para que el programa siga ejecutandose y vuelva a mostrar el menu, permitiendo al user elegir una opcion valida en lugar de salir del programa debido a un error inesperado

print('Saliendo del programa... ¡Éxitos con la entrega!') # cuando el user elige la opcion 4 para salir del programa, se imprimira un mensaje de despedida indicando que se esta saliendo del programa y deseando exitos con la entrega, este mensaje se mostrara justo antes de que el programa termine su ejecucion y cierre la ventana de la consola o terminal donde se esta ejecutando el programa, este mensaje es una forma de agradecer al user por usar el programa y desearle lo mejor en su entrega, ya sea un proyecto, una tarea, un examen, etc.