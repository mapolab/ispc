"""xx"""


monto = 5000
valor_dolar = 890

opcion = input(
    "Tienes $5000 y 5000usd, si quieres cambiar los pesos presiona P o si quieres cambiar los dolare preciosa D:")

if opcion == "p":
    calculo = monto / valor_dolar
    print("El cambio de $5000 a dolar es:", calculo)
elif opcion == "d":
    calculo = monto * valor_dolar
    print("El cambio de 5000usd a pesos es:", calculo)
