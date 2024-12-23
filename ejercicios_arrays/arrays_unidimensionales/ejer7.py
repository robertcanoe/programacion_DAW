"""
Escribe un programa que lea 15 números por teclado y que los almacene en un array. Rota los elementos de ese array, es decir, el elemento de la posición 0 debe pasar a la posición 1, el de la 1 a la 2, etc. El número que se encuentra en la última posición debe pasar a la posición 0. Finalmente, muestra el contenido del array.

Autor: Roberto Cano Estévez

Fecha: 24/11/2024
"""
from arrays_bidimensionales.utils_int import request_int

print("Este programa rota los 15 elementos dados sumando 1, el de la posición 0 pasa a la 1... y así continuamente")
print("-----------------------------------------------------------------------------------------------------------")

l = []

for i in range(15):
    number = request_int(f"Ingrese el número {i + 1}: ")
    l.append(number)
array = [l[-1]] + l[:-1]

print("\n")
print(f"Esta es la lista editada: {array}")
