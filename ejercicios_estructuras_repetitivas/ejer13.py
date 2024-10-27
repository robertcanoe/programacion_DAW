"""
Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y viceversa.

Autor: Roberto Cano Estévez

Fecha: 26/10/2024
"""

print("Este programa convierte mayúsculas en minúsculas y viceversa en una cadena dada.")
print("----------------------------------------------------------------")

text = input("Introduce una cadena: ")
converted_text = text.swapcase()
print(f"Cadena convertida: {converted_text}")
