"""
El programa es una biblioteca de funciones numéricas que realiza diversas operaciones sobre números enteros, como verificar si son capicúas o primos, contar sus dígitos, invertirlos, y manipular sus componentes (añadir o quitar dígitos). Cada función es independiente y permite trabajar con números de manera eficiente sin usar conversiones a cadenas. El programa también incluye una función de prueba para verificar que todas las funciones funcionen correctamente.

Autor: Roberto Cano Estévez

Fecha: 09/12/2024
"""

def capicua (n):
    """Verifica si un número es capicúa."""
    original = n
    invertido = 0
    while n > 0:
        invertido = invertido * 10 + n % 10
        n //= 10
    return original == invertido

def es_primo(n):
    """Verifica si un número es primo."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_number(n):
    """Cuenta la cantidad de dígitos de un número."""
    if n == 0:
        return 1
    contador = 0
    while n > 0:
        n //= 10
        contador += 1
    return contador

def invertir_numero(n):
    """Invierte los dígitos de un número."""
    invertido = 0
    while n > 0:
        invertido = invertido * 10 + n % 10
        n //= 10
    return invertido

def add_digit(n, d):
    """Añade un dígito al final de un número."""
    return n * 10 + d

def quitar_digito(n):
    """Quita el último dígito de un número."""
    return n // 10

def probar_funciones():
    """Prueba todas las funciones definidas."""
    assert capicua(121) == True
    assert capicua(123) == False
    assert es_primo(7) == True
    assert es_primo(10) == False
    assert count_number(12345) == 5
    assert invertir_numero(1234) == 4321
    assert add_digit(123, 4) == 1234
    assert quitar_digito(123) == 12
    print("Todas las pruebas pasaron correctamente.")

