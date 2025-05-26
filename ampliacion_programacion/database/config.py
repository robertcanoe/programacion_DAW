from dataclasses import dataclass

@dataclass
class DatabaseConfig:
    host: str = "localhost"
    user: str = "root"
    password: str = "rootRCE@"  
    database: str = "ejemplo_dao"

# Configuración de la base de datos
db_config = DatabaseConfig()
