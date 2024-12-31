"""
Define la función mezcla de forma que tome dos listas como parámetros y devuelve otra que es el resultado de mezclar los números de ambos de forma alterna, se coge un número de a, luego de b, luego de a, etc. Los arrays a y b pueden tener longitudes diferentes; por tanto, si se terminan los números de un array se terminan de coger todos los que quedan del otro.

Ejemplos:

Si a = [8, 9, 0] y b = [1, 2, 3], mezcla(a, b) devuelve [8, 1, 9, 2, 0, 3 ]

Si a = [4, 3] y b = [7, 8, 9, 10], mezcla(a, b) devuelve [4, 7, 3, 8, 9, 10]

Si a = [8, 9, 0, 3] y b = [1], mezcla(a, b) devuelve [8, 1, 9, 0, 3]

Si a = [ ] y b = [1, 2, 3], mezcla(a, b) devuelve [1, 2, 3]
"""

arra_mezcl = []

def mezcla():
    while True:

        list1 = int(input("Ingrese los números de tu lista 1 (0 para salir): "))
        list2 = int(input("Ingrese los números de tu lista 2 (0 para salir): "))

        if list1 or list2 == 0:
            exit(0)
#TODO tengo que hacer un while True para cada lista


if __name__ == "__main__":
    mezcla()