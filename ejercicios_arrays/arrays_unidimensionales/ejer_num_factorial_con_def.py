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

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

print("Este programa calcula el coeficiente binomial en base a los números dados de m y n, usando funciones")
print("----------------------------------------------------------------------------------------------------")

while True:
    try:
        n = int(input("Ingrese el valor de n: "))
        m = int(input("Ingrese el valor de m: "))

        if n >= m:
            break
        else:
            print("Error: El valor de n debe de ser mayor o igual que m")
    except ValueError:
        print("Error: Debes ingresar números enteros para n y m.")
        exit(1)

binomial_coefficient = factorial(n) // (factorial(m) * factorial(n - m))

print(f"El número combinatorio de {n} sobre {m} es: {binomial_coefficient}")