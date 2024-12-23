"""
Modifica el programa anterior de tal forma que no se repita ningún número en el array.

Autor: Roberto Cano Estévez

Fecha: 08/12/2024
"""
import random

ROWS = 6
COLUMNS = 10
TOTAL_NUMBERS = ROWS * COLUMNS

unique_number = random.sample(range(1000), TOTAL_NUMBERS)
matrix = [unique_number[i * COLUMNS:(i + 1) * COLUMNS] for i in range(ROWS)]

print("Programa que encuentra el número máximo y mínimo en una matriz de 6x10 (pero sin que ningún número se repita).")
print("--------------------------------------------------------------------------------------------------------------")

print("Matrix generada:")
for row in matrix:
    print(row)

max_number = 0
min_number = 1000
position_max = (0, 0)
position_min = (0, 0)

for i in range(ROWS):
    for j in range(COLUMNS):
        if matrix[i][j] > max_number:
            max_number = matrix[i][j]
            position_max = (i, j)
        if matrix[i][j] < min_number:
            min_number = matrix[i][j]
            position_min = (i, j)

print(f"\nEl número máximo es {max_number} y está en la posición {position_max}")
print(f"\nEl número mínimo es {min_number} y está en la posición {position_min}")