"""
Haz un programa que utilice una matriz de 3x3 y ofrezca un menú con las siguientes opciones:
1. Rellenar la matriz con números aleatorios entre 1 y 100.
•Llama a la función fill() que recibe como parámetros 1 y 100.
    ◦fill(1, 100)

2. Rellenar la matriz con números aleatorios entre 1 y 100 sin que se repitan.
•Puedes reutilizar la función anterior de forma que reciba un tercer parámetro con un valor por 
defecto igual a True que indique si los números se pueden repetir.
    ◦fill(1,100, False)
3. Desplazar todos los números una posición hacia la derecha.
•Llama a la función shift_right() sin parámetros.
•Ejemplo:

1 2 3   3 1 2
4 5 6 → 6 4 5
7 8 9   9 7 8



5. Desplazar todos los números una posición hacia abajo.
•Llama a la función shift_down() sin parámetros.
•Ejemplo:

1 2 3   7 8 9
4 5 6 → 1 2 3
7 8 9   4 5 6

6. Calcular la suma de los elementos de una fila.
•Llama a la función show_sum_row() sin parámetros:
    ◦Pide una fila y controla que esté entre 1 y 3. Si no es así muestra un mensaje de error.
    ◦Llama a la función sum_row() pasándole como parámetro la fila anterior, esta función 
    devuelve la suma.
    ◦Muestra la suma.

7. Modificar un elemento de la matriz.
•Llama a la función update_element() sin parámetros:
    ◦Pide una fila y una columna, controla que estén entre 1 y 3. Si no es así muestra un mensaje de
    error.
    ◦Muestra el contenido de esa posición y pregunta si de verdad quiere cambiarlo, controla que 
    conteste Sí o No.
    ◦Si contesta que Sí lo cambias, no hagas nada en caso contrario.

8. Mostrar la matriz.

•Llama a la función show() sin parámetros:
    ◦Muestra la matriz con los números alineados.
    ◦Así estaría bien:

 
 10 100   9
100  85 100
  7   4  26 
    ◦Así estaría mal:

10 100 9
100 85 100
7 4 26 

9. Salir del programa.

La matriz tiene que ser una variable global, llámala matrix. Créala, antes de mostrar el menú, rellena de
ceros.
Cada opción del menú, excepto la de salir, llama a una función. Si no sabes hacerlo con funciones, hazlo 
sin ellas, pero se penalizará con 2 puntos.
Si la opción 1 o 2 del menú no se han ejecutado, las demás (salvo la de salir) no funcionan y debes 
mostrar que hasta que alguna de esas opciones no se ejecute, no funcionará.
Controla que las opciones del menú introducidas por el usuario son correctas.
Para operar con la matriz NO se pueden usar slices. 

------------------------------------------------------------------------------------------------------
Autor: Roberto Cano Estévez
Fecha: 16/12/2024
"""
import random

from utils_int import request_int
from utils_print import request_print

matrix = [[0] * 3 for _ in range(3)]
initialized = False

def fill(start, end, allow_repeats=True):
    # Llena la matriz con números aleatorios.
    global matrix
    if allow_repeats:
        for i in range(3):
            for j in range(3):
                matrix[i][j] = random.randint(start, end)
    else:
        numbers = list(range(start, end + 1))
        random.shuffle(numbers)
        index = 0
        for i in range(3):
            for j in range(3):
                matrix[i][j] = numbers[index]
                index += 1

def shift_right():
    # Desplaza la matriz hacia la derecha.
    global matrix
    for i in range(3):
        last = matrix[i][2]
        for j in range(2, 0, -1):
            matrix[i][j] = matrix[i][j - 1]
        matrix[i][0] = last

def shift_down():
    # Desplaza la matriz hacia abajo.
    global matrix
    last_row = [matrix[2][j] for j in range(3)]
    for i in range(2, 0, -1):
        for j in range(3):
            matrix[i][j] = matrix[i - 1][j]
    for j in range(3):
        matrix[0][j] = last_row[j]

def show_sum_rows():
    # Muestra la suma de los elementos de una fila específica.
    while True:
        row = request_int("Introduce el número de la fila (1-3): ") - 1
        if 0 <= row < 3:
            total = sum(matrix[row])
            print("\nLa suma de la fila es:", total)
            break
        else:
            print("Error: El número de la fila debe estar entre 1 y 3.")

def update_element():
    # Modifica un elemento específico de la matriz.
    while True:
        row = request_int("Introduce el número de la fila (1-3): ") - 1
        col = request_int("Introduce el número de la columna (1-3): ") - 1
        if 0 <= row < 3 and 0 <= col < 3:
            print(f"\nEl valor actual es: {matrix[row][col]}")
            confirm = input("¿Quieres cambiarlo? [y/n]: ").strip().lower()
            if confirm == 'y':
                new_value = request_int("Introduce un nuevo valor: ")
                matrix[row][col] = new_value
            break
        else:
            print("Error: La fila y columna deben estar entre 1 y 3.")

def show():
    # Muestra la matriz con un formato mejorado.
    max_width = max(len(str(num)) for row in matrix for num in row)  # Obtiene el ancho del número más grande.
    cell_width = max_width + 2  # Agrega espacio adicional para una mejor visualización.
    
    horizontal_line = f"╔{'╦'.join(['═' * cell_width] * 3)}╗"
    middle_line = f"╠{'╬'.join(['═' * cell_width] * 3)}╣"
    bottom_line = f"╚{'╩'.join(['═' * cell_width] * 3)}╝"

    print("\nMatriz actual:")
    print(horizontal_line)
    for i, row in enumerate(matrix):
        print("║" + "║".join(f"{str(num).center(cell_width)}" for num in row) + "║")
        if i < 2:
            print(middle_line)
    print(bottom_line)


def main():
    # Función principal que ofrece un menú para interactuar con la matriz.
    global initialized

    while True:
        print("\n╔═══════════════════════════════════════════════════════════╗")
        print("║                           Menú                            ║")
        print("╠═══════════════════════════════════════════════════════════╣")
        print("║1. Rellenar la matriz con números aleatorios entre 1 y 100.║")
        print("║2. Rellenar la matriz con números únicos entre 1 y 100.    ║")
        print("║3. Desplazar a la derecha.                                 ║")
        print("║4. Desplazar hacia abajo.                                  ║")
        print("║5. Calcular suma de una fila.                              ║")
        print("║6. Modificar un elemento.                                  ║")
        print("║7. Mostrar la matriz.                                      ║")
        print("║8. Salir.                                                  ║")
        print("╚═══════════════════════════════════════════════════════════╝")

        option = input("Elige una opción: ").strip()

        match option:
            case "1":
                fill(1, 100)
                initialized = True
                print("\nMatriz rellenada con números aleatorios.")
            case "2":
                fill(1, 100, False)
                initialized = True
                print("\nMatriz rellenada con números únicos.")
            case "3":
                if initialized:
                    shift_right()
                    print("\nMatriz desplazada a la derecha.")
                else:
                    request_print()
            case "4":
                if initialized:
                    shift_down()
                    print("\nMatriz desplazada hacia abajo.")
                else:
                    request_print()
            case "5":
                if initialized:
                    show_sum_rows()
                else:
                    request_print()
            case "6":
                if initialized:
                    update_element()
                else:
                    request_print()
            case "7":
                show()
            case "8":
                print("\nSaliendo...")
                break
            case _:
                print("\nOpción no válida. Por favor, elige una opción entre 1 y 8.")

if __name__ == "__main__":
    main()
