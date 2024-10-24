"""
Realiza un programa que pida cinco números enteros y diga cuál es el mayor.

Autor: Roberto Cano Estévez
Fecha: 23/10/2024
"""
print("Este programa te dice cual de los 5 números es mayor.")
print("-----------------------------------------------------")

n1 = int(input("Dime el primer numero: "))
n2 = int(input("Dime el segundo numero: "))
n3 = int(input("Dime el tercer numero: "))
n4 = int(input("Dime el quarto numero: "))
n5 = int(input("Dime el quinto numero: "))

if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    print("El mayor es ", n1)

elif n2 > n3 and n2 > n4 and n2 > n5:
    print("El mayor es ", n2)

elif n3 > n4 and n3 > n5:
    print("El mayor es ", n3)

elif n4 > n5:
    print("El mayor es ", n4)

else:
    print("El mayor es ", n5)

"""
Esto se podría simplificar usando la función max(), pero como no se si puedo usarlo no lo pongo pero seria una cosa asi:
max(n1, n2, n3, n4, n5)

"""