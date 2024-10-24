"""
Diseña un programa que, dados cinco números enteros, determine cuál de los cuatro últimos números es más cercano al primero. Por ejemplo, si el usuario introduce los números 2, 6, 4, 1 y 10, el programa responderá que el número más cercano al 2 es el 1.

Autor: Roberto Cano Estévez
Fecha: 23/10/2024
"""
print("Este programa responderá con el número más cercano al primero.")
print("--------------------------------------------------------------")

n1 = int(input("Dime el primer numero: "))
n2 = int(input("Dime el segundo numero: "))
n3 = int(input("Dime el tercer numero: "))
n4 = int(input("Dime el quarto numero: "))
n5 = int(input("Dime el quinto numero: "))

difference2 = abs(n1 - n2)
difference3 = abs(n1 - n3)
difference4 = abs(n1 - n4)
difference5 = abs(n1 - n5)

closest_number = n2
if difference3 < difference2:
    closest_number = n3

if difference4 < abs(n1 - closest_number):
    closest_number = n4

if difference5 < abs(n1 - closest_number):
    closest_number = n5

print("El número más cercano a", n1, "es", closest_number)
