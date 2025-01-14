"""
2. Implementa una clase Point con sus atributos x e y. La clase debe contener: su constructor, los getters y setters (propiedades), un invert_coordinates() que invierta las coordenadas x e y del punto. Además la clase debe tener un __str__() para poder imprimir los puntos en formato “(x,y)”. Implementa un test donde crees un punto, lo imprimas utilizando de manera implícita el método __str__(), imprimas su coordenada x, asignes 0 a su coordenada x, y vuelvas a imprimir el punto.
"""
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def invert_coordinates(self):
        self._x, self._y = self._y, self._x

    def __str__(self):
        return f"({self._x},{self._y})"
