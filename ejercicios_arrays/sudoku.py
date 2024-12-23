import random

def crear_tablero():
    return [[0 for _ in range(9)] for _ in range(9)]

def es_valido(tablero, num, pos):
    # Verificar fila
    for i in range(9):
        if tablero[pos[0]][i] == num and pos[1] != i:
            return False

    # Verificar columna
    for i in range(9):
        if tablero[i][pos[1]] == num and pos[0] != i:
            return False

    # Verificar caja de 3x3
    caja_x = pos[1] // 3
    caja_y = pos[0] // 3
    for i in range(caja_y * 3, caja_y * 3 + 3):
        for j in range(caja_x * 3, caja_x * 3 + 3):
            if tablero[i][j] == num and (i, j) != pos:
                return False
    return True

def resolver_sudoku(tablero):
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                for num in range(1, 10):
                    if es_valido(tablero, num, (i, j)):
                        tablero[i][j] = num
                        if resolver_sudoku(tablero):
                            return True
                        tablero[i][j] = 0
                return False
    return True

def generar_sudoku():
    tablero = crear_tablero()
    resolver_sudoku(tablero)
    # Borrar algunos números para hacer el puzzle
    for i in range(40):  # Ajusta este número para cambiar la dificultad
        fila = random.randint(0, 8)
        col = random.randint(0, 8)
        tablero[fila][col] = 0
    return tablero

def imprimir_sudoku(tablero):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(tablero[i][j] if tablero[i][j] != 0 else " ", end="\n")
            else:
                print(str(tablero[i][j] if tablero[i][j] != 0 else " "), end=" ")

# Generar e imprimir un Sudoku
sudoku = generar_sudoku()
imprimir_sudoku(sudoku)

