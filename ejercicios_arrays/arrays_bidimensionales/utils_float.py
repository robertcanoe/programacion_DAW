def request_float(message):

    while True:
        try:
            return float(input(message))  # Devuelve el número entero si es válido
        except ValueError:
            print("Error: Por favor, introduzca un número flotante válido.")
