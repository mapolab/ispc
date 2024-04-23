"""lol"""

numeros = [3, -5, 90, -20, 150, -220, 44, -5, 2, 4]
pares = []
sumatoria = 0

for i in numeros:
    if i > 0:
        sumatoria += i
        pares.append(i)

print("Los numeros pares son: ", pares)
print("La sumatoria de los pares son: ", sumatoria)
