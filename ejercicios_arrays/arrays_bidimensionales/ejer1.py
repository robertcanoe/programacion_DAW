from utils_int import request_int

print("En este programa introduces 20 números enteros, el programa sumará las filas y columnas al igual que una hoja de cálculo")
print("------------------------------------------------------------------------------------------------------------------------")

ROWS = 4
COLS = 5

matrix = []

for i in range(ROWS):
    row = []
    for j in range(COLS):
        number = request_int(f"Ingrese el número para la posición [{i+1}, {j+1}]: ")
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
    print(f"{row_sum:>5}", end="\t")
print()

print("\nSumas por columna:")
for i in range(COLS):
    col_sum = 0
    for j in range(ROWS):
        col_sum += matrix[j][i]
    print(f"{col_sum:>5}", end="\t")
print()

total_sum = 0
for row in matrix:
    for number in row:
        total_sum += number
print(f"\nSuma total: {total_sum}")
