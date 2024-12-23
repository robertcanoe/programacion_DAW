"""
Este programa calcula el coeficiente binomial C(n, m) a partir de los valores de n y m ingresados por el usuario.
Primero calcula los factoriales de n, m y (n - m), luego muestra estos valores y el coeficiente binomial.
La fórmula para el coeficiente binomial es:

    C(n, m) = n! / (m! * (n - m)!)

Donde:
- n! es el factorial de n
- m! es el factorial de m
- (n - m)! es el factorial de (n - m)

Autor: Roberto Cano Estévez

Fecha: 22/11/2024
"""
import math

print("Este programa calcula el número factorial en base a los números dados de m y n")
print("------------------------------------------------------------------------------")

while True:
    try:
        n = int(input("Pon el valor de n: "))
        m = int(input("Pon el valor de m: "))

        if n >= m:
            break
        else:
            print("Error: El valor de n debe ser mayor o igual que m.")

    except ValueError:
        print("Error: Debes ingresar números enteros para n y m.")

n_fact = math.factorial(n)
m_fact = math.factorial(m)
nm_fact = math.factorial(n - m)

binomial_coefficient = n_fact // (m_fact * nm_fact)

print(f"El factorial de n ({n}) es: {n_fact}")
print(f"El factorial de m ({m}) es: {m_fact}")
print(f"El factorial de (n - m) ({n} - {m}) es: {nm_fact}")
print(f"El coeficiente binomial C({n}, {m}) es: {binomial_coefficient}")
