"""
Crea una biblioteca de funciones numéricas que contenga las siguientes funciones. Recuerda que puedes usar unas dentro de otras si es necesario.

Observa bien lo que hace cada función, ya que, si las implementas en el orden adecuado, te puedes ahorrar mucho trabajo. Por ejemplo, la función es_capicúa() resulta trivial teniendo voltea() y la función siguiente_primo() también es muy fácil de implementar teniendo es_primo().

Prohibido usar funciones de conversión del número a una cadena.

- es_capicúa: devuelve verdadero si el número que se pasa como parámetro es capicúa y falso en caso contrario.
- es_primo: devuelve verdadero si el número que se pasa como parámetro es primo y falso en caso contrario.
- siguiente_primo: devuelve el menor primo que es mayor al número que se pasa como parámetro.
- dígitos: devuelve el número de dígitos de un número entero.
- voltea: le da la vuelta a un número.
- digito_n: devuelve el dígito que está en la posición n de un número entero. Se empieza contando por el 0 y de izquierda a derecha.
- posición_de_digito: da la posición de la primera ocurrencia de un dígito dentro de un número entero. Si no se encuentra, devuelve -1.
- quita_por_detrás: le quita a un número "n" dígitos por detrás (por la derecha).
- quita_por_delante: le quita a un número "n" dígitos por delante (por la izquierda).
- pega_por_detrás: añade un dígito a un número por detrás.
- pega_por_delante: añade un dígito a un número por delante.
- trozoDeNumero: toma como parámetros las posiciones inicial y final dentro de un número y devuelve el trozo correspondiente.
- juntaNúmeros: pega dos números para formar uno.

Haz el programa de manera que al ejecutarse pruebe cada una de las funciones.

Autor: Roberto Cano Estévez

Fecha: xx/xx/xx
"""

def is_palindrome(num):
    # Implementation of the is_palindrome function
    pass

def is_prime(num):
    if num == 0 or num == 2:
        print("El número es primo")
    elif num % 2 == 0:
        print("El número no es primo")

def next_prime(num):
    # Implementation of the next_prime function
    pass

def digits(num):
    # Implementation of the digits function
    pass

def reverse(num):
    # Implementation of the reverse function
    pass

def digit_at(num, n):
    # Implementation of the digit_at function
    pass

def digit_position(num, digit):
    # Implementation of the digit_position function
    pass

def remove_from_back(num, n):
    # Implementation of the remove_from_back function
    pass

def remove_from_front(num, n):
    # Implementation of the remove_from_front function
    pass

def append_to_back(num, digit):
    # Implementation of the append_to_back function
    pass

def append_to_front(num, digit):
    # Implementation of the append_to_front function
    pass

def slice_number(num, start, end):
    # Implementation of the slice_number function
    pass

def join_numbers(num1, num2):
    # Implementation of the join_numbers function
    pass

def main():
    options = {
        1: is_palindrome,
        2: is_prime,
        3: next_prime,
        4: digits,
        5: reverse,
        6: digit_at,
        7: digit_position,
        8: remove_from_back,
        9: remove_from_front,
        10: append_to_back,
        11: append_to_front,
        12: slice_number,
        13: join_numbers,
    }

    while True:
        print("\n--------------------------Menú--------------------------")
        print("1. Hacer capicúa una cadena, ya sea números o letras.")
        print("2. Dice si un número es primo.")
        print("3. Devuelve el siguiente número primo.")
        print("4. Devuelve el número de dígitos de un número entero.")
        print("5. Da la vuelta a un número.")
        print("6. Devuelve el dígito que está en la posición n de un número entero.")
        print("7. Da la posición de la primera ocurrencia de un dígito dentro de un número entero.")
        print("8. Quita a un número 'n' dígitos por detrás.")
        print("9. Quita a un número 'n' dígitos por delante.")
        print("10. Añade un dígito a un número por detrás.")
        print("11. Añade un dígito a un número por delante.")
        print("12. Toma como parámetros las posiciones inicial y final dentro de un número y devuelve el trozo correspondiente.")
        print("13. Pega dos números para formar uno.")
        print("0. Salir.")
        option = int(input("Introduce una opción: "))

        if option == 0:
            break
        elif option in options:
            if option in [1, 2, 3, 4, 5]:
                num = int(input("Introduce un número: "))
                print(options[option](num))
            elif option == 6:
                num = int(input("Introduce un número: "))
                n = int(input("Introduce la posición: "))
                print(options[option](num, n))
            elif option == 7:
                num = int(input("Introduce un número: "))
                digit = int(input("Introduce el dígito: "))
                print(options[option](num, digit))
            elif option in [8, 9]:
                num = int(input("Introduce un número: "))
                n = int(input("Introduce la cantidad de dígitos: "))
                print(options[option](num, n))
            elif option in [10, 11]:
                num = int(input("Introduce un número: "))
                digit = int(input("Introduce el dígito: "))
                print(options[option](num, digit))
            elif option == 12:
                num = int(input("Introduce un número: "))
                start = int(input("Introduce la posición inicial: "))
                end = int(input("Introduce la posición final: "))
                print(options[option](num, start, end))
            elif option == 13:
                num1 = int(input("Introduce el primer número: "))
                num2 = int(input("Introduce el segundo número: "))
                print(options[option](num1, num2))
        else:
            print("Opción no válida, por favor elige una opción del menú (0-13).")

if __name__ == "__main__":
    main()