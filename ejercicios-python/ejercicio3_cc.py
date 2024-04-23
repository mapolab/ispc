"""lol"""

numero1 = 1221
numero2 = 130
numero3 = 150


if numero1 > numero2 and numero1 > numero3:
    if numero1 % 2 == 0:
        print("El nro1 es Par y es el mayor")
    else:
        print("El nro1 es imPar y es el mayor")

if numero2 > numero1 and numero2 > numero3:
    if numero2 % 2 == 0:
        print("El nro2 es Par y es el mayor")
    else:
        print("El nro2 es imPar y es el mayor")

if numero3 > numero1 and numero3 > numero2:
    if numero3 % 2 == 0:
        print("El nro3 es Par y es el mayor")
    else:
        print("El nro3 es imPar y es el mayor")
