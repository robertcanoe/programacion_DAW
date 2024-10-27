"""
Diseña un programa que lea un carácter de teclado y muestre por pantalla el mensaje «Es signo de puntuación» solo si el carácter leído es un signo de puntuación, «Es una letra» si es una letra (da igual que sea mayúscula, minúscula o acentuada), «Es un dígito» si es un dígito, «Es otro carácter» si no es ninguno de los anteriores y «No es un carácter» si el usuario ha introducido más de un carácter.

Autor: Roberto Cano Estévez

Fecha: 16/10/2024
"""

# Signos de puntuación que queremos reconocer
punctuation_marks = ".,;:!?¡¿-()[]{}'\""

# Solicitar al usuario que ingrese un carácter
char = input("Introduce un carácter: ")

# Verificar si el usuario ha introducido más de un carácter
if len(char) != 1:
    print("No es un carácter")
else:
    # Verificar si es un signo de puntuación
    if punctuation_marks.find(char) != -1:
        print("Es signo de puntuación")
    else:
        # Verificar si es una letra
        if char.isalpha():
            print("Es una letra")
        else:
            # Verificar si es un dígito
            if char.isdigit():
                print("Es un dígito")
            else:
                # Si no es ninguno de los anteriores
                print("Es otro carácter")

