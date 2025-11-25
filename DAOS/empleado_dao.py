# Este módulo contiene las funciones de acceso a datos (DAO) para la tabla 'empleado'.
# Proporciona una interfaz para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar)
# sobre los registros de empleados en la base de datos.

from DAOS.db import conectar
from decimal import Decimal

def registrar_empleado(datos):
    """
    Inserta un nuevo registro de empleado en la base de datos.

    Args:
        datos (dict): Un diccionario con los datos del empleado.
                      Las llaves deben coincidir con las columnas de la tabla 'empleado'.
    """
    conn = conectar()
    cur = conn.cursor()
    sql = """
    INSERT INTO empleado (nombre, direccion, telefono, fecha_nac, sexo, sueldo, turno, contrasena)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    # Ejecuta la consulta SQL, usando 'or None' para manejar valores de fecha opcionales.
    cur.execute(sql, (datos['nombre'], datos['direccion'], datos['telefono'], datos['fecha_nac'] or None, datos['sexo'], datos['sueldo'], datos['turno'], datos['contrasena']))
    conn.commit()
    cur.close()
    conn.close()

def mostrar_empleado_por_id(id_val):
    """
    Busca y devuelve un empleado por su código (ID).

    Args:
        id_val (str or int): El ID del empleado a buscar.

    Returns:
        tuple or None: Una tupla con los datos del empleado si se encuentra, de lo contrario None.
    """
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT codigo, nombre, direccion, telefono, fecha_nac, sexo, sueldo, turno, contrasena FROM empleado WHERE codigo = %s", (int(id_val),))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def mostrar_todos_los_empleados():
    """
    Devuelve todos los registros de empleados de la base de datos, ordenados por código.

    Returns:
        list: Una lista de tuplas, donde cada tupla representa un empleado.
    """
    conn = conectar()
    cur = conn.cursor()
    # No se selecciona la contraseña por razones de seguridad al mostrar listas.
    cur.execute("SELECT codigo, nombre, direccion, telefono, fecha_nac, sexo, sueldo, turno FROM empleado ORDER BY codigo;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def modificar_empleado(datos):
    """
    Actualiza los datos de un empleado existente en la base de datos.

    Args:
        datos (dict): Un diccionario con los datos actualizados del empleado.
                      Debe incluir 'codigo' para identificar el registro a modificar.
    """
    conn = conectar()
    cur = conn.cursor()
    sql = """
    UPDATE empleado
    SET nombre=%s, direccion=%s, telefono=%s, fecha_nac=%s, sexo=%s, sueldo=%s, turno=%s, contrasena=%s
    WHERE codigo=%s
    """
    cur.execute(sql, (datos['nombre'], datos['direccion'], datos['telefono'], datos['fecha_nac'], datos['sexo'], datos['sueldo'], datos['turno'], datos['contrasena'], datos['codigo']))
    conn.commit()
    cur.close()
    conn.close()

def eliminar_empleado(id_val):
    """
    Elimina un empleado de la base de datos por su código (ID).

    Args:
        id_val (str or int): El ID del empleado a eliminar.

    Returns:
        int: El número de filas eliminadas (debería ser 0 o 1).
    """
    conn = conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM empleado WHERE codigo = %s", (int(id_val),))
    cambios = cur.rowcount
    conn.commit()
    cur.close()
    conn.close()
    return cambios
