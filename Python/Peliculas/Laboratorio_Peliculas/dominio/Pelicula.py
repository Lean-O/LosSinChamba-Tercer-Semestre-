class Pelicula: # esta es la clase pelicula para poder identificar las peliculas por su nombres
    def __init__(self, nombre): # constructor q recibe el nombre de la pelicula como argumento para asignarlo
        self._nombre = nombre # el nombre de la pelicula se almacena en un atributo privado

    def __str__(self): # metodo para convertir el nombre de la pelicula en una cadena de texto
        return f"Película: {self._nombre}" # devuelve el nombre de la pelicula

    @property # decorador para administrar el acceso al nombre de las peliculas
    def nombre(self): # devuelve el nombre de la pelicula cuando se accede a la propiedad nombre
        return self._nombre # devuelve el valor del atributo privado, q seria nombre, permitiendo su lectura

    @nombre.setter # decorador que permite modificar el nomrbe de la pelicula a traves de la propiedad
    def nombre(self, nombre): # permite recibir un nuevo nombre para la pelicula a traves de la propiedad nombre
        self._nombre = nombre # le asigna el nuevo nombre al atributo privado, permitiendo su modificacion