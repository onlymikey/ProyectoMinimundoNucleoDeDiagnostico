from DAOS.db import conectar

def registrar_doctor(datos):
    conn = conectar()
    cur = conn.cursor()
    sql = """
    INSERT INTO doctores (nombre, direccion, telefono, fecha_nac, sexo, especialidad, contrasena)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cur.execute(sql, (datos['nombre'], datos['direccion'], datos['telefono'], datos['fecha_nac'] or None, datos['sexo'], datos['especialidad'], datos['contrasena']))
    conn.commit()
    cur.close()
    conn.close()

def mostrar_doctor_por_id(id_val):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT codigo, nombre, direccion, telefono, fecha_nac, sexo, especialidad, contrasena FROM doctores WHERE codigo = %s", (int(id_val),))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def mostrar_todos_los_doctores():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT codigo, nombre, direccion, telefono, fecha_nac, sexo, especialidad FROM doctores ORDER BY codigo;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def modificar_doctor(datos):
    conn = conectar()
    cur = conn.cursor()
    sql = """
    UPDATE doctores
    SET nombre=%s, direccion=%s, telefono=%s, fecha_nac=%s, sexo=%s, especialidad=%s, contrasena=%s
    WHERE codigo=%s
    """
    cur.execute(sql, (datos['nombre'], datos['direccion'], datos['telefono'], datos['fecha_nac'], datos['sexo'], datos['especialidad'], datos['contrasena'], datos['codigo']))
    conn.commit()
    cur.close()
    conn.close()

def eliminar_doctor(id_val):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM doctores WHERE codigo = %s", (int(id_val),))
    cambios = cur.rowcount
    conn.commit()
    cur.close()
    conn.close()
    return cambios
