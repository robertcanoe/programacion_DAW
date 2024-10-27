"""
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €,
el tercero 40 € y así sucesivamente. Realizar un programa para determinar cuánto debe pagar
mensualmente y el total de lo que pagará después de los 20 meses.

Autor: Roberto Cano Estévez

Fecha: 26/10/2024
"""

print("Este programa calcula los pagos mensuales y el total a pagar durante 20 meses con pagos duplicados cada mes.")
print("----------------------------------------------------------------")

initial_payment = 10
total_payment = 0

for month in range(1, 21):
    monthly_payment = initial_payment * (2 ** (month - 1))
    total_payment += monthly_payment
    print(f"Mes {month}: {monthly_payment} €")

print(f"El total pagado después de 20 meses es: {total_payment} €")
