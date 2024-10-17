"""
Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.

Autor: Roberto Cano Estévez

Fecha: 16/10/2024
"""
print("Este programa te pide dos números y te muestra su division")
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")

n1 = float(input("Dime el primer número: "))
n2 = float(input("Dime el segundo número: "))

if n2 != 0:
    # Realizar la división si n2 no es cero
    result = n1 / n2
    print(f"La división de {n1} entre {n2} es: {result}")
else:
    # Mostrar mensaje de advertencia si n2 es cero
    print("No se puede dividir entre cero. Por favor, introduce un número distinto de cero.")
