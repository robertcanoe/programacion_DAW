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

amount = 434
bills = [500, 200, 100, 50, 20, 10, 5]
coins = [2, 1]
change = {}

for bill in bills:
    if amount >= bill:
        change[bill] = amount // bill
        amount = amount % bill

for coin in coins:
    if amount >= coin:
        change[coin] = amount // coin
        amount = amount % coin

print(change)
