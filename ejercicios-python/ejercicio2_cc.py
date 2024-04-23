"""lol"""

importe = int(input("Ingrese el importe:"))
forma_pago = int(input("Metodo de pago: 1- Contado, 2- Tarjeta, 3- Debito:"))


if forma_pago == 1:
    descuento = importe * 10 / 100
    calculo = importe - descuento
    print("Total a pagar:", calculo)
if forma_pago == 2:
    interes = importe * 10 / 100
    calculo = importe + interes
    print("Total a pagar:", calculo)
if forma_pago == 3:
    descuento = importe * 5 / 100
    calculo = importe - descuento
    print("Total a pagar:", calculo)
