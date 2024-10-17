# las tres calificaciones parciales
grade1 = float(input("Introduce la primera calificación parcial: "))
grade2 = float(input("Introduce la segunda calificación parcial: "))
grade3 = float(input("Introduce la tercera calificación parcial: "))

# la calificación del examen final y del trabajo final
final_exam_grade = float(input("Introduce la calificación del examen final: "))
final_project_grade = float(input("Introduce la calificación del trabajo final: "))

# Calcular el promedio de las calificaciones parciales
average_partial_grades = (grade1 + grade2 + grade3) / 3

# Calcular la calificación final con los porcentajes dados
final_grade = (average_partial_grades * 0.55) + (final_exam_grade * 0.30) + (final_project_grade * 0.15)

# Mostrar el resultado
print(f"\nLa calificación final en la materia de Algoritmos es: {final_grade:.2f}")

