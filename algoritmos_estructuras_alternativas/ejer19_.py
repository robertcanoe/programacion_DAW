"""
Escribe un programa que pida un número entero entre uno y doce
e imprima el número de días que tiene el mes correspondiente.

Autor: Roberto Cano Estévez
Fecha: 19/10/2024
"""
print("Este programa solicita un número y muestra la cantidad de días del mes correspondiente.")
print("---------------------------------------------------------------------------------------")

month = int(input("Introduce un número entre 1 y 12 para indicar el mes: "))

if month in [1, 3, 5, 7, 8, 10, 12]:
    print("Este mes tiene 31 días.")
elif month in [4, 6, 9, 11]:
    print("Este mes tiene 30 días.")
elif month == 2:
    print("Este mes tiene 28 o 29 días, dependiendo de si es año bisiesto.")
else:
    print("Error: Número no válido, introduce un número entre 1 y 12.")






month = int(input("Introduce un número entre 1 y 12 para indicar el mes: "))

if month in [1, 3, 5, 7, 8, 10, 12]:
    print("Este mes tiene 31 días.")
elif month in [4, 6, 9, 11]:
    print("Este mes tiene 30 días.")
elif month == 2:
    print("Este mes tiene 28 o 29 días, dependiendo de si es año bisiesto.")
else:
    print("Error: Número no válido, introduce un número entre 1 y 12.")
