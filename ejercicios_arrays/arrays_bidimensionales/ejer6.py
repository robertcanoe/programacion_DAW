"""
Este programa calcula la estatura media, mínima y máxima de personas de diferentes países. Usa una matriz de 4 filas y 10 columnas para simular las estaturas de personas de los países: España, Rusia, Japón y Australia, generadas aleatoriamente entre 140 cm y 210 cm.

El programa imprime la media, mínima y máxima de las estaturas por país.

Autor: Roberto Cano Estévez

Fecha: 08/12/2024
"""
import random

print("Programa que calcula la estatura média, mínima y máxima de personas de diferentes países.")
print("-----------------------------------------------------------------------------------------")

ROWS = 4
COLUMNS = 10
countries = ["España", "Rusia", "Japón", "Australia"]
matrix = []

for i in range(ROWS):
    row = [random.randint(140, 210) for _ in range(COLUMNS)]
    matrix.append(row)

for i in range(ROWS):
    country = countries[i]
    row = matrix[i]

