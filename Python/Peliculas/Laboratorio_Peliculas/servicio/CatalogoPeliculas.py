import os # importo para eliminar el archivo

class CatalogoPeliculas: # esta clase se encarga de gestionar el catalogo
    ruta_archivo = 'peliculas.txt' # atributo de la clase que define la ruta del archivo en donde se guardan las peliculas

    @staticmethod # metodo estatico para agregar peliculas al catalogo
    def agregar_pelicula(pelicula): # recibe un objeto pelicula como argumento para agregarlo al catalogo
        try: # uso el modo de apertura
            # 'a' (append) para agregar sin borrar lo anterior
            with open(CatalogoPeliculas.ruta_archivo, 'a', encoding='utf8') as archivo: # abro el archivo en modo de "agregar" y con codificacion utf8 para que pueda leer bien acentos y eñes
                archivo.write(f'{pelicula.nombre}\n') # escribo el nombre de la pelicula seguido de un salto de linea para que cada peli quede en una linea diferente
            print(f'Se ha agregado: {pelicula.nombre}') # imprimo un mensaje de confirmacion junto con el nombre de la peli agregada
        except Exception as e: # manejo de excepciones para cualq error que pueda ocurrir al intentar escribir en el archivo
            print(f'Error al agregar película: {e}') # imprimo un mensaje de error junto con la descripcion del error

    @staticmethod
    def listar_peliculas(): # metodo estatico para listar las pelis del catalogo
        try: # intento abrir el archivo en modo de lectura para mostrar el contenido
            with open(CatalogoPeliculas.ruta_archivo, 'r', encoding='utf8') as archivo: # abro el archivo en modo de lectura y con la codificacion utf8 para que lea sin problemas
                print('--- Catálogo de Películas ---') # imprimo el encabezado del catalogo
                print(archivo.read()) # leo el contenido del archivo y lo imprimo, mostrando la lista de peliculas guardadas
        except FileNotFoundError: # manejo la excepcion de archivo no encontrado
            print('El archivo no existe todavía. Agregá una película primero.') # imprimo un mensaje indicando que el archivo no existe y sugiriendo agregar una peli primero
        except Exception as e: # manejo de cualq otra excepcion 
            print(f'Error al listar películas: {e}') # imprimo un mensaje de error junto con la descripcion del mismo

    @staticmethod # metodo estatico para eliminar el archivo de peliculas
    def eliminar(): # este metodo intenta eliminar el archivo de las peliculas, y si no existe, maneja la excepcion correspondiente
        try: # intento eliminar el archivo usando os.remove, que es la funcion de la biblioteca os para eliminar archivos
            os.remove(CatalogoPeliculas.ruta_archivo) # elimino el archivo usando la ruta definida en el atributo de la clase
            print(f'Archivo {CatalogoPeliculas.ruta_archivo} eliminado correctamente.') # imprimo un mensaje de confirmacion indicando 
        except FileNotFoundError: # manejo la excepcion de archivo no encontrado
            print('No se pudo eliminar: El archivo no existe.') # imprimo mensaje de error
        except Exception as e: # manejo de cualquier otra excepcion que pueda ocurrir
            print(f'Error al eliminar el archivo: {e}') # imprimo un mensaje de error junto con la descripcion del mismo