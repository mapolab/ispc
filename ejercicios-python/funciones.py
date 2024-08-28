"""xxx"""
from math import sqrt, radians, fabs, sin

# Ejemplo 1: Calcular la raíz cuadrada
numero = 25
raiz_cuadrada = sqrt(numero)
print(f"La raíz cuadrada de {numero} es {raiz_cuadrada}")
# Ejemplo 2: Calcular el seno de un ángulo en radianes
angulo_radianes = radians(30)
seno = sin(angulo_radianes)
print(f"El seno de {angulo_radianes} radianes es {seno:.2f}")
# Ejemplo 3: Redondear un número
numero_decimal = 3.14159
numero_redondeado = round(numero_decimal, 2)
print(f"El número redondeado es {numero_redondeado}")
# Ejemplo 4: Valor absoluto
numero_negativo = -10
valor_absoluto = fabs(numero_negativo)
print(f"El valor absoluto de {numero_negativo} es {valor_absoluto}")
