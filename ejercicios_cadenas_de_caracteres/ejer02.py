"""
Crea un programa que verifique si una cadena ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda, ignorando espacios, signos de puntuación y mayúsculas).

Author: Roberto Cano Estévez
Date: 6/11/2024
"""
try:
    print("This program checks a string and tells the user if it is a palindrome or not.")
    print("-----------------------------------------------------------------------------")

    text = input("Enter a string: ")

    text = text.lower()

    processed_text = ''.join(char for char in text if char.isalnum())

    is_palindrome = processed_text == processed_text[::-1]

    if is_palindrome:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

except ValueError:
    print("Invalid input: Please enter a valid string.")
