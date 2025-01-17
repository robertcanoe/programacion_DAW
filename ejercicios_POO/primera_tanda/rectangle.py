"""
3. Implementa la clase Rectangulo (determinado por dos objetos Point) que además de su constructor, tendrá dos métodos para calcular su área y su perímetro que tienes que transformar en propiedades. Implementa también un test que cree dos puntos y un rectángulo a partir de estos dos puntos y que muestre el área y perímetro de dicho rectángulo.
"""
from point import Point

class Rectangle:
    
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    @property
    
    def area(self):
        width = abs(self.p2.x - self.p1.x)
        height = abs(self.p2.y - self.p1.y)
        return width * height

    @property
    
    def perimeter(self):
        return 2 * (abs(self.p2.x - self.p1.x) + abs(self.p2.y - self.p1.y))
    

    def peremiter(self):
        width = abs(self.p2.x - self.p1.x)
        height = abs(self.p2.y - self.p1.y)
        return 2 * width + height
