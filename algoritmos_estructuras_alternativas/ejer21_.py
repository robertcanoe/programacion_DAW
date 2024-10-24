"""
Realiza un programa que pida tres números enteros y diga cuál es el mayor.

Autor: Roberto Cano Estévez
Fecha: 23/10/2024
"""

print("Este programa te dice cual de los 3 números es mayor.")
print("-----------------------------------------------------")

n1 = int(input("Dime el primer numero: "))
n2 = int(input("Dime el segundo numero: "))
n3 = int(input("Dime el tercer numero: "))

if n1 > n2 and n1 > n3:
    print("El mayor es ", n2)

elif n2 > n3:
    print("El mayor es ", n2)

else:
    print("El mayor es ", n3)
