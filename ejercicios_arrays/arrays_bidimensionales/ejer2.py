"""
Escribe un programa que pida 20 números enteros. Estos números se deben introducir en un array de 4 filas por 5 columnas. El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo se tratará. La suma total debe aparecer en la esquina inferior derecha.

Autor: Roberto Cano Estévez

Fecha: 3/12/2024
"""
from random import randint

from utils_int import request_int

print("En este programa introduces 20 números enteros, el programa sumará las filas y columnas al igual que una hoja de cálculo")
print("------------------------------------------------------------------------------------------------------------------------")

ROWS = 4
COLS = 5

matrix = []

for i in range(ROWS):
    row = []
    for j in range(COLS):
        number = randint(100, 999)
        row.append(number)
    matrix.append(row)

print("\nMatriz ingresada:")
for row in matrix:
    print(row)

print("\nSumas por fila:")
for row in matrix:
    row_sum = 0
    for number in row:
        row_sum += number
    print(row_sum, end="\t")
print()

print("\nSumas por columna:")
for i in range(COLS):
    col_sum = 0
    for j in range(ROWS):
        col_sum += matrix[j][i]
    print(col_sum, end="\t")
print()

total_sum = 0
for row in matrix:
    for number in row:
        total_sum += number
print("\nSuma total:", total_sum)

