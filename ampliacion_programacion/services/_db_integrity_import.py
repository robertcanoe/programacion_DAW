# Este archivo solo existe para importar la excepción IntegrityError correctamente
try:
    from mysql.connector.errors import IntegrityError
except ImportError:
    try:
        from pymysql.err import IntegrityError
    except ImportError:
        IntegrityError = Exception
