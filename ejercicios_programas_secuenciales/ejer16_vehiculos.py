# "Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con eso determinar y mostrar en qué tiempo (minutos) alcanzará el vehículo más rápido al otro."
# Hecho por: Roberto Cano Estevez
# Fecha: 14/10/2024

D = float(input("Introduce la distancia entre los vehículos (km): "))
c1 = float(input("Introduce la velocidad del vehículo más lento (km/h): "))
c2 = float(input("Introduce la velocidad del vehículo más rápido (km/h): "))

# Tiempo en que el vehículo más rápido alcanzará al más lento
time = D / (c2 - c1) * 60

print(f"El vehículo más rápido alcanzará al otro en {time} minutos.")

