def crear_matriz(filas, columnas):
    """Crea una matriz de tamaño filas x columnas pidiendo sus valores al usuario."""
    matriz = []
    print("Introduce los valores de la matriz:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            print("Elemento [", i, "][", j, "]: ", end="")
            valor = int(input())  # Pedimos un valor numérico
            fila.append(valor)
        matriz.append(fila)
    return matriz


def mostrar_matriz(matriz):
    """Muestra la matriz en formato de filas y columnas."""
    if len(matriz) == 0:
        print("La matriz está vacía. Crea una primero.")
        return
    print("Matriz:")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")  # Imprimimos cada valor de la fila con un espacio
        print()  # Salto de línea después de cada fila


def sumar_filas(matriz):
    """Calcula y muestra la suma de los elementos de cada fila sin usar sum()."""
    if len(matriz) == 0:
        print("La matriz está vacía. Crea una primero.")
        return
    for i in range(len(matriz)):  # Iteramos sobre las filas
        suma_fila = 0
        for j in range(len(matriz[i])):  # Iteramos sobre los elementos de la fila
            suma_fila = suma_fila + matriz[i][j]  # Sumamos los elementos
        print("Suma de la fila", i, ":", suma_fila)


def sumar_columnas(matriz):
    """Calcula y muestra la suma de los elementos de cada columna sin usar sum()."""
    if len(matriz) == 0:
        print("La matriz está vacía. Crea una primero.")
        return
    columnas = len(matriz[0])  # Número de columnas
    for j in range(columnas):  # Iteramos por cada columna
        suma_columna = 0
        for i in range(len(matriz)):  # Sumamos los elementos de cada fila en la columna actual
            suma_columna = suma_columna + matriz[i][j]
        print("Suma de la columna", j, ":", suma_columna)


def transponer_matriz(matriz):
    """Devuelve la matriz transpuesta usando bucles simples."""
    if len(matriz) == 0:
        print("La matriz está vacía. Crea una primero.")
        return []
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = []
    for j in range(columnas):  # Por cada columna de la matriz original
        nueva_fila = []
        for i in range(filas):  # Por cada fila de la matriz original
            nueva_fila.append(matriz[i][j])  # Los elementos se convierten en las filas de la transpuesta
        transpuesta.append(nueva_fila)
    return transpuesta


def menu():
    """Muestra el menú principal y permite al usuario interactuar con la matriz."""
    matriz = []  # La matriz comienza vacía
    while True:
        print("\nMenú:")
        print("1. Crear matriz")
        print("2. Mostrar matriz")
        print("3. Sumar filas")
        print("4. Sumar columnas")
        print("5. Transponer matriz")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            filas = int(input("Número de filas: "))
            columnas = int(input("Número de columnas: "))
            matriz = crear_matriz(filas, columnas)
        elif opcion == "2":
            mostrar_matriz(matriz)
        elif opcion == "3":
            sumar_filas(matriz)
        elif opcion == "4":
            sumar_columnas(matriz)
        elif opcion == "5":
            transpuesta = transponer_matriz(matriz)
            if len(transpuesta) > 0:  # Si la transposición fue exitosa
                print("Matriz transpuesta:")
                mostrar_matriz(transpuesta)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecuta el programa
if __name__ == "__main__":
    menu()
