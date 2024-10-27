"""
Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario,
el programa termina cuando se introduce un espacio.

Autor: Roberto Cano Estévez

Fecha: 26/10/2024
"""

print("Este programa identifica si un carácter es una vocal o no. El programa termina al introducir un espacio.")
print("----------------------------------------------------------------")

vowels = "aeiouAEIOU"
character = ""

while character != " ":
    character = input("Introduce un carácter: ")

    if character == " ":
        print("Programa terminado.")
        break
    elif character in vowels:
        print("VOCAL")
    else:
        print("NO VOCAL")
