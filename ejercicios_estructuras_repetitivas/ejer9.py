"""
Mostrar en pantalla los N primeros números primos. Se pide por teclado la cantidad de números primos que queremos mostrar.

Autor: Roberto Cano Estévez

Fecha: 26/10/2024
"""

print("Este programa muestra los primeros N números primos.")
print("----------------------------------------------------------------")

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

n = int(input("Introduce la cantidad de números primos que quieres ver: "))
count = 0
num = 2

while count < n:
    if is_prime(num):
        print(num)
        count += 1
    num += 1
