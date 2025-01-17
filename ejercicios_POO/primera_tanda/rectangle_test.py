from rectangle import Point, Rectangle

p1 = Point(1, 2)
p2 = Point(4, 6)

# Crear un rectángulo con los puntos
rect = Rectangle(p1, p2)

# Mostrar área y perímetro iniciales
print(f"Área inicial: {rect.area}")          # 12
print(f"Perímetro inicial: {rect.perimeter}") # 14

# Modificar un punto del rectángulo
rect.p1 = Point(2, 3)
print(f"Nuevo área: {rect.area}")            # 6
print(f"Nuevo perímetro: {rect.perimeter}")  # 10
