# Este módulo contiene las funciones de acceso a datos (DAO) para la tabla 'doctores'.
# Cada función se encarga de una operación CRUD (Crear, Leer, Actualizar, Eliminar)
# específica en la base de datos, interactuando directamente con la tabla 'doctores'.

from DAOS.db import conectar

def registrar_doctor(datos):
    """
    Inserta un nuevo registro de doctor en la base de datos.

    Args:
        datos (dict): Un diccionario con los datos del doctor.
                      Debe contener las llaves: 'nombre', 'direccion', 'telefono', 'fecha_nac',
                      'sexo', 'especialidad', 'contrasena'.
    """
    # Establece conexión con la base de datos.
    conn = conectar()
    cur = conn.cursor()
    
    # Consulta SQL para insertar un nuevo doctor.
    sql = """
    INSERT INTO doctores (nombre, direccion, telefono, fecha_nac, sexo, especialidad, contrasena)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    # Ejecuta la consulta con los datos proporcionados.
    # Se usa 'or None' para manejar fechas de nacimiento vacías y convertirlas a NULL en la BD.
    cur.execute(sql, (datos['nombre'], datos['direccion'], datos['telefono'], datos['fecha_nac'] or None, datos['sexo'], datos['especialidad'], datos['contrasena']))
    
    # Confirma la transacción para guardar los cambios.
    conn.commit()
    
    # Cierra el cursor y la conexión.
    cur.close()
    conn.close()

def mostrar_doctor_por_id(id_val):
    """
    Busca y devuelve un doctor por su código (ID).

    Args:
        id_val (str or int): El ID del doctor a buscar.

    Returns:
        tuple or None: Una tupla con los datos del doctor si se encuentra, de lo contrario None.
    """
    conn = conectar()
    cur = conn.cursor()
    
    # Consulta para seleccionar un doctor por su código.
    cur.execute("SELECT codigo, nombre, direccion, telefono, fecha_nac, sexo, especialidad, contrasena FROM doctores WHERE codigo = %s", (int(id_val),))
    
    # Obtiene el primer resultado de la consulta.
    row = cur.fetchone()
    
    cur.close()
    conn.close()
    return row

def mostrar_todos_los_doctores():
    """
    Devuelve todos los registros de doctores de la base de datos, ordenados por código.

    Returns:
        list: Una lista de tuplas, donde cada tupla es un registro de un doctor.
    """
    conn = conectar()
    cur = conn.cursor()
    
    # Consulta para obtener todos los doctores. No se selecciona la contraseña por seguridad.
    cur.execute("SELECT codigo, nombre, direccion, telefono, fecha_nac, sexo, especialidad FROM doctores ORDER BY codigo;")
    
    # Obtiene todos los resultados de la consulta.
    rows = cur.fetchall()
    
    cur.close()
    conn.close()
    return rows

def modificar_doctor(datos):
    """
    Actualiza los datos de un doctor existente en la base de datos.

    Args:
        datos (dict): Un diccionario con los datos actualizados del doctor.
                      Debe contener la llave 'codigo' para identificar al doctor a modificar.
    """
    conn = conectar()
    cur = conn.cursor()
    
    # Consulta SQL para actualizar un doctor.
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
    """
    Elimina un doctor de la base de datos por su código (ID).

    Args:
        id_val (str or int): El ID del doctor a eliminar.

    Returns:
        int: El número de filas eliminadas (0 si no se encontró, 1 si se eliminó).
    """
    conn = conectar()
    cur = conn.cursor()
    
    # Consulta para eliminar un doctor por su código.
    cur.execute("DELETE FROM doctores WHERE codigo = %s", (int(id_val),))
    
    # Obtiene el número de filas afectadas por la última operación.
    cambios = cur.rowcount
    
    conn.commit()
    cur.close()
    conn.close()
    return cambios
