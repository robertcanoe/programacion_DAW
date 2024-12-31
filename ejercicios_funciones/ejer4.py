import random
from math import sqrt

def menu():
    while True:
        print("\n" + "="*50)
        print(" " + "|{:^46}|".format("MENU PRINCIPAL"))  # Título centrado
        print("="*50)
        print(" 1. Muestra los números primos entre 1 y 1000.")
        print(" 2. Muestra los números capicúa que hay entre 1 y 99999.")
        print(" 3. Muestra la moda de 50 números enteros aleatorios entre 1 y 10.")
        print(" 4. Muestra la mediana de 10 números enteros aleatorios entre 1 y 50.")
        print(" 5. Muestra el máximo y mínimo de 1000 números enteros aleatorios entre 1 y 50000.")
        print(" 6. Muestra la varianza de 10 números enteros aleatorios entre 1 y 5.")
        print(" 0. SALIR")
        print("="*50)

        options = int(input("Ingrese una opción válida: "))
        print("="*50)

        if options == 1:
            print("Entrado en la opción 1...")
            NumberPrim()

        elif options == 2:
            print("Entrado en la opción 2...")
            NumbersCapicua()

        elif options == 3:
            print("Entrado en la opción 3...")
            NumberModa()

        elif options == 4:
            print("Entrado en la opción 4...")
            NumberMediana()

        elif options == 5:
            print("Entrado en la opción 5...")
            NumberMaxMin()

        elif options == 6:
            print("Entrado en la opción 6...")
            NumberVarianza()

        elif options == 0:
            print("Saliendo del programa....")
            print("="*50)
            exit(0)

def NumberPrim():
    numbers_primes = []
    for n in range(2, 1000):
        is_prime = True
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break
        
        if is_prime:
            numbers_primes.append(n)
    print("Números primos encontrados entre 1 y 1000:")
    print(numbers_primes)

def NumbersCapicua():
    numbers_capicua = []
    for n in range(1, 99999):
        if str(n) == str(n)[::-1]:
            numbers_capicua.append(n)
    print("Números capicúa encontrados entre 1 y 99999:")
    print(numbers_capicua)

def NumberModa():
    numbers = [random.randint(1, 10) for _ in range(50)]
    print(f"Números generados: {numbers}")
    mode = None
    max_count = 0
    for n in numbers:
        count = 0
        for num in numbers:
            if num == n:
                count += 1
        if count > max_count:
            max_count = count
            mode = n
    print(f"La moda es: {mode}")

def NumberMediana():
    numbers = [random.randint(1, 50) for _ in range(10)]
    print(f"Números generados: {numbers}")
    numbers.sort()
    median = numbers[4] if len(numbers) % 2 != 0 else (numbers[4] + numbers[5]) / 2
    print(f"La mediana es: {median}")

def NumberMaxMin():
    numbers = [random.randint(1, 50000) for _ in range(1000)]
    max_num = max(numbers)
    min_num = min(numbers)
    print(f"Máximo: {max_num}, Mínimo: {min_num}")

def NumberVarianza():
    numbers = [random.randint(1, 5) for _ in range(10)]
    print(f"Números generados: {numbers}")
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    print(f"La varianza es: {variance}")

if __name__ == "__main__":
    menu()
