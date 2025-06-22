# Sistema de Gestión Bancaria en Python

Este proyecto es una aplicación de consola en Python para la gestión de clientes, cuentas y transacciones bancarias. Permite crear, modificar y eliminar clientes, gestionar cuentas bancarias y registrar movimientos, todo conectado a una base de datos MySQL.

## Características principales
- Alta, modificación y baja de clientes
- Gestión de cuentas bancarias (apertura, cierre, consulta)
- Registro y consulta de movimientos/transferencias
- Menús interactivos en consola
- Acceso a base de datos MySQL mediante `mysql-connector-python`
- Configuración sencilla mediante archivo `.env`

## Requisitos
- Python 3.10 o superior
- MySQL Server

### Dependencias Python
Instalables con:
```bash
pip install -r requirements.txt
```

## Configuración
1. **Clona el repositorio**
2. **Crea un archivo `.env`** en la raíz del proyecto con las siguientes variables:
   ```env
   HOST=localhost
   USER=tu_usuario_mysql
   PASSWORD=tu_contraseña_mysql
   DATABASE=nombre_base_datos
   ```
3. **Inicializa la base de datos** ejecutando el script correspondiente (ver notas abajo).

## Uso
Ejecuta la aplicación principal:
```bash
python main.py
```
Sigue los menús interactivos para gestionar clientes, cuentas y movimientos.

## Estructura del proyecto
```
├── accounts/           # Lógica y modelos de cuentas bancarias
├── clients/            # Lógica y modelos de clientes
├── db/                 # Configuración y utilidades de la base de datos
├── errors/             # Gestión de errores personalizados
├── main.py             # Punto de entrada de la aplicación
├── requirements.txt    # Dependencias Python
├── services/           # Servicios de negocio (clientes, cuentas, transacciones)
├── transactions/       # Lógica y modelos de movimientos/transferencias
├── utils/              # Utilidades y menús
```

## Notas importantes
- **Cambio reciente:** El modelo de cliente ahora utiliza los campos `nombres` y `apellidos` en vez de `nombre`.
- **Recuerda**: Si modificas la estructura de la base de datos, ejecuta el script de inicialización (`init_db.py` o equivalente) para evitar errores.
- El archivo `.env` **no debe subirse al repositorio** por seguridad.

## Créditos
Desarrollado por Robert Cano para prácticas de ampliación de programación.
