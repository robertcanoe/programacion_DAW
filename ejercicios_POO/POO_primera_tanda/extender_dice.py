"""
4. Implementar otra clase Dado. Por defecto el dado tendrá 6 caras. Tendremos tres formar de construir un dado (uno al que no se le pasa nada e inicializa el dado al azar, otro al que sólo se le pasa que número tiene el dado en la cara superior y otro con el número del dado en la cara superior y el número de caras del dado). Implementa los getters, el método roll() que tirará el dado al azar y el __str__(). Implementa un tester que tenga un vector de 4 dados y los lance una serie de veces.
"""
import random

class ExtendedDice:
    def __init__(self, top_face=None, num_faces=6):
        self.num_faces = num_faces
        self.value = top_face if top_face is not None else random.randint(1, num_faces)

    @property
    def top_face(self):
        return self.value

    @top_face.setter
    def top_face(self, value):
        if 1 <= value <= self.num_faces:
            self.value = value
        else:
            raise ValueError("The value must be within the range of the dice faces.")

    def roll(self):
        self.value = random.randint(1, self.num_faces)
        return self.value

    def __str__(self):
        return f"Dice with {self.num_faces} faces shows {self.value}"
