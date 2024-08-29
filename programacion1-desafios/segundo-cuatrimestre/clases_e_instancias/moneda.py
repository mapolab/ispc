"""
Conversor de Monedas. Crea una clase Moneda que permita la conversión
entre monedas (ej. dólares a pesos). Implementa los métodos __str__ y
__add__ para mostrar la cantidad convertida y sumar cantidades en
diferentes monedas.
"""


class Moneda:
    valor_moneda = {
        'USD': 1350,
        'ARS': 1
    }

    def __init__(self, cantidad, tipo_moneda):
        self.cantidad = cantidad
        self.tipo_moneda = tipo_moneda

    def __add__(self, otro):
        if self.tipo_moneda == otro.tipo_moneda:
            return Moneda(self.cantidad + otro.cantidad, self.tipo_moneda)
        else:
            otra_conversion = otro.convertir(self.tipo_moneda)
            return Moneda(self.cantidad + otra_conversion, self.tipo_moneda)

    def __str__(self):
        return f"{self.cantidad:.2f} {self.tipo_moneda}"

    def convertir(self, moneda_a_convertir):
        match moneda_a_convertir:
            case 'ARS':
                monto_convertido = self.cantidad * self.valor_moneda['USD']
            case 'USD':
                monto_convertido = self.cantidad / self.valor_moneda['USD']
        return monto_convertido


dolar = Moneda(10, 'USD')
peso = Moneda(10000, 'ARS')


print(dolar)
print(f"{dolar.convertir('ARS'):.2f} ARS")
print(" ")
print(peso)
print(f"{peso.convertir('USD'):.2f} USD")

suma = dolar + peso
print(" ")
print("La suma da:", suma)
