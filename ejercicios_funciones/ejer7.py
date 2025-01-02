"""
Define la función mezcla de forma que tome dos listas como parámetros y devuelve otra que es el resultado de mezclar los números de ambos de forma alterna, se coge un número de a, luego de b, luego de a, etc. Los arrays a y b pueden tener longitudes diferentes; por tanto, si se terminan los números de un array se terminan de coger todos los que quedan del otro.

Ejemplos:

Si a = [8, 9, 0] y b = [1, 2, 3], mezcla(a, b) devuelve [8, 1, 9, 2, 0, 3 ]

Si a = [4, 3] y b = [7, 8, 9, 10], mezcla(a, b) devuelve [4, 7, 3, 8, 9, 10]

Si a = [8, 9, 0, 3] y b = [1], mezcla(a, b) devuelve [8, 1, 9, 0, 3]

Si a = [ ] y b = [1, 2, 3], mezcla(a, b) devuelve [1, 2, 3]
"""

def merge(list1, list2):
    result = []
    min_length = min(len(list1), len(list2))
    
    for i in range(min_length):
        result.append(list1[i])
        result.append(list2[i])
    
    result.extend(list1[min_length:])
    result.extend(list2[min_length:])
    
    return result

def main():
    list1 = input("Enter the numbers for list 1 separated by commas (e.j., 1,2,3): ")
    list2 = input("Enter the numbers for list 2 separated by commas (e.j., 4,5,6): ")
    
    list1 = [int(x) for x in list1.split(",")] if list1 else []
    list2 = [int(x) for x in list2.split(",")] if list2 else []
    
    result = merge(list1, list2)
    
    print("The merged list is:", result)

if __name__ == "__main__":
    main()

