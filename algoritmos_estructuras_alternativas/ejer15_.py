"""
El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos. Realiza un programa que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.

Autor: Roberto Cano Estévez

Fecha: 19/10/2024
"""

students = 60

if students >= 100:
    cost = students * 65
elif 50 <= students <= 99:
    cost = students * 70
elif 30 <= students <= 49:
    cost = students * 95
else:
    cost = 4000

print(cost)
