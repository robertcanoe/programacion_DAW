"""
Este programa calcula la transpuesta de una matriz dada.
Autor: Roberto Cano Estévez
Fecha: 11/12/2024
"""

# Matriz original
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Mostrar matriz original
print("Matriz original:")
for row in matrix:
    print(row)
print("-" * 20)

# Crear la transpuesta de forma sencilla
transposed = []
for j in range(len(matrix[0])):  # Iterar sobre las columnas
    new_row = []  # Crear una nueva fila
    for i in range(len(matrix)):  # Iterar sobre las filas
        new_row.append(matrix[i][j])  # Agregar el elemento transpuesto
    transposed.append(new_row)  # Agregar la nueva fila a la transpuesta

# Mostrar la matriz transpuesta
print("Matriz transpuesta:")
for row in transposed:
    print(row)
