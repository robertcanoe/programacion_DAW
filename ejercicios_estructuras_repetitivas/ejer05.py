"""
Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que el superior lo tiene que volver a pedir.

A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:

- La suma de los números que están dentro del intervalo (intervalo abierto).
- Cuantos números están fuera del intervalo.
- Informa si hemos introducido algún número igual a los límites del intervalo.

Autor: Roberto Cano Estévez

Fecha: 26/10/2024
"""

print("Este programa solicita un intervalo y luego permite introducir números, mostrando resultados al final.")
print("----------------------------------------------------------------")

# Solicitar límites del intervalo y validar que el límite inferior sea menor que el superior
while True:
    lower_limit = int(input("Introduce el límite inferior del intervalo: "))
    upper_limit = int(input("Introduce el límite superior del intervalo: "))

    if lower_limit < upper_limit:
        break
    else:
        print("El límite inferior debe ser menor que el límite superior. Vuelve a intentarlo.")

# Variables de conteo y suma
sum_within_interval = 0
count_outside_interval = 0
matched_limits = False

# Solicitar números hasta que se introduzca un 0
while True:
    user_number = int(input("Introduce un número (0 para terminar): "))

    if user_number == 0:
        break

    if lower_limit < user_number < upper_limit:
        sum_within_interval += user_number
    else:
        count_outside_interval += 1

    if user_number == lower_limit or user_number == upper_limit:
        matched_limits = True

# Resultados finales
print("Resultados:")
print(f"Suma de los números dentro del intervalo: {sum_within_interval}")
print(f"Cantidad de números fuera del intervalo: {count_outside_interval}")
print("Se ha introducido algún número igual a los límites del intervalo." if matched_limits else "No se ha introducido ningún número igual a los límites del intervalo.")
