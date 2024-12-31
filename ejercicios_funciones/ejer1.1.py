"""
Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cinco opciones:
sumar, restar, multiplicar, dividir y terminar. Cada opción llama a una función a la que se le
pasan las dos variables y muestra el resultado de la operación. Si se introduce una opción incorrecta
se muestra un mensaje de error. El menú se volverá a mostrar, a menos que no se dé a la opción terminar.

Autor: Roberto Cano Estévez
Fecha: 27/11/2024
"""

def main():

    while True:
        try:
            value1 = float(input("Ingrese el primer valor (a): "))
            if value1 < 0:
                raise ValueError("El valor no puede ser negativo.")

            value2 = float(input("Ingrese el segundo valor (b): "))
            if value2 < 0:
                raise ValueError("El valor no puede ser negativo.")

            break
        except ValueError as error:
            print(f"Error: {error}. Por favor, ingresa un número válido (flotante o entero) y no negativo.")

    while True:
        selection = menu()

        if selection is None:
            continue
        elif selection == 5:
            print("El programa ha terminado.")
            break
        operaciones(selection, value1, value2)


def menu():

    print("\nA continuación se muestra un menú con cinco opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Terminar")

    try:
        options = int(input("Elige una opción (1-5): "))
        if options < 1 or options > 5:
            raise ValueError("Opción fuera del rango permitido.")
        return options
    except ValueError as e:
        print(f"Error: {e}. Por favor, elige una opción entre 1 y 5.")
        return None


def operaciones(option, a, b):

    try:
        if option == 1:
            print(f"La suma entre {a} y {b} es: {a + b}")
        elif option == 2:
            print(f"La resta entre {a} y {b} es: {a - b}")
        elif option == 3:
            print(f"La multiplicación entre {a} y {b} es: {a * b}")
        elif option == 4:
            if b == 0:
                raise ZeroDivisionError("No se puede dividir entre cero.")
            print(f"La división entre {a} y {b} es: {a / b}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
