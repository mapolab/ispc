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
                return True
            else:
                return False
        else:
            raise ValueError("El reproductor esta apagado")

    def pausar_cancion(self):
        if self.__reproducciendo == True:
            self.__reproducciendo = False
        else:
            self.__reproducciendo = True

    def siguiente_cancion(self, posicion=1):
        nro_posiciones = len(self.__lista)
        print("cantidad de posc:", nro_posiciones)
        nro_posicion_actual = self.__lista.index(
            self.__cancion_actual) + posicion
        if nro_posicion_actual < nro_posiciones:
            print("pos actual:", self.__cancion_actual)
            self.__cancion_actual = self.__lista[nro_posicion_actual]
            return True
        else:
            # Si el nro de posiciones a adelantar esta fuera de rango volver al primer elemento
            self.__cancion_actual = self.__lista[0]
            return False

    def agregar_cancion(self, valor):
        if valor in self.__lista:
            raise ValueError("La cancion ya esta en lista")
        else:
            self.__lista.append(valor)
            return True

    def mostrar_canciones(self):
        return self.__lista
