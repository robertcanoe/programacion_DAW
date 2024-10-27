"""
Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente),
saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia ni la función.

Autor: Roberto Cano Estévez

Fecha: 26/10/2024
"""

print("Este programa calcula la potencia de un número real elevado a un exponente entero positivo sin usar el operador de potencia.")
print("----------------------------------------------------------------")

base = float(input("Introduce la base (número real): "))
exponent = int(input("Introduce el exponente (entero positivo): "))

result = 1
for _ in range(exponent):
    result *= base

print(f"El resultado de {base} elevado a {exponent} es: {result}")
