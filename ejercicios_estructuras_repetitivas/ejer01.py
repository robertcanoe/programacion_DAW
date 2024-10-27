"""

Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100.
A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el
introducido, además de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa
termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), si se
llega al límite de intentos te muestra el número que había generado.

Autor: Roberto Cano Estévez

Fecha: 26/10/2024
"""
import random

print("¡Bienvenido al juego de adivinanza!")
print("----------------------------------------------------------------")

target_number = random.randint(1, 100)
remaining_attempts = 10
guess_correct = False

while remaining_attempts > 0 and not guess_correct:
    print(f"Tienes {remaining_attempts} intentos restantes.")
    user_guess = int(input("Introduce un número entre 1 y 100: "))

    if user_guess == target_number:
        print(f"¡Felicidades! Has adivinado el número en {10 - remaining_attempts + 1} intentos.")
        guess_correct = True
    elif user_guess < target_number:
        print("El número a adivinar es mayor.")
    else:
        print("El número a adivinar es menor.")

    remaining_attempts -= 1

if not guess_correct:
    print(f"Lo siento, te has quedado sin intentos. El número era {target_number}.")
