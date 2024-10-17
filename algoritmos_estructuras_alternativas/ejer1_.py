"""
Programa que pida dos números e indique si el primero es mayor que el segundo o no.

Autor: Roberto Cano Estévez

Fecha: 16/10/2024
"""

print("En este programa vas a dar dos números y te va a decir si el primero es mayor que el segundo o no.")
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")

n1 = int(input("Dime el primer numero: "))
n2 = int(input("Dime el segundo numero: "))

if n1 > n2:
    print("El número primero es mayor que el segundo")
if n1 < n2:
    print("El segundo número es mayor que el primero")
if n1 == n2:
    print("Los dos números son iguales")

