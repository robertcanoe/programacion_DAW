"""
Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

Autor: Roberto Cano Estévez

Fecha: 16/10/2024
"""
print("Escribe una cadena y programa te dira si son letras mayúsculas")
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")

# Programa que comprueba si una cadena es una letra mayúscula

chain = input("Introduce una cadena: ")

if len(chain) == 1 and chain.isupper():
    print(f"'{chain}' es una letra mayúscula.")
else:
    print(f"'{chain}' no es una letra mayúscula.")


