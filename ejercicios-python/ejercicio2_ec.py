"""lol"""

numeros = [0, 200, 40, 10, 33, 66, 120, 99, 5500, 1, 540]

menor = 0
mayor = 0

for n in numeros:
    if n < 100:
        menor += 1
    else:
        mayor += 1


print("Hay ", menor, " menores de 100")
print("Hay ", mayor, " mayores de 100")

numeros.sort()
print("El numero mayor es: ", numeros[-1])
print("El numero menor es: ", numeros[0])
