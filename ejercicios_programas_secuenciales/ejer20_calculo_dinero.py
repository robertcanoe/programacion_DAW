"""
Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuántas monedas tenemos de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos.
Hecho por: Roberto Cano Estévez
Fecha: 14/10/2024
"""

print("Este programa calculará el total de dinero que tienes según el número de monedas que ingreses.")

coins_2e = int(input("Introduce el número de monedas de 2€: "))
coins_1e = int(input("Introduce el número de monedas de 1€: "))
coins_50c = int(input("Introduce el número de monedas de 50 céntimos: "))
coins_20c = int(input("Introduce el número de monedas de 20 céntimos: "))
coins_10c = int(input("Introduce el número de monedas de 10 céntimos: "))

total = coins_2e * 2 + coins_1e * 1 + coins_50c * 0.5 + coins_20c * 0.2 + coins_10c * 0.1

print(f"El total de dinero es: {total} euros")
