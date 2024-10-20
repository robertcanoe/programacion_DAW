"""
Escribir un programa que lea un año indicar si es bisiesto.

Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.

Autor: Roberto Cano Estévez

Fecha: 19/10/2024
"""

number = 400

if number % 4 == 0:
    if number % 100 == 0:
        if number % 400 == 0:
            result = f"{number} es divisible por 4, 100 y 400"
        else:
            result = f"{number} es divisible por 4 y 100"
    else:
        result = f"{number} es divisible por 4"
else:
    result = f"{number} no es divisible por 4"

print(result)

