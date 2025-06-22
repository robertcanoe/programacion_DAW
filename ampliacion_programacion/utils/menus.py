class Menu:
    def __init__(self, title, options):
        self.__title = title
        self.__options = options

    def choose(self):
        self.__print_menu()
        return self.__chosen_option()

    def __print_menu(self):
        numbered_options = [f"{i+1}. {opt}" for i, opt in enumerate(self.__options)]
        content_width = max(len(self.__title), *(len(opt) for opt in numbered_options))
        box_width = content_width + 8
        top_border = "═" * box_width
        sep_border = "─" * box_width
        print(f"\n╔{top_border}╗")
        print(self._center_line(self.__title, box_width))
        print(f"╠{sep_border}╣")
        for opt in numbered_options:
            print(self._left_line(opt, box_width))
        print(f"╚{top_border}╝")

    def __chosen_option(self):
        while True:
            try:
                option = int(input("Elige una opción: "))
                if 1 <= option <= len(self.__options):
                    return option
                else:
                    print(f"Elige un número entre 1 y {len(self.__options)}.")
            except ValueError:
                print("Introduce un número válido.")

    def _center_line(self, text, width):
        total_padding = width - len(text)
        left = total_padding // 2
        right = total_padding - left
        return f"║{' ' * left}{text}{' ' * right}║"

    def _left_line(self, text, width):
        padding = width - len(text)
        return f"║ {text}{' ' * (padding - 1)}║"

main_menu = Menu(
    "BANCO PYTHON - MENÚ PRINCIPAL",
    ["Gestión de clientes", "Gestión de cuentas", "Movimientos", "Salir"]
)

customer_menu = Menu(
    "GESTIÓN DE CLIENTES",
    [
        "Registrar cliente",
        "Modificar cliente",
        "Dar de baja cliente",
        "Reactivar cliente",
        "Listar clientes",
        "Volver"
    ]
)

account_menu = Menu(
    "GESTIÓN DE CUENTAS",
    [
        "Crear cuenta corriente",
        "Reabrir cuenta",
        "Cerrar cuenta",
        "Consultar saldo",
        "Depositar dinero",
        "Retirar dinero",
        "Transferir dinero",
        "Listar cuentas",
        "Volver"
    ]
)

movements_menu = Menu(
    "GESTIÓN DE MOVIMIENTOS",
    [
        "Ver ingresos",
        "Ver retiros",
        "Ver transferencias",
        "Ver movimientos entre fechas",
        "Volver"
    ]
)
