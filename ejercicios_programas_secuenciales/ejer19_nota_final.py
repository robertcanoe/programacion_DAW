# "Escribir un programa para calcular la nota final de un examen, considerando que:
# cada respuesta correcta suma 5 puntos, cada respuesta incorrecta resta 1 punto, y cada respuesta en blanco suma 0 puntos. Imprime la puntuación total obtenida."
# Hecho por: Roberto Cano Estévez
# Fecha: 14/10/2024

correct = int(input("Introduce el número de respuestas correctas: "))
incorrect = int(input("Introduce el número de respuestas incorrectas: "))
white = int(input("Introduce el número de respuestas en blanco: "))

note = correct * 5 + incorrect * -1 + white * 0

print(f"La nota final es: {note}")


