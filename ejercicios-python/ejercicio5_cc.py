"""lol"""

numero = int(input("Ingreso un nro del 1 a 12: "))
meses = {1: 'Enero', 2: 'Febrero', 3: 'Marzo',
         4: 'Abril', 5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Nomviembre', 12: 'Diciembre'}

# print("x:", dias[1])

if numero == 1:
    print("El nro corresponde a : ", meses.get(1))
elif numero == 2:
    print("El nro corresponde a : ", meses.get(2))
elif numero == 3:
    print("El nro corresponde a : ", meses.get(3))
elif numero == 4:
    print("El nro corresponde a : ", meses.get(4))
elif numero == 5:
    print("El nro corresponde a : ", meses.get(5))
elif numero == 6:
    print("El nro corresponde a : ", meses.get(6))
elif numero == 7:
    print("El nro corresponde a : ", meses.get(7))
elif numero == 8:
    print("El nro corresponde a : ", meses.get(8))
elif numero == 9:
    print("El nro corresponde a : ", meses.get(9))
elif numero == 10:
    print("El nro corresponde a : ", meses.get(10))
elif numero == 11:
    print("El nro corresponde a : ", meses.get(11))
elif numero == 12:
    print("El nro corresponde a : ", meses.get(12))
else:
    print("El nro no esta en el rango especificado")
