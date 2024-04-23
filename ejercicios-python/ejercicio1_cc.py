"""lol"""


lado1 = input("Ingrese lado 1:")
lado2 = input("Ingrese lado 2:")
lado3 = input("Ingrese lado 3:")

if lado1 == lado2 == lado3:
    print("Es un triangulo equilatero")
elif lado1 == lado2 and lado2 != lado3:
    print("Es un triangulo isosceles")
elif lado2 == lado3 and lado3 != lado1:
    print("Es un triangulo isosceles")
elif lado3 == lado1 and lado2 != lado1:
    print("Es un triangulo isosceles")
