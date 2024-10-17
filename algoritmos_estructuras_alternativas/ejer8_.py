"""
Programa que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor o igual a dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.

Autor: Roberto Cano Estévez

Fecha: 16/10/2024
"""
print("Este programa evaluará si tu solicitud es ACEPTADA, POSIBLE o NO ACEPTADA.")
print("Por favor, introduce tu nota, tu edad y tu sexo para continuar.")
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")

note = float(input("dime tu nota: "))
year = int(input("dime tu edad: "))
sex = input("dime tu sexo: ")

if note >= 5 and year >= 18:
    if sex == "F":
        print("ACEPTADA")
    else:
        if sex == "M":
            print("POSIBLE")
else:
    print("NO ACEPTADA")
