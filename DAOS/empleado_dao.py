from DAOS.db import conectar
from decimal import Decimal

def registrar_empleado(datos):
    conn = conectar()
    cur = conn.cursor()
    sql = """
    INSERT INTO empleado (nombre, direccion, telefono, fecha_nac, sexo, sueldo, turno, contrasena)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cur.execute(sql, (datos['nombre'], datos['direccion'], datos['telefono'], datos['fecha_nac'] or None, datos['sexo'], datos['sueldo'], datos['turno'], datos['contrasena']))
    conn.commit()
    cur.close()
    conn.close()

def mostrar_empleado_por_id(id_val):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT codigo, nombre, direccion, telefono, fecha_nac, sexo, sueldo, turno, contrasena FROM empleado WHERE codigo = %s", (int(id_val),))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def mostrar_todos_los_empleados():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT codigo, nombre, direccion, telefono, fecha_nac, sexo, sueldo, turno FROM empleado ORDER BY codigo;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def modificar_empleado(datos):
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
    conn = conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM empleado WHERE codigo = %s", (int(id_val),))
    cambios = cur.rowcount
    conn.commit()
    cur.close()
    conn.close()
    return cambios
