"""
Desarrolla un programa en Python que simule el juego clásico "Piedra, papel o tijera" contra el
ordenador.

Autor: Roberto Cano Estévez
Fecha: 12/11/2024
"""

import random

print("Este programa simula el clásico juego: Piedra, Papel y Tijera")
print("-------------------------------------------------------------")

# Variables para conteo de resultados
rounds_played = 0
rounds_won = 0
rounds_lost = 0
rounds_tied = 0

game_active = True

while game_active:
    # Elección del ordenador
    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        computer_choice = "piedra"
    elif computer_choice == 2:
        computer_choice = "papel"
    else:
        computer_choice = "tijera"

    # Elección del jugador
    user_choice = input("¿Piedra, papel o tijera? ").strip().lower()

    if user_choice not in ["piedra", "papel", "tijera"]:
        print("Opción inválida. Por favor, elige entre piedra, papel o tijera.")
        continue

    # Mostrar elección del ordenador
    print(f"\nEl ordenador eligió: {computer_choice}")

    # Determinar el resultado
    if user_choice == computer_choice:
        print("¡Empate!")
        rounds_tied += 1
    elif (user_choice == "piedra" and computer_choice == "tijera") or \
         (user_choice == "papel" and computer_choice == "piedra") or \
         (user_choice == "tijera" and computer_choice == "papel"):
        print("¡Ganaste esta ronda!")
        rounds_won += 1
    else:
        print("Perdiste esta ronda.")
        rounds_lost += 1

    rounds_played += 1

    # Preguntar si el usuario quiere seguir jugando
    continue_game = input("\n¿Quieres jugar otra vez? (sí/no): ").strip().lower()
    if continue_game != "sí":
        game_active = False
        print("\nFin del juego.")
        print(f"Has jugado {rounds_played} rondas: {rounds_won} ganadas, {rounds_lost} perdidas, {rounds_tied} empates.")
