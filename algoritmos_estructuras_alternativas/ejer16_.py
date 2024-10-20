"""
La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que está dura, de tal forma que los primeros cinco minutos cuestan 1 euro por minuto, los siguientes tres, 80 céntimos por minuto, los siguientes dos minutos, 70 céntimos por minuto, y a partir del décimo minuto, 50 céntimos por minuto.

Además, se carga un impuesto de 3% cuando es domingo, y si es otro día, en turno de mañana, 15%, y en turno de tarde, 10%. Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.

Autor: Roberto Cano Estévez

Fecha: 19/10/2024
"""

call_minutes = 15

if call_minutes <= 3:
    cost = call_minutes * 1
elif call_minutes <= 5:
    cost = 3 + (call_minutes - 3) * 0.80
elif call_minutes <= 10:
    cost = 4.6 + (call_minutes - 5) * 0.70
else:
    cost = 8.1 + (call_minutes - 10) * 0.50

print(cost)
