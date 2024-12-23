"""
Realiza un programa que rellene un array de 6 filas por 10 columnas con números enteros positivos comprendidos entre 0 y 1000 (ambos incluidos).
A continuación, el programa deberá dar la posición tanto del máximo como del mínimo.
Autor: Roberto Cano Estévez

Fecha: 05/12/2024
"""
import random

ROWS = 6
COLUMNS = 10
matrix = [[random.randint(0, 1000) for _ in range(COLUMNS)] for _ in range(ROWS)]

print("Programa que encuentra el número máximo y mínimo en una matriz de 6x10.")
print("-----------------------------------------------------------------------")

print("Matrix generada:")
for row in matrix:
    print(row)

max_numbers = 0
min_numbers = 1000
position_max = (0, 0)
position_min = (0, 0)

for i in range(ROWS):
    for j in range(COLUMNS):
        if matrix[i][j] > max_numbers:
            max_numbers = matrix[i][j]
            position_max = (i, j)
        if matrix[i][j] < min_numbers:
            min_numbers = matrix[i][j]
            position_min = (i, j)

print(f"\nEl número máximo es {max_numbers} y esta en la posición {position_max}")
print(f"\nEl número mínimo es {min_numbers} y esta en la posición {position_min}")
