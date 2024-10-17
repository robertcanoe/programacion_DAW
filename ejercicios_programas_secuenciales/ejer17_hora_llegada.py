# "Un ciclista parte de una ciudad a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B."
# Hecho por: Roberto Cano Estevez
# Fecha: 14/10/2024

HH = int(input("Introduce la hora de partida (HH): "))
MM = int(input("Introduce los minutos de partida (MM): "))
SS = int(input("Introduce los segundos de partida (SS): "))
T = int(input("Introduce el tiempo de viaje en segundos: "))

# Convertimos la hora inicial a segundos
tiempo_inicial = HH * 3600 + MM * 60 + SS
# Sumamos el tiempo de viaje
tiempo_final = tiempo_inicial + T

# Convertimos el tiempo final a horas, minutos y segundos
HH_final = tiempo_final // 3600 % 24
MM_final = (tiempo_final % 3600) // 60
SS_final = tiempo_final % 60

print(f"El ciclista llegará a las {HH_final:02}:{MM_final:02}:{SS_final:02}")
