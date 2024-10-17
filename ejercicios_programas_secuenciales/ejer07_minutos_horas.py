minutes = int(input("Ingresa la cantidad de minutos: "))

hours = minutes // 60
minutes_remaining = minutes % 60

print(f"{minutes} minutos son {hours} horas y {minutes_remaining} minutos.")
