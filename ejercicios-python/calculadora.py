"""lalalala"""

# Módulo de Operaciones Matemáticas


def suma(a, b):
    """Realiza la suma de dos números."""
    return a + b


def resta(a, b):
    """Realiza la resta de dos números."""
    return a - b


def multiplicacion(a, b):
    """Realiza la multiplicación de dos números."""
    return a * b


def division(a, b):
    """Realiza la división de dos números (evita la división por
cero)."""
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre cero"
