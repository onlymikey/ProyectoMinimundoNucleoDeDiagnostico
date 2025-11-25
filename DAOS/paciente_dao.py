from DAOS.db import conectar
from decimal import Decimal

def registrar_paciente(datos):
    conn = conectar()
    cur = conn.cursor()
    sql = """
    INSERT INTO pacientes (nombre, direccion, telefono, fecha_nac, sexo, edad, estatura)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cur.execute(sql, (datos['nombre'], datos['direccion'], datos['telefono'], datos['fecha_nac'] or None, datos['sexo'], datos['edad'], datos['estatura']))
    conn.commit()
    cur.close()
    conn.close()

def mostrar_paciente_por_id(id_val):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT codigo, nombre, direccion, telefono, fecha_nac, sexo, edad, estatura FROM pacientes WHERE codigo = %s", (int(id_val),))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def mostrar_todos_los_pacientes():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT codigo, nombre, direccion, telefono, fecha_nac, sexo, edad, estatura FROM pacientes ORDER BY codigo;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def modificar_paciente(datos):
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
    conn = conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM pacientes WHERE codigo = %s", (int(id_val),))
    cambios = cur.rowcount
    conn.commit()
    cur.close()
    conn.close()
    return cambios
