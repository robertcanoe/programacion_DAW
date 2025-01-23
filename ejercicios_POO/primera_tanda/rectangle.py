"""
3. Implementa la clase Rectangulo (determinado por dos objetos Point) que además de su constructor, tendrá dos métodos para calcular su área y su perímetro que tienes que transformar en propiedades. Implementa también un test que cree dos puntos y un rectángulo a partir de estos dos puntos y que muestre el área y perímetro de dicho rectángulo.
"""
from point import Point

class Rectangle:
  
    def __init__(self, p1, p2):
        self.__p1 = p1
        self.__p2 = p2
        self.update_dimensions()
    
    @property
    
    def area(self):
        return self.__width * self.__height

    @property
    
    def perimeter(self):
        return 2 * (self.__width + self.__height)
    
    @property

    def p1(self):
        return self.__p1
    
    @p1.setter
    
    def p1(self, value):
        self.__p1 = value
        self.update_dimensions()
    
    @property

    def p2(self):
        return self.__p2
    
    @p2.setter

    def p2(self, value):
        self.__p2 = value
        self.update_dimensions()

    def update_dimensions(self):

        self.__width = abs(self.__p2.x - self.__p1.x)
        self.__height = abs(self.__p2.y - self.__p1.y)
