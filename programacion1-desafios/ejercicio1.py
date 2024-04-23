"""
1- Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el
número con los dígitos en orden inverso: .
"""

numero = input(" Ingrese un Nro de 3 digitos: ")

if len(numero) == 3:
    nro_invertido = ""

    i = 1
    while i < 4:
        nro_invertido = nro_invertido + numero[-i]
        i += 1

    print("invertido: ", nro_invertido)
else:
    print("Ingresaste una cantidad de digitos incorrecta")
