"""
Escribir un programa que calcule el desglose mínimo en billetes y monedas de una cantidad exacta de euros. Hay billetes de 500, 200, 100, 50, 20, 10 y 5 € y monedas de 2 y 1 €.

Por ejemplo, si deseamos conocer el desglose de 434 €, el programa mostrará por pantalla el siguiente resultado:

- 2 billetes de 200 euros.
- 1 billete de 20 euros.
- 1 billete de 10 euros.
- 2 monedas de 2 euros.

Autor: Roberto Cano Estévez

Fecha: 19/10/2024
"""

print("Este programa calcula el desglose mínimo en billetes y monedas de una cantidad exacta de euros.")
print("-----------------------------------------------------------------------------------------------")

amount = 434  # Cantidad en euros
bills = [500, 200, 100, 50, 20, 10, 5]  # Billetes disponibles
coins = [2, 1]  # Monedas disponibles
change = {}  # Diccionario para almacenar el desglose

# Calcular el desglose en billetes
for bill in bills:
    if amount >= bill:
        change[bill] = amount // bill  # Número de billetes
        amount = amount % bill  # Resto de la cantidad

# Calcular el desglose en monedas
for coin in coins:
    if amount >= coin:
        change[coin] = amount // coin  # Número de monedas
        amount = amount % coin  # Resto de la cantidad

# Imprimir el resultado
print("Desglose de la cantidad:")
for denomination, count in change.items():
    if denomination >= 5:  # Para billetes
        print(f"- {count} billete(s) de {denomination} euros.")
    else:  # Para monedas
        print(f"- {count} moneda(s) de {denomination} euros.")
