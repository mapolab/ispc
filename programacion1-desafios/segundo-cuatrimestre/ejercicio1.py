"""
Persona. crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
Construye los siguientes métodos para la clase:
a. Un constructor, donde los datos pueden estar vacíos.
b. Los setters y getters para cada uno de los atributos. Hay que validar las
entradas de datos.
c. mostrar(): Muestra los datos de la persona.
d. esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
Además, crea en una aplicación de consola que permita al usuario crear un objeto
Persona y evaluar si es mayo o menor de edad..
"""


class Persona():
    def __init__(self, nombre, edad, dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            raise Exception("Error en el nombre ingresado")

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):

        if isinstance(edad, int):
            self.__edad = edad
        else:
            raise Exception("EL edad ingresado no es valido")

    def get_dni(self):
        return self.__dni

    def set_dni(self, dni):
        if isinstance(dni, int):
            self.__dni = dni
        else:
            raise Exception("EL dni ingresado no es valido")

    def mostrar(self):
        return f"Nombre:{self.get_nombre()} Edad:{self.get_edad()} DNI:{self.get_dni()}"

    def esMayorDeEdad(self):
        if self.__edad >= 18:
            return "Es mayor de edad."
        else:
            return "No es mayor de edad."


pepe = Persona("Pepe", 22, 27644034)

pepe.set_edad(70)

print(pepe.esMayorDeEdad())

print(pepe.mostrar())
