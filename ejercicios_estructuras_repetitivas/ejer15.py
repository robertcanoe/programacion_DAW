"""
Introducir una cadena de caracteres e indicar si es un palíndromo.
Una palabra palíndroma es aquella que se lee igual adelante que atrás.

Autor: Roberto Cano Estévez

Fecha: 26/10/2024
"""

print("Este programa verifica si una cadena es un palíndromo.")
print("----------------------------------------------------------------")

text = input("Introduce una cadena: ").replace(" ", "").lower()
if text == text[::-1]:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
