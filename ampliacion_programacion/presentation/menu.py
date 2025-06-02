from datetime import datetime
from services.banco_service import BancoService
from exceptions.validation_exceptions import ValidationError

class Menu:
    def __init__(self):
        self.banco_service = BancoService()

    def mostrar_menu_principal(self):
        while True:
            print("\n=== SISTEMA BANCARIO ===")
            print("1. Gestión de Clientes")
            print("2. Gestión de Cuentas")
            print("3. Gestión de Cuenta Individual")
            print("4. Salir")
            
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                self.menu_clientes()
            elif opcion == "2":
                self.menu_cuentas()
            elif opcion == "3":
                self.menu_cuenta_individual()
            elif opcion == "4":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida")

    def menu_clientes(self):
        while True:
            print("\n=== GESTIÓN DE CLIENTES ===")
            print("1. Alta de cliente")
            print("2. Baja de cliente")
            print("3. Modificación de cliente")
            print("4. Volver al menú principal")
            
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                self.alta_cliente()
            elif opcion == "2":
                self.baja_cliente()
            elif opcion == "3":
                self.modificacion_cliente()
            elif opcion == "4":
                break
            else:
                print("Opción no válida")

    def menu_cuentas(self):
        while True:
            print("\n=== GESTIÓN DE CUENTAS ===")
            print("1. Alta de cuenta")
            print("2. Baja de cuenta")
            print("3. Modificación de cuenta")
            print("4. Listar cuentas")
            print("5. Realizar ingreso")
            print("6. Realizar salida")
            print("7. Realizar transferencia")
            print("8. Volver al menú principal")
            
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                self.alta_cuenta()
            elif opcion == "2":
                self.baja_cuenta()
            elif opcion == "3":
                self.modificacion_cuenta()
            elif opcion == "4":
                self.listar_cuentas()
            elif opcion == "5":
                self.realizar_ingreso()
            elif opcion == "6":
                self.realizar_salida()
            elif opcion == "7":
                self.realizar_transferencia()
            elif opcion == "8":
                break
            else:
                print("Opción no válida")

    def menu_cuenta_individual(self):
        numero_cuenta = input("Ingrese el número de cuenta: ")
        try:
            numero_cuenta = int(numero_cuenta)
        except ValueError:
            print("Número de cuenta inválido")
            return

        while True:
            print(f"\n=== GESTIÓN DE CUENTA {numero_cuenta} ===")
            print("1. Ver saldo")
            print("2. Listar movimientos")
            print("3. Listar movimientos entre fechas")
            print("4. Realizar transferencia")
            print("5. Volver al menú principal")
            
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                self.ver_saldo(numero_cuenta)
            elif opcion == "2":
                self.listar_movimientos(numero_cuenta)
            elif opcion == "3":
                self.listar_movimientos_fechas(numero_cuenta)
            elif opcion == "4":
                self.realizar_transferencia_desde_cuenta(numero_cuenta)
            elif opcion == "5":
                break
            else:
                print("Opción no válida")

    def _validar_entrada(self, mensaje: str, validacion_func, *args) -> str:
        #código refactorizado con *args
        while True:
            try:
                valor = input(mensaje)
                validacion_func(valor, *args)
                return valor
            except ValidationError as e:
                print(f"Error: {e}")

    def alta_cliente(self):
        print("\n=== ALTA DE CLIENTE ===")
        from validators.data_validators import DataValidator

        dni = self._validar_entrada("DNI: ", DataValidator.validate_dni)
        nombre = self._validar_entrada("Nombre: ", DataValidator.validate_required_field, "Nombre")
        telefono = self._validar_entrada("Teléfono: ", DataValidator.validate_phone)
        direccion = self._validar_entrada("Dirección: ", DataValidator.validate_required_field, "Dirección")

        if self.banco_service.crear_cliente(dni, nombre, telefono, direccion):
            print("Cliente creado correctamente")
        else:
            print("Error al crear el cliente")

    def baja_cliente(self):
        print("\n=== BAJA DE CLIENTE ===")
        dni = input("DNI del cliente a eliminar: ")
        exito, mensaje = self.banco_service.eliminar_cliente(dni)
        print(mensaje)

    def modificacion_cliente(self):
        print("\n=== MODIFICACIÓN DE CLIENTE ===")
        dni = input("DNI del cliente a modificar: ")
        cliente = self.banco_service.obtener_cliente(dni)
        
        if not cliente:
            print("Cliente no encontrado")
            return

        print("Ingrese los nuevos datos (deje en blanco para mantener el valor actual):")
        nombre = input(f"Nombre [{cliente.nombre}]: ") or cliente.nombre
        telefono = input(f"Teléfono [{cliente.telefono}]: ") or cliente.telefono
        direccion = input(f"Dirección [{cliente.direccion}]: ") or cliente.direccion

        if self.banco_service.modificar_cliente(dni, nombre, telefono, direccion):
            print("Cliente modificado correctamente")
        else:
            print("Error al modificar el cliente")

    # Funciones auxiliares para el menú de cuentas
    def alta_cuenta(self):
        print("\n=== ALTA DE CUENTA ===")
        dni = input("DNI del cliente: ")
        exito, mensaje, numero = self.banco_service.crear_cuenta(dni)
        if exito:
            print(f"{mensaje} - Número de cuenta: {numero}")
        else:
            print(mensaje)

    def baja_cuenta(self):
        print("\n=== BAJA DE CUENTA ===")
        try:
            numero = int(input("Número de cuenta: "))
            exito, mensaje = self.banco_service.dar_baja_cuenta(numero)
            print(mensaje)
        except ValueError:
            print("Número de cuenta inválido")

    def modificacion_cuenta(self):
        print("\n=== MODIFICACIÓN DE CUENTA ===")
        numero = int(input("Número de cuenta: "))
        cuenta = self.banco_service.obtener_cuenta(numero)
        
        if not cuenta:
            print("Cuenta no encontrada")
            return

        print("Ingrese los nuevos datos (deje en blanco para mantener el valor actual):")
        saldo = input(f"Saldo [{cuenta.saldo}]: ") or cuenta.saldo
        activa = input(f"Activa [{cuenta.activa}]: ") or cuenta.activa

        if self.banco_service.modificar_cuenta(numero, saldo, activa):
            print("Cuenta modificada correctamente")
        else:
            print("Error al modificar la cuenta")

    def realizar_ingreso(self):
        print("\n=== REALIZAR INGRESO ===")
        from validators.data_validators import DataValidator
        from exceptions.validation_exceptions import ValidationError

        # Validar número de cuenta
        while True:
            try:
                numero_str = input("Número de cuenta: ")
                DataValidator.validate_account_number(numero_str)
                numero = int(numero_str)
                break
            except (ValidationError, ValueError) as e:
                print(f"Error: Número de cuenta inválido")

        # Validar importe
        while True:
            try:
                importe_str = input("Importe: ")
                try:
                    importe = float(importe_str)
                    DataValidator.validate_amount(importe)
                    break
                except ValueError:
                    print("Error: El importe debe ser un número")
            except ValidationError as e:
                print(f"Error: {e}")

        # Validar concepto
        while True:
            try:
                concepto = input("Concepto: ")
                DataValidator.validate_required_field(concepto, "Concepto")
                break
            except ValidationError as e:
                print(f"Error: {e}")

        exito, mensaje = self.banco_service.realizar_ingreso(numero, importe, concepto)
        print(mensaje)

    def realizar_salida(self):
        print("\n=== REALIZAR SALIDA ===")
        from validators.data_validators import DataValidator
        from exceptions.validation_exceptions import ValidationError

        # Validar número de cuenta
        while True:
            try:
                numero_str = input("Número de cuenta: ")
                DataValidator.validate_account_number(numero_str)
                numero = int(numero_str)
                break
            except (ValidationError, ValueError) as e:
                print(f"Error: Número de cuenta inválido")

        # Validar importe
        while True:
            try:
                importe_str = input("Importe: ")
                try:
                    importe = float(importe_str)
                    DataValidator.validate_amount(importe)
                    break
                except ValueError:
                    print("Error: El importe debe ser un número")
            except ValidationError as e:
                print(f"Error: {e}")

        # Validar concepto
        while True:
            try:
                concepto = input("Concepto: ")
                DataValidator.validate_required_field(concepto, "Concepto")
                break
            except ValidationError as e:
                print(f"Error: {e}")

        exito, mensaje = self.banco_service.realizar_salida(numero, importe, concepto)
        print(mensaje)

    def realizar_transferencia(self):
        print("\n=== REALIZAR TRANSFERENCIA ===")
        from validators.data_validators import DataValidator
        from exceptions.validation_exceptions import ValidationError

        # Validar cuenta origen
        while True:
            try:
                origen_str = input("Número de cuenta origen: ")
                DataValidator.validate_account_number(origen_str)
                origen = int(origen_str)
                break
            except (ValidationError, ValueError) as e:
                print(f"Error: Número de cuenta origen inválido")

        # Validar cuenta destino
        while True:
            try:
                destino_str = input("Número de cuenta destino: ")
                DataValidator.validate_account_number(destino_str)
                destino = int(destino_str)
                if destino == origen:
                    print("Error: La cuenta destino no puede ser igual a la cuenta origen")
                    continue
                break
            except (ValidationError, ValueError) as e:
                print(f"Error: Número de cuenta destino inválido")

        # Validar importe
        while True:
            try:
                importe_str = input("Importe: ")
                try:
                    importe = float(importe_str)
                    DataValidator.validate_amount(importe)
                    break
                except ValueError:
                    print("Error: El importe debe ser un número")
            except ValidationError as e:
                print(f"Error: {e}")

        # Validar concepto
        while True:
            try:
                concepto = input("Concepto: ")
                DataValidator.validate_required_field(concepto, "Concepto")
                break
            except ValidationError as e:
                print(f"Error: {e}")

        exito, mensaje = self.banco_service.realizar_transferencia(origen, destino, importe, concepto)
        print(mensaje)

    def realizar_transferencia_desde_cuenta(self, cuenta_origen):
        print("\n=== REALIZAR TRANSFERENCIA ===")
        try:
            destino = int(input("Número de cuenta destino: "))
            importe = float(input("Importe: "))
            concepto = input("Concepto: ")
            exito, mensaje = self.banco_service.realizar_transferencia(cuenta_origen, destino, importe, concepto)
            print(mensaje)
        except ValueError:
            print("Datos inválidos")

    def listar_cuentas(self):
        print("\n=== LISTADO DE CUENTAS ===")
        cuentas = self.banco_service.obtener_cuentas()
        if cuentas:
            for cuenta in cuentas:
                estado = "Activa" if cuenta.activa else "Inactiva"
                print(f"Número: {cuenta.numero}, Saldo: {cuenta.saldo}€, Estado: {estado}")
        else:
            print("No hay cuentas registradas")

    # Funciones auxiliares para el menú de cuenta individual
    def ver_saldo(self, numero_cuenta):
        saldo = self.banco_service.obtener_saldo(numero_cuenta)
        print(f"\nSaldo actual: {saldo:.2f}€")

    def listar_movimientos(self, numero_cuenta):
        movimientos = self.banco_service.obtener_movimientos(numero_cuenta)
        self._mostrar_movimientos(movimientos)

    def listar_movimientos_fechas(self, numero_cuenta):
        print("\nIngrese el rango de fechas (formato: dd/mm/yyyy)")
        try:
            fecha_inicio = datetime.strptime(input("Fecha inicio: "), "%d/%m/%Y")
            fecha_fin = datetime.strptime(input("Fecha fin: "), "%d/%m/%Y")
            movimientos = self.banco_service.obtener_movimientos(numero_cuenta, fecha_inicio, fecha_fin)
            self._mostrar_movimientos(movimientos)
        except ValueError:
            print("Formato de fecha inválido")

    def _mostrar_movimientos(self, movimientos):
        if not movimientos:
            print("\nNo hay movimientos para mostrar")
            return

        print("\n=== LISTADO DE MOVIMIENTOS ===")
        for mov in movimientos:
            fecha = mov.fecha_hora.strftime("%d/%m/%Y %H:%M:%S")
            if mov.tipo in ["ingreso", "transferencia_recibida"]:
                signo = "+"
            else:
                signo = "-"
            
            print(f"Fecha: {fecha}")
            print(f"Tipo: {mov.tipo}")
            print(f"Importe: {signo}{mov.importe:.2f}€")
            if mov.numero_cuenta_transferencia:
                print(f"Cuenta {'destino' if 'enviada' in mov.tipo else 'origen'}: {mov.numero_cuenta_transferencia}")
            print(f"Concepto: {mov.concepto}")
            print("-" * 40)
