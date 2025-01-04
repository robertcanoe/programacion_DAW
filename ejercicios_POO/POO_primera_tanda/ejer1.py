"""
Este script implementa varias clases para trabajar con conceptos básicos de programación orientada a objetos:

1. La clase `Dado` simula un dado estándar con seis caras y proporciona métodos para lanzarlo y obtener su valor.
2. La clase `Point` representa un punto en un plano cartesiano, con métodos para gestionar sus coordenadas y modificarlas.
3. La clase `Rectangulo` utiliza dos puntos (`Point`) para definir un rectángulo y calcular su área y perímetro.
4. La clase `DadoExtendido` extiende la funcionalidad de un dado, permitiendo configurar el número de caras y la cara superior inicial, además de incluir un método para lanzarlo.

El código incluye pruebas para cada clase, mostrando cómo funcionan y sus características principales.
"""
import random

# 1. Clase Dado
class Dado:
    def __init__(self):
        self.valor = random.randint(1, 6)

    def lanzar(self):
        self.valor = random.randint(1, 6)
        return self.valor

    def __str__(self):
        return f"Dado muestra {self.valor}"

# Prueba de la clase Dado
print("Prueba de la clase Dado")
dado = Dado()
print(dado)
print("Lanzando el dado...")
print(f"Resultado: {dado.lanzar()}")

# 2. Clase Point
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

# Prueba de la clase Point
print("\nPrueba de la clase Point")
p = Point(3, 5)
print(f"Punto inicial: {p}")
print(f"Coordenada x: {p.x}")
p.x = 0
print(f"Punto después de modificar x: {p}")
p.invert_coordinates()
print(f"Punto después de invertir coordenadas: {p}")

# 3. Clase Rectangulo
class Rectangulo:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    @property
    def area(self):
        return abs(self.p2.x - self.p1.x) * abs(self.p2.y - self.p1.y)

    @property
    def perimetro(self):
        return 2 * (abs(self.p2.x - self.p1.x) + abs(self.p2.y - self.p1.y))

# Prueba de la clase Rectangulo
print("\nPrueba de la clase Rectangulo")
p1 = Point(1, 2)
p2 = Point(4, 6)
rect = Rectangulo(p1, p2)
print(f"Área del rectángulo: {rect.area}")
print(f"Perímetro del rectángulo: {rect.perimetro}")

# 4. Clase Dado con más funcionalidad
class DadoExtendido:
    def __init__(self, cara_superior=None, num_caras=6):
        self.num_caras = num_caras
        self.valor = cara_superior if cara_superior is not None else random.randint(1, num_caras)

    @property
    def cara_superior(self):
        return self.valor

    @cara_superior.setter
    def cara_superior(self, value):
        if 1 <= value <= self.num_caras:
            self.valor = value
        else:
            raise ValueError("El valor debe estar dentro del rango de caras del dado.")

    def roll(self):
        self.valor = random.randint(1, self.num_caras)
        return self.valor

    def __str__(self):
        return f"Dado de {self.num_caras} caras muestra {self.valor}"

# Prueba de la clase DadoExtendido
print("\nPrueba de la clase DadoExtendido")
dados = [DadoExtendido(), DadoExtendido(4), DadoExtendido(3, 8), DadoExtendido(None, 10)]

for i, dado in enumerate(dados):
    print(f"Dado {i + 1}: {dado}")

print("Lanzando los dados...")
for i, dado in enumerate(dados):
    print(f"Dado {i + 1} después de lanzar: {dado.roll()}")
