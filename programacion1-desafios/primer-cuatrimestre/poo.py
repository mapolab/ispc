class Humano:
    __pies = 0
    __brazos = 0
    __ojos = ""

    def __init__(self) -> None:
        self.__pies = 2
        self.__brazos = 2
        self.__ojos = "amarillos"

    def camina(self):
        print("Empece a caminar")

    def ver_brazos(self):
        return self.__brazos

    def modifica_brazos(self, cantidad):
        self.__brazos = cantidad


    def color_ojos(self):
        return self.__ojos


pedro = Humano()

pedro.camina()

pedro.modifica_brazos(7)

print(pedro.color_ojos())

print(pedro.ver_brazos())
