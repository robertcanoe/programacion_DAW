"""
Crea una función que reciba un número, lo convierta al sistema de palotes y lo devuelva en una cadena de caracteres. 

Por ejemplo, el 470213 en decimal es el | | | | - | | | | | | | - - | | - | - | | | en el sistema de palotes. 

Utiliza esta función en un programa para comprobar que funciona bien. Desde la función no se debe mostrar nada por pantalla, solo se debe usar print desde el programa principal.

"""

def convertir_a_palotes(numero):
    resultado = []
    for digito in str(numero):
        valor = int(digito)
        resultado.append('| ' * valor if valor > 0 else '-')
    return '- '.join(resultado)

def main():
    numero = int(input("Introduce un número: "))
    resultado_palotes = convertir_a_palotes(numero)
    print(f"El número {numero} en el sistema de palotes es: {resultado_palotes}")

if __name__ == "__main__":
    main()
