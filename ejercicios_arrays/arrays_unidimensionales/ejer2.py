"""
Escribe un programa que lea 10 números por teclado y que luego los muestre en orden inverso, es decir, el primero que se introduce es el último en mostrarse y viceversa.

Autor: Roberto Cano Estévez

Fecha: 22/11/2024
"""
from arrays_bidimensionales.utils_int import request_int

print("Este programa muestra el orden inverso de 1o números, el primero que se introduce es el último en mostrarse y viceversa")
print("-----------------------------------------------------------------------------------------------------------------------")
numbers = []

for i in range(10):
  number = request_int("Introduce un número: ")
  numbers.append(number)

print(f"Este es el orden inverso de los números: {numbers[::-1]}")
