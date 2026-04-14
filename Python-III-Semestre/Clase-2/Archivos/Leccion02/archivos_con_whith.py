# MANEJO DE CONTEXTO WITH: sintaxis simplificada, abre y cierra el archivo
from manejo_archivo import ManejoArchivos

#with open('LosSinChamba.txt', 'r', encoding='utf8') as archivo:
    #print(archivo.read())
# No hace falta ni el try, ni el finally
# en el contexto de with lo que se ejecuta de manera automatica
# Utiliza diferentes métodos: __enter__ este es el que abre
# Ahora el siguiente método es el que cierra: __exit__

with ManejoArchivos('LosSinChamba.txt') as archivo:
    print(archivo.read())