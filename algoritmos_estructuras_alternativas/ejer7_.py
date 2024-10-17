"""
Realiza un programa que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:

    -El exponente sea positivo, solo tienes que imprimir la potencia.
    -El exponente sea 0, el resultado es 1.
    -El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

Autor: Roberto Cano Estévez

Fecha: 16/10/2024
"""
print("Ingrese la base y el exponente para calcular la potencia.")
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")

base = float(input("Ingrese la base: "))
exponent = int(input("Ingrese el exponente: "))

if exponent > 0:
    result = base ** exponent
    print(f"El resultado de {base} elevado a {exponent} es: {result}")

if exponent == 0:
    print("El resultado de cualquier número elevado a 0 es: 1")
if exponent < 0:
    result = 1 / (base ** abs(exponent))
    print(f"El resultado de {base} es: {result}")
