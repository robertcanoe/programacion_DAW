# "Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuánto valen al final las dos variables."
# Hecho por: Roberto Cano Estevez
# Fecha: 14/10/2024

A = float(input("Introduce el valor de A: "))
B = float(input("Introduce el valor de B: "))

# Intercambiamos los valores de A y B
A, B = B, A

print(f"Ahora, A vale: {A} y B vale: {B}")
