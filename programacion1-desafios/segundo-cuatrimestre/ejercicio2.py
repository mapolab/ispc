"""
Área y Perímetro. Crea una clase Rectángulo que permita calcular su área y su
perímetro. Además, crea en una aplicación de consola que permita al usuario crear
un objeto Perímetro y realizar los cálculos.
"""


class Rectángulo():
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def calcular_area(self):
        calculo = self.__base * self.__altura / 2
        return calculo

    def calcular_perimetro(self):
        calculo = self.__base * 2 + self.__altura * 2
        return calculo


if __name__ == "__main__":
    print("Calculadora de Perimetro de un Rectangulo")
    base = int(input("Ingrese la base:"))
    altura = int(input("Ingrese la altura:"))

    perimetro = Rectángulo(base, altura)
    print("El perimetro es de:", perimetro.calcular_perimetro())
    print("El area es de:", perimetro.calcular_area())
