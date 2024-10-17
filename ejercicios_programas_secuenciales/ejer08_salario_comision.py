base_salary = float(input("Ingrese el sueldo base del vendedor: "))
sales = float(input("Ingrese el total de ventas del vendedor: "))

commission = sales * 0.10

total_to_receive = base_salary + commission

print(f"El vendedor recibirá una comisión de: {commission:.2f}")
print(f"El total a recibir en el mes es: {total_to_receive:.2f}")
