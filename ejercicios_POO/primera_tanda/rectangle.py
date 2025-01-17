"""
3. Implementa la clase Rectangulo (determinado por dos objetos Point) que además de su constructor, tendrá dos métodos para calcular su área y su perímetro que tienes que transformar en propiedades. Implementa también un test que cree dos puntos y un rectángulo a partir de estos dos puntos y que muestre el área y perímetro de dicho rectángulo.
"""
from point import Point

class Rectangle:
  
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.update_dimensions()
    
    @property
    
    def area(self):
        return self._width * self._height

    @property
    
    def perimeter(self):
        return 2 * (self._width + self._height)
    
    @property

    def p1(self):
        return self._p1
    
    @p1.setter
    
    def p1(self, value):
        self._p1 = value
        self.update_dimensions()
    
    @property

    def p2(self):
        return self._p2
    
    @p2.setter

    def p2(self, value):
        self._p2 = value
        self.update_dimensions()

    def update_dimensions(self):

        self._width = abs(self._p2.x - self._p1.x)
        self._height = abs(self._p2.y - self._p1.y)
