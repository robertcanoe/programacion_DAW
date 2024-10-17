"""
Escribe un programa que lea un número e indique si es par o impar.

Autor: Roberto Cano Estévez

Fecha: 16/10/2024
"""
print("En este programa das un número y te dice si es par o impar")
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")

n1 = int(input("Dime un número: "))
if n1 % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")