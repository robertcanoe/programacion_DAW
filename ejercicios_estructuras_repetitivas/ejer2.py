"""
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir).
El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

Autor: Roberto Cano Estévez

Fecha: 26/10/2024
"""

print("Este programa te permite introducir varios números y luego muestra cuántos son positivos, negativos o iguales a cero.")
print("----------------------------------------------------------------")

count_positive = 0
count_negative = 0
count_zero = 0

number_of_inputs = int(input("Introduce la cantidad de números que deseas introducir: "))

for _ in range(number_of_inputs):
    user_number = int(input("Introduce un número: "))

    if user_number > 0:
        count_positive += 1
    elif user_number < 0:
        count_negative += 1
    else:
        count_zero += 1

print(f"Cantidad de números mayores que 0: {count_positive}")
print(f"Cantidad de números menores que 0: {count_negative}")
print(f"Cantidad de números iguales a 0: {count_zero}")
