"""
1. Crea una clase "Dado" que simule el funcionamiento de un dado con caras del 1 al 6 que tienen la misma probabilidad de salir y un programa de prueba.
"""

import random

class Dice:
    def __init__(self):
        self.value = random.randint(1, 6)

    def roll(self):
        self.value = random.randint(1, 6)

    def __str__(self):
        return f"Dice shows {self.value}"