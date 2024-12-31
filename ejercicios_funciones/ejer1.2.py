"""
Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con seis opciones:
ingresar valores, sumar, restar, multiplicar, dividir y terminar. Cada opción llama a una función
a la que se le pasan las dos variables y muestra el resultado de la operación. Si se introduce una opción
incorrecta se muestra un mensaje de error. El menú se volverá a mostrar, a menos que no se dé a la opción terminar.

Autor: Roberto Cano Estévez

Fecha: 27/11/2024
"""

def main():
    a, b = 0, 0

    while True:
        user_option = menu()

        if user_option is None:
            continue

        elif user_option == 1:
            a, b = ingresar_valores()

        elif user_option == 6:
            print("El programa ha terminado.")
            break

        elif a == 0 and b == 0:
            print("Primero debes ingresar los valores de a y b antes de realizar operaciones.")

        else:
            operaciones(user_option, a, b)


def menu():
    print("\nA continuación se muestra un menú con seis opciones:")
    print("1. Ingresar los valores de a y b")
    print("2. Sumar")
    print("3. Restar")
    print("4. Multiplicar")
    print("5. Dividir")
    print("6. Terminar")

    try:
        user_inputs = int(input("Elige una opción (1-6): "))

        if user_inputs < 1 or user_inputs > 6:
            raise ValueError("Opción fuera del rango permitido.")

        return user_inputs

    except ValueError as e:
        print(f"Error: {e}. Por favor, elige una opción entre 1 y 6.")
        return None


def operaciones(option, num1, num2):
    try:
        if option == 2:
            print(f"La suma entre {num1} y {num2} es: {num1 + num2}")

        elif option == 3:
            print(f"La resta entre {num1} y {num2} es: {num1 - num2}")

        elif option == 4:
            print(f"La multiplicación entre {num1} y {num2} es: {num1 * num2}")

        elif option == 5:
            if num2 == 0:
                raise ZeroDivisionError("No se puede dividir entre cero.")
            print(f"La división entre {num1} y {num2} es: {num1 / num2}")

    except ZeroDivisionError as e:
        print(f"Error: {e}")


def ingresar_valores():
    while True:
        try:
            valor1 = float(input("Ingresa el valor de a: "))

            if valor1 < 0:
                raise ValueError("El valor no puede ser negativo.")

            valor2 = float(input("Ingresa el valor de b: "))

            if valor2 < 0:
                raise ValueError("El valor no puede ser negativo.")

            return valor1, valor2

        except ValueError as error:
            print(f"Error: {error}. Por favor, ingresa números válidos y no negativos.")


if __name__ == "__main__":
    main()
