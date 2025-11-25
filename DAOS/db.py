# Este módulo proporciona una función centralizada para conectarse a la base de datos PostgreSQL.
# Abstrae los detalles de la conexión para que otros módulos (los DAOs) no necesiten
# conocer las credenciales o la configuración específica de la base de datos.

import psycopg2

# ---------------------- CONEXIÓN ----------------------
def conectar():
    """
    Establece y devuelve una conexión con la base de datos 'nucleo_diagnostico'.

    Utiliza credenciales predefinidas para conectarse a una instancia local de PostgreSQL.
    ADVERTENCIA: En una aplicación de producción, las credenciales nunca deben estar
    hardcodeadas en el código. Deberían gestionarse de forma segura utilizando
    variables de entorno, un archivo de configuración no versionado o un servicio de gestión de secretos.

    Returns:
        psycopg2.connection: Un objeto de conexión a la base de datos.
    """
    return psycopg2.connect(
        host="localhost",
        dbname="nucleo_diagnostico",
        user="postgres",
        password="12345"  # ¡Esto es inseguro para producción!
    )
