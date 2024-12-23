"""
Realiza un programa que pida la temperatura media que ha hecho en cada mes de un determinado año y que muestre a continuación un diagrama de barras horizontales con esos datos. Las barras del diagrama se pueden dibujar a base de asteriscos o cualquier otro carácter.

Autor: Roberto Cano Estévez

Fecha: 22/11/2024
"""
from arrays_bidimensionales.utils_float import request_float

print(  "Este programa solicita la temperatura media de cada mes de un año y muestra un diagrama de barras con esos datos.")
print("------------------------------------------------------------------------------------------------------------------------")

MONTHS = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
"Octubre", "Noviembre", "Diciembre"]
temperature = []

for month in MONTHS:
    temp = request_float(f"Ingrese el temperatura del {month}: ")
    temperature.append(temp)


print("\nDiagrama de barras de las temperaturas medias: ")
for i in range(12):
    print(f"{MONTHS[i]:<10} | {'*' * int(temperature[i])} ")













