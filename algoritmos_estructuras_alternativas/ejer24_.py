"""
Diseña un programa que, dado un número real que debe representar la calificación numérica de un examen, proporcione la calificación cualitativa correspondiente al número dado. La calificación cualitativa será una de las siguientes: «Suspenso» (nota menor que 5), «Aprobado» (nota mayor o igual que 5, pero menor que 7), «Notable» (nota mayor o igual que 7, pero menor que 9), «Sobresaliente» (nota mayor o igual que 9, pero menor que 10), «Matrícula de Honor» (nota 10).

Autor: Roberto Cano Estévez
Fecha: 23/10/2024
"""
print("Este programa representa de una nota la calificación cualitativa")
print("----------------------------------------------------------------")

note = float(input("Proporciona la calificación: "))

if note < 5:
    print("Suspenso")
elif note >=5 and note <7:
    print("Aprobado")
elif note >=7 and note <9:
    print("Notable")
elif note >= 9 and note <=10:
    print("Sobresaliente")
elif note == 10:
    print("Matrícula de honor")

else:
    print("La calificación proporcionada no es válida")