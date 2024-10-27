"""
Pide una cadena y dos caracteres por teclado (valida que sea un carácter),
sustituye la aparición del primer carácter en la cadena por el segundo carácter.

Autor: Roberto Cano Estévez

Fecha: 26/10/2024
"""

print("Este programa sustituye un carácter en una cadena por otro carácter especificado.")
print("----------------------------------------------------------------")

text = input("Introduce una cadena: ")
char1 = input("Introduce el carácter a reemplazar: ")
char2 = input("Introduce el carácter de reemplazo: ")

result = text.replace(char1, char2)
print(f"Cadena resultante: {result}")
