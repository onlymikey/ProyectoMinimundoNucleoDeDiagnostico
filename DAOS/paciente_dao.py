# Este módulo contiene las funciones de acceso a datos (DAO) para la tabla 'pacientes'.
# Se encarga de las operaciones CRUD directas con la base de datos para los registros de pacientes.

from DAOS.db import conectar
from decimal import Decimal

def registrar_paciente(datos):
    """
    Inserta un nuevo paciente en la tabla 'pacientes'.

    Args:
        datos (dict): Diccionario con los datos del paciente a registrar.
    """
    conn = conectar()
    cur = conn.cursor()
    sql = """
    INSERT INTO pacientes (nombre, direccion, telefono, fecha_nac, sexo, edad, estatura)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    # Ejecuta el comando SQL con los datos del paciente.
    cur.execute(sql, (datos['nombre'], datos['direccion'], datos['telefono'], datos['fecha_nac'] or None, datos['sexo'], datos['edad'], datos['estatura']))
    conn.commit()
    cur.close()
    conn.close()

def mostrar_paciente_por_id(id_val):
    """
    Busca y retorna un paciente por su ID.

    Args:
        id_val (str or int): El ID del paciente a buscar.

    Returns:
        tuple or None: Una tupla con los datos del paciente o None si no se encuentra.
    """
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT codigo, nombre, direccion, telefono, fecha_nac, sexo, edad, estatura FROM pacientes WHERE codigo = %s", (int(id_val),))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def mostrar_todos_los_pacientes():
    """
    Retorna todos los pacientes de la base de datos, ordenados por código.

    Returns:
        list: Una lista de tuplas, donde cada tupla es un paciente.
    """
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT codigo, nombre, direccion, telefono, fecha_nac, sexo, edad, estatura FROM pacientes ORDER BY codigo;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def modificar_paciente(datos):
    """
    Actualiza los datos de un paciente existente en la base de datos.

    Args:
        datos (dict): Diccionario con los datos actualizados del paciente, incluyendo el 'codigo'.
    """
    conn = conectar()
    cur = conn.cursor()
    sql = """
    UPDATE pacientes
    SET nombre=%s, direccion=%s, telefono=%s, fecha_nac=%s, sexo=%s, edad=%s, estatura=%s
    WHERE codigo=%s
    """
    cur.execute(sql, (datos['nombre'], datos['direccion'], datos['telefono'], datos['fecha_nac'], datos['sexo'], datos['edad'], datos['estatura'], datos['codigo']))
    conn.commit()
    cur.close()
    conn.close()

def eliminar_paciente(id_val):
    """
    Elimina un paciente de la base de datos por su ID.

    Args:
        id_val (str or int): El ID del paciente a eliminar.

    Returns:
        int: El número de filas afectadas por la operación (0 o 1).
    """
    conn = conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM pacientes WHERE codigo = %s", (int(id_val),))
    cambios = cur.rowcount
    conn.commit()
    cur.close()
    conn.close()
    return cambios
