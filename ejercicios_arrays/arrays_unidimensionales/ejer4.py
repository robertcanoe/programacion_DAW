"""
Escribe un programa que pida 10 números por teclado y que luego muestre los números introducidos junto con las palabras “máximo” y “mínimo” al lado del máximo y del mínimo respectivamente.

Autor: Roberto Cano Estévez

Fecha: 22/11/2024
"""
from arrays_bidimensionales.utils_int import request_int

number = []
print("Este programa pide 10 números y luego muestra el máximo y el mínimo")
print("-------------------------------------------------------------------")


for i in range(10):
    values = request_int(f"Ingrese el número {i+1}: ")
    number.append(values)


number_max = max(number)
number_min = min(number)

print("\nLos números introducidos son: ")
for n in number:
    if n == number_max:
        print(f"{n} (máximo)")
    elif n == number_min:
        print(f"{n} (mínimo)")
    else:
        print(n)
