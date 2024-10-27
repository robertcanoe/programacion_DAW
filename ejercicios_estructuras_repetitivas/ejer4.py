"""
Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

Autor: Roberto Cano Estévez

Fecha: 26/10/2024
"""

print("Este programa muestra todos los números pares entre dos números que introduzcas.")
print("----------------------------------------------------------------")

start_number = int(input("Introduce el primer número: "))
end_number = int(input("Introduce el segundo número: "))

if start_number > end_number:
    start_number, end_number = end_number, start_number

print(f"Números pares entre {start_number} y {end_number}:")

for number in range(start_number, end_number + 1):
    if number % 2 == 0:
        print(number)
