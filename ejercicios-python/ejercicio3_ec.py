"""lol"""

i = 0
mujeres = 0
varones = 0
mayores = 0
menores = 0

while i < 3:
    sexo = input("Ingresa el sexo del persona (f o m): ")
    edad = int(input("Ingresa la edad de la persona: "))

    if edad > 18:
        mayores += 1
    else:
        menores += 1

    if sexo == "m":
        varones += 1
    else:
        mujeres += 1

    i += 1

print("La cantidad de mayores son: ", mayores)
print("La cantidad de menores son: ", menores)

print("La cantidad de varones son: ", varones)
print("La cantidad de mujeres son: ", mujeres)
