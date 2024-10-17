# "Pide al usuario dos pares de números x1, y1 y x2, y2, que representan dos puntos en el plano. Calcula y muestra la distancia entre ellos."
# Hecho por: Roberto Cano Estévez
# Fecha: 14/10/2024

import math

x1 = float(input("Introduce x1: "))
y1 = float(input("Introduce y1: "))
x2 = float(input("Introduce x2: "))
y2 = float(input("Introduce y2: "))

# Fórmula de la distancia entre dos puntos en un plano: √((x2 - x1)^2 + (y2 - y1)^2)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"La distancia entre los puntos es: {distancia}")
