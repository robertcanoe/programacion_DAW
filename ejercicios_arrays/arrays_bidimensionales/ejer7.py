students = []

modules = ["PROGRAMACIÓN", "LENGUAJE DE MARCAS", "BASES DE DATOS", "SISTEMAS INFORMÁTICOS"]


def add_student():
    while True:
        name = input("Introduce el nombre y apellidos del alumno (o deja vacío para terminar): ")
        if not name:
            break
        grades = [name]
        for module in modules:
            while True:
                try:
                    grade = float(input(f"Introduce la nota para {module}: "))
                    if grade < 0 or grade > 10:
                        print("La nota debe estar entre 0 y 10.")
                        continue
                    grades.append(grade)
                    break
                except ValueError:
                    print("Introduce un número válido.")
        students.append(grades)


def print_all_grades():
    if not students:
        print("No hay datos para mostrar.")
        return
    for student in students:
        print(f"{student[0]}:")
        for i, grade in enumerate(student[1:], 1):
            print(f"  {modules[i - 1]}: {grade}")
        print()


def print_student_grades():
    name = input("Introduce el nombre y apellidos del alumno: ")
    for student in students:
        if student[0] == name:
            print(f"Calificaciones de {name}:")
            for i, grade in enumerate(student[1:], 1):
                print(f"  {modules[i - 1]}: {grade}")
            return
    print("No se encontró al alumno.")


def calculate_module_average():
    module = input("Introduce el nombre del módulo: ").upper()
    if module in modules:
        index = modules.index(module) + 1
        total = sum(student[index] for student in students)
        count = len(students)
        if count > 0:
            print(f"La nota media de {module} es {total / count:.2f}")
        else:
            print("No hay datos para calcular la media.")
    else:
        print("Módulo no válido.")


def find_module_max():
    module = input("Introduce el nombre del módulo: ").upper()
    if module in modules:
        index = modules.index(module) + 1
        max_grade = float('-inf')
        max_student = ""
        for student in students:
            if student[index] > max_grade:
                max_grade = student[index]
                max_student = student[0]
        if students:
            print(f"La nota más alta de {module} es {max_grade}, obtenida por: {max_student}.")
        else:
            print("No hay datos disponibles para este módulo.")
    else:
        print("Módulo no válido.")


def find_module_min():
    module = input("Introduce el nombre del módulo: ").upper()
    if module in modules:
        index = modules.index(module) + 1
        min_grade = float('inf')
        min_student = ""
        for student in students:
            if student[index] < min_grade:
                min_grade = student[index]
                min_student = student[0]
        if students:
            print(f"La nota más baja de {module} es {min_grade}, obtenida por: {min_student}.")
        else:
            print("No hay datos disponibles para este módulo.")
    else:
        print("Módulo no válido.")


def sort_module_grades():
    module = input("Introduce el nombre del módulo: ").upper()
    if module in modules:
        index = modules.index(module) + 1

        # Función de comparación para ordenar
        def sort_key(student):
            return student[index]

        sorted_students = sorted(students, key=sort_key, reverse=True)
        print(f"Notas ordenadas de mayor a menor en {module}:")
        for student in sorted_students:
            print(f"{student[0]}: {student[index]}")
    else:
        print("Módulo no válido.")


# Menú principal del programa
while True:
    print("\nMenú:")
    print("1. Añadir alumnos y calificaciones")
    print("2. Ver todas las calificaciones")
    print("3. Ver calificaciones de un alumno")
    print("4. Calcular media de un módulo")
    print("5. Nota máxima de un módulo")
    print("6. Nota más baja de un módulo")
    print("7. Ordenar notas de un módulo")
    print("8. Salir")

    option = input("Selecciona una opción: ").strip()
    if option == "1":
        add_student()
    elif option == "2":
        print_all_grades()
    elif option == "3":
        print_student_grades()
    elif option == "4":
        calculate_module_average()
    elif option == "5":
        find_module_max()
    elif option == "6":
        find_module_min()
    elif option == "7":
        sort_module_grades()
    elif option == "8":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")