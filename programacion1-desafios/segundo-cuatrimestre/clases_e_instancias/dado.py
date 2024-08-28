"""
Desafío. Intenta crear una clase Dado que cumpla los siguientes
requerimientos:
* el dado debe tener un número de caras (por defecto 6)
* debe ser capaz de lanzarse y devolver un número aleatorio entre 1
y el número de caras.
"""
from random import *


class Dado:

    def __init__(self, nro_caras=6):
        self.nro_caras = nro_caras
        self.nro_final = 0

    def lanzar(self):
        nro_aleatorio = randint(1, self.nro_caras)
        nro_final = nro_aleatorio
        return nro_aleatorio


tirada = Dado()
print(tirada.lanzar())
