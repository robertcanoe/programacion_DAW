"""
Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que tipo de triángulo es, teniendo en cuenta los siguientes:

- Si se cumple Pitágoras entonces es triángulo rectángulo
- Si solo dos lados del triángulo son iguales entonces es isósceles.
- Si los 3 lados son iguales entonces es equilátero.
- Si no se cumple ninguna de las condiciones anteriores, es escaleno.

Autor: Roberto Cano Estévez

Fecha: 19/10/2024
"""
print("Este programa te pide dos números y te muestra su division")
print("------------------------------------------------------------")

side_a = 3
side_b = 4
side_c = 5

if (side_a**2 + side_b**2 == side_c**2) or (side_a**2 + side_c**2 == side_b**2) or (side_b**2 + side_c**2 == side_a**2):
    triangle_type = "Triángulo Rectángulo"
elif side_a == side_b == side_c:
    triangle_type = "Triángulo Equilátero"
elif side_a == side_b or side_b == side_c or side_a == side_c:
    triangle_type = "Triángulo Isósceles"
else:
    triangle_type = "Triángulo Escaleno"

print(triangle_type)
