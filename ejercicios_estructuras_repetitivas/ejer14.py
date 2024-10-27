"""
Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.

Autor: Roberto Cano Estévez

Fecha: 26/10/2024
"""

print("Este programa verifica si una cadena contiene una subcadena dada.")
print("----------------------------------------------------------------")

main_text = input("Introduce la cadena principal: ")
sub_text = input("Introduce la subcadena a buscar: ")

if sub_text in main_text:
    print("La subcadena está presente en la cadena.")
else:
    print("La subcadena no está presente en la cadena.")
