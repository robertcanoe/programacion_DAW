"""
Escribe un programa que genere 20 números enteros aleatorios entre 0 y 100 y que los almacene en un array. El programa debe ser capaz de pasar todos los números pares a las primeras posiciones del array (del 0 en adelante) y todos los números impares a las celdas restantes. Utiliza arrays auxiliares si es necesario.

Autor: Roberto Cano Estévez

Fecha: 24/11/2024
"""
from random import randint

print("Este programa genera aleatoriamente 20 números comprendidos entre 0 y 100, y el programa divide los números entre pares e impares")
print("---------------------------------------------------------------------------------------------------------------------------------\n")
l = []
l_pair = []
l_odd = []

for i in range(20):
    NUM = randint(0, 100)
    l.append(NUM)

    if NUM % 2 == 0:
        l_pair.append(NUM)
    else:
        l_odd.append(NUM)

l = l_pair + l_odd

print(f"Esta es la lista la cúal tiene a la izquierda los pares y a la derecha los impares: {l}\n")
print(f"Esta es la lista con los pares y los impares divididos en dos listas: \nPares {l_pair}\nImpares {l_odd}")


