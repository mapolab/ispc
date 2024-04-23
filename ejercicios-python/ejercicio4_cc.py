"""lol"""

numero = int(input("Ingreso un nro del 1 a 7: "))
dias = {1: 'Lunes', 2: 'Martes', 3: 'Miercoles',
        4: 'Jueves', 5: 'Viernes', 6: 'Sabado', 7: 'Domingo'}

# print("x:", dias[1])

if numero == 1:
    print("El nro corresponde a : ", dias.get(1))
elif numero == 2:
    print("El nro corresponde a : ", dias.get(2))
elif numero == 3:
    print("El nro corresponde a : ", dias.get(3))
elif numero == 4:
    print("El nro corresponde a : ", dias.get(4))
elif numero == 5:
    print("El nro corresponde a : ", dias.get(5))
elif numero == 6:
    print("El nro corresponde a : ", dias.get(6))
elif numero == 7:
    print("El nro corresponde a : ", dias.get(7))
else:
    print("El nro no esta en el rango especificado")
