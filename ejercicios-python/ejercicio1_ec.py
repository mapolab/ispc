"""lol"""

numeros = [2, 7, 9, 20]
pares = 0
impares = 0
suma_pares = 0

for n in numeros:
    if n % 2 == 0:
        pares += 1
        suma_pares = suma_pares + n
    else:
        impares += 1

print("Hay ", pares, " pares")
print("Hay ", impares, " impares")
print("La suma de los impares da:", suma_pares)
