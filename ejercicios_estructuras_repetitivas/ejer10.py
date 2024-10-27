"""
Pide una cadena y un carácter por teclado y muestra cuantas veces aparece el carácter en la cadena.

Autor: Roberto Cano Estévez

Fecha: 26/10/2024
"""

print("Este programa cuenta cuántas veces aparece un carácter específico en una cadena dada.")
print("----------------------------------------------------------------")

text = input("Introduce una cadena: ")
character = input("Introduce el carácter a buscar: ")

occurrences = text.count(character)
print(f"El carácter '{character}' aparece {occurrences} veces en la cadena.")
