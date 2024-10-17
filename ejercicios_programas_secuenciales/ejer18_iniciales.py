# "Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales."
# Hecho por: Roberto Cano Estevez
# Fecha: 14/10/2024

nombre = input("Introduce tu nombre: ")
apellidos = input("Introduce tus apellidos: ")

# Tomamos la primera letra del nombre y la primera de cada apellido
iniciales = nombre[0] + apellidos.split()[0][0] + apellidos.split()[1][0]
print(f"Las iniciales son: {iniciales.upper()}")
