"""main"""

import calculadora

if __name__ == '__main__':
    num1 = float(input("ingrese el primer numero"))
    num2 = float(input("Ingresa el segundo número: "))

    print("La suma da: ", calculadora.suma(num1, num2))
    print(f"Resta: {calculadora.resta(num1, num2)}")
    print(f"Multiplicación: {calculadora.multiplicacion(num1, num2)}")
    print(f"División: {calculadora.division(num1, num2)}")
