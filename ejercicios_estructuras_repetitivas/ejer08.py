"""
Hacer un programa que muestre un cronómetro, indicando las horas, minutos y segundos.

Autor: Roberto Cano Estévez

Fecha: 26/10/2024
"""

import time

print("Cronómetro en formato hh:mm:ss.")
print("----------------------------------------------------------------")

hours = 0
minutes = 0
seconds = 0

while True:
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1
