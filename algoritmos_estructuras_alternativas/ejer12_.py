"""
Programa que lee un año e indica si es bisiesto.
Un año es bisiesto si es un número divisible por 4,
pero no si es divisible por 100, excepto que también sea divisible por 400.

Autor: Roberto Cano Estévez
Fecha: 19/10/2024
"""

print("Este programa te pide un año y te dice si es bisiesto.")
print("-----------------------------------------------------")

# Leer el año desde la entrada del usuario
year = int(input("Introduce un año: "))

# Determinar si el año es bisiesto
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            result = f"{year} es bisiesto."
        else:
            result = f"{year} no es bisiesto."
    else:
        result = f"{year} es bisiesto."
else:
    result = f"{year} no es bisiesto."

print(result)

