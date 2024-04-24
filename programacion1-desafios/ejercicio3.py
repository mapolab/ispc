"""Escribir un programa que pida al usuario un número entero y muestre por pantalla si
es un número primo o no."""

numero = int(input("Ingrese un nro entero: "))
conteo = 0

for i in range(2, numero):
    if numero % i == 0:
        conteo += 1

if conteo > 2:
    print(numero, "No es primo")
else:
    print("El número", numero, "es primo")
