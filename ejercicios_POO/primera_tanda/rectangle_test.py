from rectangle import Point, Rectangle

p1 = Point(1, 2)
p2 = Point(4, 6)

# Crea un rectángulo con esos puntos
rect = Rectangle(p1, p2)

# Esto va a mostrar el área y el perímetro
print(f"Área del rectángulo: {rect.area}")      
print(f"Perímetro del rectángulo: {rect.perimeter}")