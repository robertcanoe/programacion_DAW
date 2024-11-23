"""
Realiza un programa que pida la temperatura media que ha hecho en cada mes de un determinado año y que muestre a continuación un diagrama de barras horizontales con esos datos. Las barras del diagrama se pueden dibujar a base de asteriscos o cualquier otro carácter.

Autor: Roberto Cano Estévez

Fecha: 22/11/2024
"""

print("Este programa pide la temperatura media que ha hecho en cada mes de un determinado y muestra un diagrama con esos datos.")

months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
"Octubre", "Noviembre", "Diciembre"]
temperature = []

try:
    for month in months:
        temp = float(input(f"Ingrese el temperatura del {month}: "))
        temperature.append(temp)
except ValueError:
    print("Error: Por favor ingrese temperaturas válidas en números")
    exit(1)

print("\nDiagrama de barras de las temperaturas medias: ")
for i in range(12):
    print(f"{months[i]:<10} | {'*' * int(temperature[i])} ")














