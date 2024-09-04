""" 
Reproductor de Musica 
Define 3 comportamientos clave del objeto que involucren lógica de
programación (no solo getters/setters).
"""


class Reproductor:

    def __init__(self, lista):
        self.__lista = lista
        self.__encendido = False
        self.__reproducciendo = False
        self.__cancion_actual = ""

    def get_encedido(self):
        return self.__encendido

    def set_encedido(self, valor):
        self.__encendido = valor

    def __str__(self):
        if self.__reproducciendo == True:
            estado = "Reproducciendo"
        else:
            estado = "Pausado"
        return f" Cancion Actual = { self.__cancion_actual}\n Estado = {estado}\n Encendido = {self.__encendido}"

    def reproducir_cancion(self, cancion):
        if self.__encendido == True:
            if cancion in self.__lista:
                self.__reproducciendo = True
                self.__cancion_actual = cancion
            else:
                raise ValueError("La cancion no esta en lista")
        else:
            raise ValueError("El reproductor esta apagado")

    def pausar_cancion(self):
        if self.__reproducciendo == True:
            self.__reproducciendo = False
        else:
            self.__reproducciendo = True

    def siguiente_cancion(self):
        nro_posiciones = len(self.__lista)
        nro_posicion_actual = self.__lista.index(self.__cancion_actual) + 1
        if nro_posicion_actual < nro_posiciones:
            self.__cancion_actual = self.__lista[nro_posicion_actual]
        else:
            self.__cancion_actual = self.__lista[0]


canciones = ["Enter Sandman", "Linkin Park", "Paranoid", "Eminem",
             "Master of Puppets", "Painkiller", "Iron Man", "South of Heaven"]


playlist = Reproductor(canciones)
playlist.set_encedido(True)
playlist.reproducir_cancion("Eminem")
playlist.siguiente_cancion()
print(playlist)
