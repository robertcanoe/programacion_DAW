"""
Define tres arrays de 20 números enteros cada uno, con nombres número, cuadrado y cubo. Carga el array número con valores aleatorios entre 0 y 100. En el array cuadrado se deben almacenar los cuadrados de los valores que hay en el array número. En el array cubo se deben almacenar los cubos de los valores que hay en número. A continuación, muestra el contenido de los tres arrays dispuesto en tres columnas.

Autor: Roberto Cano Estévez

Fecha: 22/11/2024
"""
from random import randint

number = []
squared = []
cube = []

print("Este programa genera 20 números aleatorios entre 0 y 100. Luego, calcula y muestra el cuadrado y el cubo de cada uno de estos números.")
print("--------------------------------------------------------------------------------------------------------------------------------------")
for i in range(20):
    value = randint(0, 100)
    number.append(value)
    squared.append(value ** 2)
    cube.append(value ** 3)

print(f"{"número":<10}{"Cuadrado":<15}{"Cubo":<15}")
for i in range(20):
    print(f"{number[i]:<10}{squared[i]:<15}{cube[i]:<15}")