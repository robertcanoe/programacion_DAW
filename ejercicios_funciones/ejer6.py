"""
Crea una función que reciba un número, lo convierta al sistema Morse y lo devuelve en una cadena de caracteres. 

Por ejemplo, el 213 es el ..___ .____ ...__ en Morse. Utiliza esta función en un programa para comprobar que funciona bien.

Desde la función no se debe mostrar nada por pantalla, solo se debe usar print desde el programa principal.

Los números en Morse los puedes encontrar aquí
"""

MORSE_NUMEROS = {
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.'
}

def convertir_a_morse(numero):
    numero_str = str(numero)
    morse = [MORSE_NUMEROS[digito] for digito in numero_str]
    return ' '.join(morse)

def main():
    numero = int(input("Introduce un número: "))
    resultado_morse = convertir_a_morse(numero)
    print(f"El número {numero} en Morse es: {resultado_morse}")

if __name__ == "__main__":
    main()
