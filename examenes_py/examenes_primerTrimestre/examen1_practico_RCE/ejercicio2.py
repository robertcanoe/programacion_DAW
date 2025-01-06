"""
Desarrolla un programa en Python que simule un juego de dados contra el ordenador, donde se
acumulen puntos basados en el resultado de los lanzamientos.

Autor: Roberto Cano Estévez
Fecha: 12/11/2024
"""

import random

print("Este programa simula un juego de dados contra el ordenador")
print("----------------------------------------------------------")

# Variables para conteo de resultados
user_points = 0
computer_points = 0
rounds_played = 0

game_active = True

while game_active:
    # Lanzamiento de dados
    input("Presiona Intro para lanzar tu dado: ")
    user_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)

    print(f"\nDado del ordenador: {computer_roll}")
    print(f"Tu dado: {user_roll}")

    # Determinar el ganador de la ronda
    if user_roll > computer_roll:
        print("\n¡Ganaste la ronda!")
        user_points += user_roll
    elif user_roll < computer_roll:
        print("\nEl ordenador gana la ronda.")
        computer_points += computer_roll
    else:
        print("\n¡EMPATE!")

    rounds_played += 1

    # Mostrar los puntos acumulados
    print(f"\nPuntos acumulados por ti: {user_points}")
    print(f"Puntos acumulados por el ordenador: {computer_points}")

    # Preguntar si el usuario quiere seguir jugando
    continue_game = input("\n¿Quieres lanzar de nuevo? (sí/no): ").strip().lower()
    if continue_game != "sí":
        game_active = False
        print("\nFin del juego.")
        if user_points > computer_points:
            print(f"¡Ganaste el juego con {user_points} puntos frente a {computer_points} del ordenador!")
        elif user_points < computer_points:
            print(f"El ordenador ganó el juego con {computer_points} puntos frente a tus {user_points} puntos.")
        else:
            print("El juego terminó en empate.")
