'''
"Realiza un programa que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se puede calcular?"
 Hecho por: Roberto Cano Estevez
 Fecha: 14/10/2024
 '''
import math

num = float(input("Introduce un número: "))
square_root = math.sqrt(num)  # Raíz cuadrada usando math.sqrt
cube_root = num ** (1/3)  # Raíz cúbica elevando el número a la potencia 1/3

print(f"La raíz cuadrada de {num} es: {square_root}")
print(f"La raíz cúbica de {num} es: {cube_root}")

