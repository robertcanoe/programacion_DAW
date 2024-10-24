"""
Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.

Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.”.
Ejemplo:

Introduzca número del dado: 5
En la cara opuesta está el "dos".


Autor: Roberto Cano Estévez

Fecha: 19/10/2024
"""

print("programa que solicita al usuario que introduzca un número del dado")
print("------------------------------------------------------------------")
die_number = int(input("Elige un número (1-6): "))
opposite_faces = {1: "seis", 2: "cinco", 3: "cuatro", 4: "tres", 5: "dos", 6: "uno"}

# Verificar si el número está en el rango válido
if 1 <= die_number <= 6:
    result = opposite_faces[die_number]
    print(f"En la cara opuesta está el \"{result}\".")
else:
    print("ERROR: número incorrecto.")
