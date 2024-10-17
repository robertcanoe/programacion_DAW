"""
Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda. Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.

Autor: Roberto Cano Estévez

Fecha: 16/10/2024
"""
print("En este programa tienes que dar la edad de dos personas y te dice quien es mas joven, si la primera o la segunda")
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
years1 = int(input("Ingrese la edad de la primera persona: "))
years2 = int(input("Ingrese la edad de la segunda persona: "))

if years1 < years2:
    print("La primera persona es más joven que la segunda")
else:
    if years1 > years2:
        print("La segunda persona es más joven que la primera")
    else:
        print("Ambas personas tienen la misma edad")

