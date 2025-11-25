import psycopg2

# ---------------------- CONEXIÓN ----------------------
def conectar():
    return psycopg2.connect(
        host="localhost",
        dbname="nucleo_diagnostico",
        user="postgres",
        password="12345"
    )
