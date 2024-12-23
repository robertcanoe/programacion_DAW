def request_int(message):

    while True:
        try:
            return int(input(message))  # Devuelve el número entero si es válido
        except ValueError:
            print("Error: Por favor, introduzca un número entero válido.")
