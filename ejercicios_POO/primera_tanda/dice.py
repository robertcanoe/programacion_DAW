"""
1. Crea una clase "Dado" que simule el funcionamiento de un dado con caras del 1 al 6 que tienen la misma probabilidad de salir y un programa de prueba.
"""

import random

class Dice:
    
    def __init__(self):
        self.__face = random.randint(1, 6)

    def roll(self):
        self._face = random.randint(1, 6)

    @property
    def get_face(self):
        return self.__face
    
    @get_face.setter
    def set_face(self, value):
        if value < 1 or value > 6:
            raise ValueError("The value must be between 1 and 6")
        self.__face = value

    def __str__(self):
        return f"Dice shows {self.__face}"