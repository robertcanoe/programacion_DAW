"""
Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cinco opciones:
sumar, restar, multiplicar, dividir y terminar. Cada opción llama a una función a la que se le
pasan las dos variables y muestra el resultado de la operación. Si se introduce una opción incorrecta
se muestra un mensaje de error. El menú se volverá a mostrar, a menos que no se dé a la opción terminar.

Autor: Roberto Cano Estévez
Fecha: 27/11/2024
"""

from utils_float import request_float
from utils_int import request_int


def main():

    while True:
        value_a = request_float("Ingresa el valor de a: ")
        if value_a < 0:
            print("El valor de a no puede ser negativo")

        value_b = request_float("Ingresa el valor de b: ")
        if value_b < 0:
            print("El valor de b no puede ser negativo")

    while True:
        selection = menu()

def menu():

    print("\nA continuación se muestra un menú con cinco opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Terminar")

    options = request_int("Introduce una opción entre las 5: ")
    if options < 1 or options > 5:
        raise ValueError("Introduce una opción entre 1 y 5")
    return options

def operations(option, a, b):
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








