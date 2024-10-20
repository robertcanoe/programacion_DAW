"""
Una compañía de transporte internacional tiene servicio en algunos países de América del Norte,
América Central, América del Sur, Europa y Asia. El costo por el servicio de transporte
se basa en el peso del paquete y la zona a la que va dirigido.

Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados.
Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.

Autor: Roberto Cano Estévez
Fecha: 19/10/2024
"""
print("Este programa calcula el costo del transporte de un paquete según la zona y el peso.")
print("------------------------------------------------------------------------------------")

zone = int(input("Introduce la zona (1 a 5) a donde se dirige el paquete: "))
weight = float(input("Introduce el peso del paquete en kg: "))

if weight > 5:
    print("Los paquetes que pesen más de 5 kg no pueden ser transportados.")
else:
    if zone == 1:
        cost_per_gram = 24.00
    elif zone == 2:
        cost_per_gram = 20.00
    elif zone == 3:
        cost_per_gram = 21.00
    elif zone == 4:
        cost_per_gram = 10.00
    elif zone == 5:
        cost_per_gram = 18.00
    else:
        print("Error: Zona no válida.")
        exit()

    total_cost = weight * 1000 * cost_per_gram
    print(f"El costo por transportar el paquete es de {total_cost:.2f} euros.")




zone = int(input("Introduce la zona (1 a 5) a donde se dirige el paquete: "))
weight = float(input("Introduce el peso del paquete en kg: "))

if weight > 5:
    print("Los paquetes que pesen más de 5 kg no pueden ser transportados.")
else:
    if zone == 1:
        cost_per_gram = 24.00
    elif zone == 2:
        cost_per_gram = 20.00
    elif zone == 3:
        cost_per_gram = 21.00
    elif zone == 4:
        cost_per_gram = 10.00
    elif zone == 5:
        cost_per_gram = 18.00
    else:
        print("Error: Zona no válida.")
        exit()

    total_cost = weight * 1000 * cost_per_gram
    print(f"El costo por transportar el paquete es de {total_cost:.2f} euros.")
