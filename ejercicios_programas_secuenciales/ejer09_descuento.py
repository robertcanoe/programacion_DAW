# el precio original y el descuentooriginal_price = float(input("Ingrese el precio original: "))discount_percentage = float(input("Ingrese el porcentaje de descuento: "))# calcular el descuentodiscount = original_price * (discount_percentage / 100)# calcular el precio finalfinal_price = original_price - discount# resultadoprint(f"El descuento es: {discount:.2f}")print(f"El precio final después del descuento es: {final_price:.2f}")