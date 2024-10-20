"""
La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto, esta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.

Autor: Roberto Cano Estévez

Fecha: 19/10/2024
"""

initial_price = float(input("Ingrese el precio inicial por kilo de uva: "))
grape_type = input("Ingrese el tipo de uva (A o B): ").upper()
grape_size = int(input("Ingrese el tamaño de uva (1 o 2): "))
kilos = float(input("Ingrese la cantidad de kilos entregados: "))

if grape_type == 'A':
    if grape_size == 1:
        final_price = initial_price + 0.20
    elif grape_size == 2:
        final_price = initial_price + 0.30
    else:
        print("Tamaño de uva no válido.")
        final_price = 0
elif grape_type == 'B':
    if grape_size == 1:
        final_price = initial_price - 0.30
    elif grape_size == 2:
        final_price = initial_price - 0.50
    else:
        print("Tamaño de uva no válido.")
        final_price = 0
else:
    print("Tipo de uva no válido.")
    final_price = 0

earnings = final_price * kilos

if final_price != 0:
    print(f"La ganancia obtenida es: {earnings:.2f} euros.")

