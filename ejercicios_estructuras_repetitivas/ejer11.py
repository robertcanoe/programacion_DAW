"""
Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios),
realiza un programa que cuente cuantas palabras tiene.

Autor: Roberto Cano Estévez

Fecha: 26/10/2024
"""

print("Este programa cuenta el número de palabras en una frase introducida.")
print("----------------------------------------------------------------")

phrase = input("Introduce una frase: ")
word_count = len(phrase.split())
print(f"La frase tiene {word_count} palabras.")
