import tkinter as tk
from tkinter import messagebox, ttk
import psycopg2
from decimal import Decimal
from PIL import Image, ImageTk  # Necesitarás instalar: pip install Pillow

# ---------------------- CONEXIÓN ----------------------
def conectar():
    return psycopg2.connect(
        host="localhost",
        dbname="nucleo_diagnostico",
        user="postgres",
        password="12345"
    )

# ---------------------- LOGIN ----------------------
def validar_login():
    usuario = entry_usuario.get().strip()
    contra = entry_contra.get().strip()

    # Verificar si es administrador
    if usuario == "admin" and contra == "12345":
        messagebox.showinfo("Acceso permitido", "Bienvenido administrador")
        ventana_login.destroy()
        abrir_menu_principal_admin(usuario)
    else:
        # Verificar si es empleado
        try:
            conn = conectar()
            cur = conn.cursor()
            # Verificar si el código de empleado y contraseña son correctos
            cur.execute("SELECT codigo, nombre FROM empleado WHERE codigo = %s AND contrasena = %s", 
                       (usuario, contra))
            empleado = cur.fetchone()
            cur.close()
            conn.close()

            if empleado:
                messagebox.showinfo("Acceso permitido", f"Bienvenido empleado: {empleado[1]}")
                ventana_login.destroy()
                abrir_menu_principal_empleado(empleado[0], empleado[1])  # Pasar código y nombre
            else:
                messagebox.showerror("Acceso denegado", "Código o contraseña incorrectos")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo validar el empleado: {e}")

# ---------------------- MENÚ PRINCIPAL ADMIN ----------------------
def abrir_menu_principal_admin(usuario):
    global ventana_menu_admin, bg_image_admin
    
    ventana_menu_admin = tk.Tk()
    ventana_menu_admin.title("Sistema - Menú Principal Administrador")
    ventana_menu_admin.geometry("800x600")
    
    # Cargar imagen de fondo con Pillow
    try:
        image = Image.open("fondo_nucleo.png")
        # Redimensionar imagen al tamaño de la ventana
        image = image.resize((800, 600), Image.Resampling.LANCZOS)
        bg_image_admin = ImageTk.PhotoImage(image)
        
        background_label = tk.Label(ventana_menu_admin, image=bg_image_admin)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print(f"Error cargando imagen de fondo: {e}")
        ventana_menu_admin.configure(bg='#2c3e50')
    
    # Frame principal
    main_frame = tk.Frame(ventana_menu_admin, bg='white', relief='raised', bd=3)
    main_frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=350)

    # Saludo en la parte superior izquierda
    saludo_frame = tk.Frame(main_frame, bg='white')
    saludo_frame.pack(anchor='nw', fill='x', pady=(0, 10))
    
    ttk.Label(saludo_frame, text=f"Administrador: {usuario}", 
              font=("Arial", 12, "bold"), 
              background='white',
              foreground='#2c3e50').pack(side='left')

    # Título del sistema
    titulo_frame = tk.Frame(main_frame, bg='#3498db', height=60)
    titulo_frame.pack(fill='x', pady=(0, 20))
    titulo_frame.pack_propagate(False)
    
    ttk.Label(titulo_frame, text="NÚCLEO DIAGNÓSTICO", 
              font=("Arial", 16, "bold"), 
              background='#3498db',
              foreground='white').pack(expand=True)
    
    ttk.Label(main_frame, text="Seleccione una opción", 
              font=("Arial", 14, "bold"), 
              background='white',
              foreground='#34495e').pack(pady=5)

    # Frame para los botones
    botones_frame = tk.Frame(main_frame, bg='white')
    botones_frame.pack(pady=20)
    
    # Botones con colores
    estilo_botones = ttk.Style()
    estilo_botones.configure('Botones.TButton', font=('Arial', 10), width=25)
    
    ttk.Button(botones_frame, text="Empleados", 
               style='Botones.TButton',
               command=abrir_menu_empleados).pack(pady=10)
    ttk.Button(botones_frame, text="Doctores", 
               style='Botones.TButton',
               command=abrir_menu_doctores).pack(pady=10)
    ttk.Button(botones_frame, text="Salir", 
               style='Botones.TButton',
               command=ventana_menu_admin.destroy).pack(pady=10)
    
    # Información de pie de página
    pie_frame = tk.Frame(main_frame, bg='#ecf0f1', height=40)
    pie_frame.pack(fill='x', side='bottom')
    pie_frame.pack_propagate(False)
    
    ttk.Label(pie_frame, text="Sistema de Gestión Hospitalaria v1.0", 
              font=("Arial", 8), 
              background='#ecf0f1',
              foreground='#7f8c8d').pack(expand=True)

    ventana_menu_admin.mainloop()

# ---------------------- MENÚ PRINCIPAL EMPLEADO ----------------------
def abrir_menu_principal_empleado(codigo_empleado, nombre_empleado):
    global ventana_menu_empleado, bg_image_empleado
    
    ventana_menu_empleado = tk.Tk()
    ventana_menu_empleado.title("Sistema - Menú Principal Empleado")
    ventana_menu_empleado.geometry("800x600")
    
    # Cargar imagen de fondo con Pillow
    try:
        image = Image.open("fondo_nucleo.png")
        # Redimensionar imagen al tamaño de la ventana
        image = image.resize((800, 600), Image.Resampling.LANCZOS)
        bg_image_empleado = ImageTk.PhotoImage(image)
        
        background_label = tk.Label(ventana_menu_empleado, image=bg_image_empleado)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print(f"Error cargando imagen de fondo: {e}")
        ventana_menu_empleado.configure(bg='#2c3e50')
    
    # Frame principal
    main_frame = tk.Frame(ventana_menu_empleado, bg='white', relief='raised', bd=3)
    main_frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=350)

    # Saludo en la parte superior izquierda
    saludo_frame = tk.Frame(main_frame, bg='white')
    saludo_frame.pack(anchor='nw', fill='x', pady=(0, 10))
    
    ttk.Label(saludo_frame, text=f"Hola, {nombre_empleado}", 
              font=("Arial", 12, "bold"), 
              background='white',
              foreground='#2c3e50').pack(side='left')

    # Título del sistema
    titulo_frame = tk.Frame(main_frame, bg='#27ae60', height=60)
    titulo_frame.pack(fill='x', pady=(0, 20))
    titulo_frame.pack_propagate(False)
    
    ttk.Label(titulo_frame, text="NÚCLEO DIAGNÓSTICO", 
              font=("Arial", 16, "bold"), 
              background='#27ae60',
              foreground='white').pack(expand=True)
    
    ttk.Label(main_frame, text="Seleccione una opción", 
              font=("Arial", 14, "bold"), 
              background='white',
              foreground='#34495e').pack(pady=5)

    # Frame para los botones
    botones_frame = tk.Frame(main_frame, bg='white')
    botones_frame.pack(pady=20)
    
    # Botones para empleado
    ttk.Button(botones_frame, text="Administrar pacientes", width=25, 
               command=abrir_gestion_pacientes).pack(pady=8)
    ttk.Button(botones_frame, text="Administrar citas", width=25, 
               command=menu_citas_no_disponible).pack(pady=8)
    ttk.Button(botones_frame, text="Administrar medicamentos", width=25, 
               command=menu_medicamentos_no_disponible).pack(pady=8)
    ttk.Button(botones_frame, text="Salir", width=25, 
               command=ventana_menu_empleado.destroy).pack(pady=8)
    
    # Información de pie de página
    pie_frame = tk.Frame(main_frame, bg='#ecf0f1', height=40)
    pie_frame.pack(fill='x', side='bottom')
    pie_frame.pack_propagate(False)
    
    ttk.Label(pie_frame, text="Sistema de Gestión Hospitalaria v1.0", 
              font=("Arial", 8), 
              background='#ecf0f1',
              foreground='#7f8c8d').pack(expand=True)

    ventana_menu_empleado.mainloop()

# ---------------------- FUNCIONES TEMPORALES PARA MÓDULOS NO DISPONIBLES ----------------------
def menu_citas_no_disponible():
    messagebox.showinfo("En desarrollo", "El módulo de Administrar Citas está en desarrollo")

def menu_medicamentos_no_disponible():
    messagebox.showinfo("En desarrollo", "El módulo de Administrar Medicamentos está en desarrollo")

# ---------------------- GESTIÓN DE PACIENTES (PARA EMPLEADOS) ----------------------
def abrir_gestion_pacientes():
    ventana_pacientes = tk.Toplevel()
    ventana_pacientes.title("Gestión de Pacientes")
    ventana_pacientes.geometry("400x400")
    ventana_pacientes.configure(bg='#ecf0f1')

    # Frame principal
    main_frame = tk.Frame(ventana_pacientes, bg='white', relief='raised', bd=2)
    main_frame.pack(expand=True, fill='both', padx=20, pady=20)

    ttk.Label(main_frame, text="Gestión de Pacientes", 
              font=("Arial", 16, "bold"),
              background='white').pack(pady=20)

    # Frame para botones
    botones_frame = tk.Frame(main_frame, bg='white')
    botones_frame.pack(expand=True)

    ttk.Button(botones_frame, text="Registrar paciente", width=30, 
               command=ventana_registrar_paciente).pack(pady=8)
    ttk.Button(botones_frame, text="Mostrar paciente por ID", width=30, 
               command=ventana_mostrar_paciente_por_id).pack(pady=8)
    ttk.Button(botones_frame, text="Mostrar todos los pacientes", width=30, 
               command=ventana_mostrar_todos_pacientes).pack(pady=8)
    ttk.Button(botones_frame, text="Modificar paciente", width=30, 
               command=ventana_modificar_paciente).pack(pady=8)
    ttk.Button(botones_frame, text="Eliminar paciente", width=30, 
               command=ventana_eliminar_paciente).pack(pady=8)
    ttk.Button(botones_frame, text="Cerrar", width=30, 
               command=ventana_pacientes.destroy).pack(pady=15)

# ---------------------- MENÚ EMPLEADOS (ADMIN) ----------------------
def abrir_menu_empleados():
    ventana_empleados = tk.Toplevel()
    ventana_empleados.title("Sistema - Empleados")
    ventana_empleados.geometry("400x400")
    ventana_empleados.configure(bg='#ecf0f1')

    # Frame principal
    main_frame = tk.Frame(ventana_empleados, bg='white', relief='raised', bd=2)
    main_frame.pack(expand=True, fill='both', padx=20, pady=20)

    ttk.Label(main_frame, text="Gestión de Empleados", 
              font=("Arial", 16, "bold"),
              background='white').pack(pady=20)

    # Frame para botones
    botones_frame = tk.Frame(main_frame, bg='white')
    botones_frame.pack(expand=True)

    ttk.Button(botones_frame, text="Registrar empleado", width=30, 
               command=ventana_registrar_empleado).pack(pady=8)
    ttk.Button(botones_frame, text="Mostrar empleado por ID", width=30, 
               command=ventana_mostrar_empleado_por_id).pack(pady=8)
    ttk.Button(botones_frame, text="Mostrar todos los empleados", width=30, 
               command=ventana_mostrar_todos_empleados).pack(pady=8)
    ttk.Button(botones_frame, text="Modificar empleado", width=30, 
               command=ventana_modificar_empleado).pack(pady=8)
    ttk.Button(botones_frame, text="Eliminar empleado", width=30, 
               command=ventana_eliminar_empleado).pack(pady=8)
    ttk.Button(botones_frame, text="Cerrar", width=30, 
               command=ventana_empleados.destroy).pack(pady=15)

# ---------------------- MENÚ DOCTORES (ADMIN) ----------------------
def abrir_menu_doctores():
    ventana_doctores = tk.Toplevel()
    ventana_doctores.title("Sistema - Doctores")
    ventana_doctores.geometry("400x400")
    ventana_doctores.configure(bg='#ecf0f1')
    
    # Frame principal
    main_frame = tk.Frame(ventana_doctores, bg='white', relief='raised', bd=2)
    main_frame.pack(expand=True, fill='both', padx=20, pady=20)

    ttk.Label(main_frame, text="Gestión de Doctores", 
              font=("Arial", 16, "bold"),
              background='white').pack(pady=20)

    # Frame para botones
    botones_frame = tk.Frame(main_frame, bg='white')
    botones_frame.pack(expand=True)
    
    ttk.Button(botones_frame, text="Registrar doctor", width=30, 
               command=ventana_registrar_doctor).pack(pady=8)
    ttk.Button(botones_frame, text="Mostrar doctor por ID", width=30, 
               command=ventana_mostrar_doctor_por_id).pack(pady=8)
    ttk.Button(botones_frame, text="Mostrar todos los doctores", width=30, 
               command=ventana_mostrar_todos_doctores).pack(pady=8)
    ttk.Button(botones_frame, text="Modificar doctor", width=30, 
               command=ventana_modificar_doctor).pack(pady=8)
    ttk.Button(botones_frame, text="Eliminar doctor", width=30, 
               command=ventana_eliminar_doctor).pack(pady=8)
    ttk.Button(botones_frame, text="Cerrar", width=30, 
               command=ventana_doctores.destroy).pack(pady=15)

# ====================== FUNCIONES PARA PACIENTES ======================

# ---------------------- REGISTRAR PACIENTE ----------------------
def ventana_registrar_paciente():
    win = tk.Toplevel()
    win.title("Registrar paciente")
    win.geometry("500x500")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=10, pady=10)

    labels = ["Nombre", "Dirección", "Teléfono", "Fecha Nac (YYYY-MM-DD)", "Sexo", "Edad", "Estatura"]
    entries = {}

    for i, text in enumerate(labels):
        ttk.Label(main_frame, text=text+":").grid(row=i, column=0, padx=8, pady=8, sticky="e")
        ent = ttk.Entry(main_frame, width=40)
        ent.grid(row=i, column=1, padx=8, pady=8)
        entries[text] = ent

    def guardar():
        try:
            datos = (
                entries["Nombre"].get().strip(),
                entries["Dirección"].get().strip(),
                entries["Teléfono"].get().strip(),
                entries["Fecha Nac (YYYY-MM-DD)"].get().strip(),
                entries["Sexo"].get().strip(),
                entries["Edad"].get().strip(),
                entries["Estatura"].get().strip()
            )

            if not datos[0]:
                messagebox.showwarning("Validación", "El nombre es obligatorio")
                return

            # Validar edad
            try:
                edad_val = int(datos[5]) if datos[5] else None
            except ValueError:
                messagebox.showwarning("Validación", "Edad debe ser un número entero")
                return

            # Validar estatura
            try:
                estatura_val = Decimal(datos[6]) if datos[6] else None
            except:
                messagebox.showwarning("Validación", "Estatura debe ser un número válido")
                return

            conn = conectar()
            cur = conn.cursor()
            sql = """
            INSERT INTO pacientes (nombre, direccion, telefono, fecha_nac, sexo, edad, estatura)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cur.execute(sql, (datos[0], datos[1], datos[2], datos[3] or None, datos[4], edad_val, estatura_val))
            conn.commit()
            cur.close()
            conn.close()

            messagebox.showinfo("Éxito", "Paciente registrado correctamente")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar: {e}")

    button_frame = tk.Frame(main_frame)
    button_frame.grid(row=len(labels), column=0, columnspan=2, pady=20)
    
    ttk.Button(button_frame, text="Guardar", command=guardar).pack(side='left', padx=10)
    ttk.Button(button_frame, text="Cancelar", command=win.destroy).pack(side='left', padx=10)

# ---------------------- MOSTRAR PACIENTE POR ID ----------------------
def ventana_mostrar_paciente_por_id():
    win = tk.Toplevel()
    win.title("Mostrar paciente por ID")
    win.geometry("500x300")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=20, pady=20)

    ttk.Label(main_frame, text="ID del paciente:").grid(row=0, column=0, padx=8, pady=8)
    id_entry = ttk.Entry(main_frame, width=20)
    id_entry.grid(row=0, column=1, padx=8, pady=8)

    def buscar():
        try:
            id_val = id_entry.get().strip()
            if not id_val.isdigit():
                messagebox.showwarning("Validación", "ID inválido")
                return
            conn = conectar()
            cur = conn.cursor()
            cur.execute("SELECT codigo, nombre, direccion, telefono, fecha_nac, sexo, edad, estatura FROM pacientes WHERE codigo = %s", (int(id_val),))
            row = cur.fetchone()
            cur.close()
            conn.close()

            if not row:
                messagebox.showinfo("Resultado", "No se encontró el paciente con ese ID")
                return

            result_frame = tk.Frame(main_frame, relief='sunken', bd=2)
            result_frame.grid(row=2, column=0, columnspan=2, padx=8, pady=8, sticky='we')
            
            txt = tk.Text(result_frame, width=60, height=8, wrap='word')
            txt.pack(padx=5, pady=5)
            txt.delete("1.0", tk.END)
            txt.insert(tk.END, f"ID: {row[0]}\nNombre: {row[1]}\nDirección: {row[2]}\nTeléfono: {row[3]}\nFecha Nac: {row[4]}\nSexo: {row[5]}\nEdad: {row[6]}\nEstatura: {row[7]}")
            txt.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Buscar", command=buscar).grid(row=1, column=0, columnspan=2, pady=10)

# ---------------------- MOSTRAR TODOS LOS PACIENTES ----------------------
def ventana_mostrar_todos_pacientes():
    win = tk.Toplevel()
    win.title("Todos los pacientes")
    win.geometry("900x400")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=10, pady=10)

    cols = ("codigo","nombre","direccion","telefono","fecha_nac","sexo","edad","estatura")
    tree = ttk.Treeview(main_frame, columns=cols, show="headings")
    
    for c in cols:
        tree.heading(c, text=c.capitalize())
        tree.column(c, width=100, anchor="center")

    vsb = ttk.Scrollbar(main_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    
    tree.pack(side='left', fill='both', expand=True)
    vsb.pack(side='right', fill='y')

    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT codigo, nombre, direccion, telefono, fecha_nac, sexo, edad, estatura FROM pacientes ORDER BY codigo;")
        rows = cur.fetchall()
        cur.close()
        conn.close()

        for r in rows:
            tree.insert("", tk.END, values=r)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------------------- MODIFICAR PACIENTE ----------------------
def ventana_modificar_paciente():
    win = tk.Toplevel()
    win.title("Modificar paciente")
    win.geometry("500x550")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=10, pady=10)

    ttk.Label(main_frame, text="ID a modificar:").grid(row=0, column=0, padx=8, pady=8)
    id_entry = ttk.Entry(main_frame, width=20)
    id_entry.grid(row=0, column=1, padx=8, pady=8)

    def cargar():
        id_val = id_entry.get().strip()
        if not id_val.isdigit():
            messagebox.showwarning("Validación", "ID inválido")
            return
        try:
            conn = conectar()
            cur = conn.cursor()
            cur.execute("SELECT codigo, nombre, direccion, telefono, fecha_nac, sexo, edad, estatura FROM pacientes WHERE codigo = %s", (int(id_val),))
            row = cur.fetchone()
            cur.close()
            conn.close()

            if not row:
                messagebox.showinfo("Resultado", "No se encontró el paciente")
                return

            labels = ["Nombre", "Dirección", "Teléfono", "Fecha Nac (YYYY-MM-DD)", "Sexo", "Edad", "Estatura"]
            entries = {}
            for i, text in enumerate(labels):
                ttk.Label(main_frame, text=text+":").grid(row=2+i, column=0, padx=8, pady=6, sticky="e")
                ent = ttk.Entry(main_frame, width=40)
                ent.grid(row=2+i, column=1, padx=8, pady=6)
                entries[text] = ent

            entries["Nombre"].insert(0, row[1])
            entries["Dirección"].insert(0, row[2])
            entries["Teléfono"].insert(0, row[3])
            entries["Fecha Nac (YYYY-MM-DD)"].insert(0, row[4] if row[4] else "")
            entries["Sexo"].insert(0, row[5] if row[5] else "")
            entries["Edad"].insert(0, str(row[6]) if row[6] is not None else "")
            entries["Estatura"].insert(0, str(row[7]) if row[7] is not None else "")

            def guardar_cambios():
                try:
                    nombre = entries["Nombre"].get().strip()
                    direccion = entries["Dirección"].get().strip()
                    telefono = entries["Teléfono"].get().strip()
                    fecha = entries["Fecha Nac (YYYY-MM-DD)"].get().strip() or None
                    sexo = entries["Sexo"].get().strip()
                    edad_raw = entries["Edad"].get().strip()
                    estatura_raw = entries["Estatura"].get().strip()

                    # Validar edad
                    try:
                        edad_val = int(edad_raw) if edad_raw != "" else None
                    except ValueError:
                        messagebox.showwarning("Validación", "Edad debe ser un número entero")
                        return

                    # Validar estatura
                    try:
                        estatura_val = Decimal(estatura_raw) if estatura_raw != "" else None
                    except:
                        messagebox.showwarning("Validación", "Estatura debe ser un número válido")
                        return

                    conn = conectar()
                    cur = conn.cursor()
                    sql = """
                    UPDATE pacientes
                    SET nombre=%s, direccion=%s, telefono=%s, fecha_nac=%s, sexo=%s, edad=%s, estatura=%s
                    WHERE codigo=%s
                    """
                    cur.execute(sql, (nombre, direccion, telefono, fecha, sexo, edad_val, estatura_val, int(id_val)))
                    conn.commit()
                    cur.close()
                    conn.close()

                    messagebox.showinfo("Éxito", "Paciente modificado correctamente")
                    win.destroy()
                except Exception as e:
                    messagebox.showerror("Error", str(e))

            button_frame = tk.Frame(main_frame)
            button_frame.grid(row=2+len(labels), column=0, columnspan=2, pady=20)
            
            ttk.Button(button_frame, text="Guardar cambios", command=guardar_cambios).pack(side='left', padx=10)
            ttk.Button(button_frame, text="Cancelar", command=win.destroy).pack(side='left', padx=10)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Cargar", command=cargar).grid(row=1, column=0, columnspan=2, pady=10)

# ---------------------- ELIMINAR PACIENTE ----------------------
def ventana_eliminar_paciente():
    win = tk.Toplevel()
    win.title("Eliminar paciente")
    win.geometry("400x200")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=20, pady=20)

    ttk.Label(main_frame, text="ID a eliminar:").grid(row=0, column=0, padx=8, pady=8)
    id_entry = ttk.Entry(main_frame, width=20)
    id_entry.grid(row=0, column=1, padx=8, pady=8)

    def eliminar():
        id_val = id_entry.get().strip()
        if not id_val.isdigit():
            messagebox.showwarning("Validación", "ID inválido")
            return

        if not messagebox.askyesno("Confirmar", f"¿Eliminar paciente con ID {id_val}?"):
            return

        try:
            conn = conectar()
            cur = conn.cursor()
            cur.execute("DELETE FROM pacientes WHERE codigo = %s", (int(id_val),))
            cambios = cur.rowcount
            conn.commit()
            cur.close()
            conn.close()

            if cambios == 0:
                messagebox.showinfo("Resultado", "No se encontró el paciente")
            else:
                messagebox.showinfo("Éxito", "Paciente eliminado correctamente")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    button_frame = tk.Frame(main_frame)
    button_frame.grid(row=1, column=0, columnspan=2, pady=20)
    
    ttk.Button(button_frame, text="Eliminar", command=eliminar).pack(side='left', padx=10)
    ttk.Button(button_frame, text="Cancelar", command=win.destroy).pack(side='left', padx=10)

# ====================== FUNCIONES PARA EMPLEADOS (ADMIN) ======================

# ---------------------- REGISTRAR EMPLEADO ----------------------
def ventana_registrar_empleado():
    win = tk.Toplevel()
    win.title("Registrar empleado")
    win.geometry("500x500")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=10, pady=10)

    labels = ["Nombre", "Dirección", "Teléfono", "Fecha Nac (YYYY-MM-DD)", "Sexo (M/F)", "Sueldo", "Turno", "Contraseña"]
    entries = {}

    for i, text in enumerate(labels):
        ttk.Label(main_frame, text=text+":").grid(row=i, column=0, padx=8, pady=8, sticky="e")
        ent = ttk.Entry(main_frame, width=40, show="*" if "Contraseña" in text else "")
        ent.grid(row=i, column=1, padx=8, pady=8)
        entries[text] = ent

    def guardar():
        try:
            datos = (
                entries["Nombre"].get().strip(),
                entries["Dirección"].get().strip(),
                entries["Teléfono"].get().strip(),
                entries["Fecha Nac (YYYY-MM-DD)"].get().strip(),
                entries["Sexo (M/F)"].get().strip(),
                entries["Sueldo"].get().strip(),
                entries["Turno"].get().strip(),
                entries["Contraseña"].get().strip()
            )

            if not datos[0]:
                messagebox.showwarning("Validación", "El nombre es obligatorio")
                return

            try:
                sueldo_val = Decimal(datos[5]) if datos[5] != "" else Decimal("0.00")
            except Exception:
                messagebox.showwarning("Validación", "Sueldo inválido")
                return

            conn = conectar()
            cur = conn.cursor()
            sql = """
            INSERT INTO empleado (nombre, direccion, telefono, fecha_nac, sexo, sueldo, turno, contrasena)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cur.execute(sql, (datos[0], datos[1], datos[2], datos[3] or None, datos[4], sueldo_val, datos[6], datos[7]))
            conn.commit()
            cur.close()
            conn.close()

            messagebox.showinfo("Éxito", "Empleado registrado correctamente")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar: {e}")

    button_frame = tk.Frame(main_frame)
    button_frame.grid(row=len(labels), column=0, columnspan=2, pady=20)
    
    ttk.Button(button_frame, text="Guardar", command=guardar).pack(side='left', padx=10)
    ttk.Button(button_frame, text="Cancelar", command=win.destroy).pack(side='left', padx=10)

# ---------------------- MOSTRAR EMPLEADO POR ID ----------------------
def ventana_mostrar_empleado_por_id():
    win = tk.Toplevel()
    win.title("Mostrar empleado por ID")
    win.geometry("500x300")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=20, pady=20)

    ttk.Label(main_frame, text="ID del empleado:").grid(row=0, column=0, padx=8, pady=8)
    id_entry = ttk.Entry(main_frame, width=20)
    id_entry.grid(row=0, column=1, padx=8, pady=8)

    def buscar():
        try:
            id_val = id_entry.get().strip()
            if not id_val.isdigit():
                messagebox.showwarning("Validación", "ID inválido")
                return
            conn = conectar()
            cur = conn.cursor()
            cur.execute("SELECT codigo, nombre, direccion, telefono, fecha_nac, sexo, sueldo, turno FROM empleado WHERE codigo = %s", (int(id_val),))
            row = cur.fetchone()
            cur.close()
            conn.close()

            if not row:
                messagebox.showinfo("Resultado", "No se encontró el empleado con ese ID")
                return

            result_frame = tk.Frame(main_frame, relief='sunken', bd=2)
            result_frame.grid(row=2, column=0, columnspan=2, padx=8, pady=8, sticky='we')
            
            txt = tk.Text(result_frame, width=60, height=8, wrap='word')
            txt.pack(padx=5, pady=5)
            txt.delete("1.0", tk.END)
            txt.insert(tk.END, f"ID: {row[0]}\nNombre: {row[1]}\nDirección: {row[2]}\nTeléfono: {row[3]}\nFecha Nac: {row[4]}\nSexo: {row[5]}\nSueldo: {row[6]}\nTurno: {row[7]}")
            txt.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Buscar", command=buscar).grid(row=1, column=0, columnspan=2, pady=10)

# ---------------------- MOSTRAR TODOS LOS EMPLEADOS ----------------------
def ventana_mostrar_todos_empleados():
    win = tk.Toplevel()
    win.title("Todos los empleados")
    win.geometry("900x400")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=10, pady=10)

    cols = ("codigo","nombre","direccion","telefono","fecha_nac","sexo","sueldo","turno")
    tree = ttk.Treeview(main_frame, columns=cols, show="headings")
    
    for c in cols:
        tree.heading(c, text=c.capitalize())
        tree.column(c, width=110, anchor="center")

    vsb = ttk.Scrollbar(main_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    
    tree.pack(side='left', fill='both', expand=True)
    vsb.pack(side='right', fill='y')

    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT codigo, nombre, direccion, telefono, fecha_nac, sexo, sueldo, turno FROM empleado ORDER BY codigo;")
        rows = cur.fetchall()
        cur.close()
        conn.close()

        for r in rows:
            tree.insert("", tk.END, values=r)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------------------- MODIFICAR EMPLEADO ----------------------
def ventana_modificar_empleado():
    win = tk.Toplevel()
    win.title("Modificar empleado")
    win.geometry("500x600")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=10, pady=10)

    ttk.Label(main_frame, text="ID a modificar:").grid(row=0, column=0, padx=8, pady=8)
    id_entry = ttk.Entry(main_frame, width=20)
    id_entry.grid(row=0, column=1, padx=8, pady=8)

    def cargar():
        id_val = id_entry.get().strip()
        if not id_val.isdigit():
            messagebox.showwarning("Validación", "ID inválido")
            return
        try:
            conn = conectar()
            cur = conn.cursor()
            cur.execute("SELECT codigo, nombre, direccion, telefono, fecha_nac, sexo, sueldo, turno, contrasena FROM empleado WHERE codigo = %s", (int(id_val),))
            row = cur.fetchone()
            cur.close()
            conn.close()

            if not row:
                messagebox.showinfo("Resultado", "No se encontró el empleado")
                return

            labels = ["Nombre", "Dirección", "Teléfono", "Fecha Nac (YYYY-MM-DD)", "Sexo (M/F)", "Sueldo", "Turno", "Contraseña"]
            entries = {}
            for i, text in enumerate(labels):
                ttk.Label(main_frame, text=text+":").grid(row=2+i, column=0, padx=8, pady=6, sticky="e")
                ent = ttk.Entry(main_frame, width=40, show="*" if "Contraseña" in text else "")
                ent.grid(row=2+i, column=1, padx=8, pady=6)
                entries[text] = ent

            entries["Nombre"].insert(0, row[1])
            entries["Dirección"].insert(0, row[2])
            entries["Teléfono"].insert(0, row[3])
            entries["Fecha Nac (YYYY-MM-DD)"].insert(0, row[4] if row[4] else "")
            entries["Sexo (M/F)"].insert(0, row[5] if row[5] else "")
            entries["Sueldo"].insert(0, str(row[6]) if row[6] is not None else "")
            entries["Turno"].insert(0, row[7] if row[7] else "")
            entries["Contraseña"].insert(0, row[8] if row[8] else "")

            def guardar_cambios():
                try:
                    nombre = entries["Nombre"].get().strip()
                    direccion = entries["Dirección"].get().strip()
                    telefono = entries["Teléfono"].get().strip()
                    fecha = entries["Fecha Nac (YYYY-MM-DD)"].get().strip() or None
                    sexo = entries["Sexo (M/F)"].get().strip()
                    sueldo_raw = entries["Sueldo"].get().strip()
                    turno = entries["Turno"].get().strip()
                    contra = entries["Contraseña"].get().strip()

                    try:
                        sueldo_val = Decimal(sueldo_raw) if sueldo_raw != "" else None
                    except Exception:
                        messagebox.showwarning("Validación", "Sueldo inválido")
                        return

                    conn = conectar()
                    cur = conn.cursor()
                    sql = """
                    UPDATE empleado
                    SET nombre=%s, direccion=%s, telefono=%s, fecha_nac=%s, sexo=%s, sueldo=%s, turno=%s, contrasena=%s
                    WHERE codigo=%s
                    """
                    cur.execute(sql, (nombre, direccion, telefono, fecha, sexo, sueldo_val, turno, contra, int(id_val)))
                    conn.commit()
                    cur.close()
                    conn.close()

                    messagebox.showinfo("Éxito", "Empleado modificado correctamente")
                    win.destroy()
                except Exception as e:
                    messagebox.showerror("Error", str(e))

            button_frame = tk.Frame(main_frame)
            button_frame.grid(row=2+len(labels), column=0, columnspan=2, pady=20)
            
            ttk.Button(button_frame, text="Guardar cambios", command=guardar_cambios).pack(side='left', padx=10)
            ttk.Button(button_frame, text="Cancelar", command=win.destroy).pack(side='left', padx=10)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Cargar", command=cargar).grid(row=1, column=0, columnspan=2, pady=10)

# ---------------------- ELIMINAR EMPLEADO ----------------------
def ventana_eliminar_empleado():
    win = tk.Toplevel()
    win.title("Eliminar empleado")
    win.geometry("400x200")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=20, pady=20)

    ttk.Label(main_frame, text="ID a eliminar:").grid(row=0, column=0, padx=8, pady=8)
    id_entry = ttk.Entry(main_frame, width=20)
    id_entry.grid(row=0, column=1, padx=8, pady=8)

    def eliminar():
        id_val = id_entry.get().strip()
        if not id_val.isdigit():
            messagebox.showwarning("Validación", "ID inválido")
            return

        if not messagebox.askyesno("Confirmar", f"¿Eliminar empleado con ID {id_val}?"):
            return

        try:
            conn = conectar()
            cur = conn.cursor()
            cur.execute("DELETE FROM empleado WHERE codigo = %s", (int(id_val),))
            cambios = cur.rowcount
            conn.commit()
            cur.close()
            conn.close()

            if cambios == 0:
                messagebox.showinfo("Resultado", "No se encontró el empleado")
            else:
                messagebox.showinfo("Éxito", "Empleado eliminado correctamente")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    button_frame = tk.Frame(main_frame)
    button_frame.grid(row=1, column=0, columnspan=2, pady=20)
    
    ttk.Button(button_frame, text="Eliminar", command=eliminar).pack(side='left', padx=10)
    ttk.Button(button_frame, text="Cancelar", command=win.destroy).pack(side='left', padx=10)

# ====================== FUNCIONES PARA DOCTORES (ADMIN) ======================

# ---------------------- REGISTRAR DOCTOR ----------------------
def ventana_registrar_doctor():
    win = tk.Toplevel()
    win.title("Registrar doctor")
    win.geometry("500x450")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=10, pady=10)

    labels = ["Nombre", "Dirección", "Teléfono", "Fecha Nac (YYYY-MM-DD)", "Sexo", "Especialidad", "Contraseña"]
    entries = {}

    for i, text in enumerate(labels):
        ttk.Label(main_frame, text=text+":").grid(row=i, column=0, padx=8, pady=8, sticky="e")
        ent = ttk.Entry(main_frame, width=40, show="*" if "Contraseña" in text else "")
        ent.grid(row=i, column=1, padx=8, pady=8)
        entries[text] = ent

    def guardar():
        try:
            datos = (
                entries["Nombre"].get().strip(),
                entries["Dirección"].get().strip(),
                entries["Teléfono"].get().strip(),
                entries["Fecha Nac (YYYY-MM-DD)"].get().strip(),
                entries["Sexo"].get().strip(),
                entries["Especialidad"].get().strip(),
                entries["Contraseña"].get().strip()
            )

            if not datos[0]:
                messagebox.showwarning("Validación", "El nombre es obligatorio")
                return

            conn = conectar()
            cur = conn.cursor()
            sql = """
            INSERT INTO doctores (nombre, direccion, telefono, fecha_nac, sexo, especialidad, contrasena)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cur.execute(sql, (datos[0], datos[1], datos[2], datos[3] or None, datos[4], datos[5], datos[6]))
            conn.commit()
            cur.close()
            conn.close()

            messagebox.showinfo("Éxito", "Doctor registrado correctamente")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar: {e}")

    button_frame = tk.Frame(main_frame)
    button_frame.grid(row=len(labels), column=0, columnspan=2, pady=20)
    
    ttk.Button(button_frame, text="Guardar", command=guardar).pack(side='left', padx=10)
    ttk.Button(button_frame, text="Cancelar", command=win.destroy).pack(side='left', padx=10)

# ---------------------- MOSTRAR DOCTOR POR ID ----------------------
def ventana_mostrar_doctor_por_id():
    win = tk.Toplevel()
    win.title("Mostrar doctor por ID")
    win.geometry("500x300")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=20, pady=20)

    ttk.Label(main_frame, text="ID del doctor:").grid(row=0, column=0, padx=8, pady=8)
    id_entry = ttk.Entry(main_frame, width=20)
    id_entry.grid(row=0, column=1, padx=8, pady=8)

    def buscar():
        try:
            id_val = id_entry.get().strip()
            if not id_val.isdigit():
                messagebox.showwarning("Validación", "ID inválido")
                return
            conn = conectar()
            cur = conn.cursor()
            cur.execute("SELECT codigo, nombre, direccion, telefono, fecha_nac, sexo, especialidad FROM doctores WHERE codigo = %s", (int(id_val),))
            row = cur.fetchone()
            cur.close()
            conn.close()

            if not row:
                messagebox.showinfo("Resultado", "No se encontró el doctor con ese ID")
                return

            result_frame = tk.Frame(main_frame, relief='sunken', bd=2)
            result_frame.grid(row=2, column=0, columnspan=2, padx=8, pady=8, sticky='we')
            
            txt = tk.Text(result_frame, width=60, height=8, wrap='word')
            txt.pack(padx=5, pady=5)
            txt.delete("1.0", tk.END)
            txt.insert(tk.END, f"ID: {row[0]}\nNombre: {row[1]}\nDirección: {row[2]}\nTeléfono: {row[3]}\nFecha Nac: {row[4]}\nSexo: {row[5]}\nEspecialidad: {row[6]}")
            txt.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Buscar", command=buscar).grid(row=1, column=0, columnspan=2, pady=10)

# ---------------------- MOSTRAR TODOS LOS DOCTORES ----------------------
def ventana_mostrar_todos_doctores():
    win = tk.Toplevel()
    win.title("Todos los doctores")
    win.geometry("900x400")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=10, pady=10)

    cols = ("codigo","nombre","direccion","telefono","fecha_nac","sexo","especialidad")
    tree = ttk.Treeview(main_frame, columns=cols, show="headings")
    
    for c in cols:
        tree.heading(c, text=c.capitalize())
        tree.column(c, width=110, anchor="center")

    vsb = ttk.Scrollbar(main_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    
    tree.pack(side='left', fill='both', expand=True)
    vsb.pack(side='right', fill='y')

    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT codigo, nombre, direccion, telefono, fecha_nac, sexo, especialidad FROM doctores ORDER BY codigo;")
        rows = cur.fetchall()
        cur.close()
        conn.close()

        for r in rows:
            tree.insert("", tk.END, values=r)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------------------- MODIFICAR DOCTOR ----------------------
def ventana_modificar_doctor():
    win = tk.Toplevel()
    win.title("Modificar doctor")
    win.geometry("500x550")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=10, pady=10)

    ttk.Label(main_frame, text="ID a modificar:").grid(row=0, column=0, padx=8, pady=8)
    id_entry = ttk.Entry(main_frame, width=20)
    id_entry.grid(row=0, column=1, padx=8, pady=8)

    def cargar():
        id_val = id_entry.get().strip()
        if not id_val.isdigit():
            messagebox.showwarning("Validación", "ID inválido")
            return
        try:
            conn = conectar()
            cur = conn.cursor()
            cur.execute("SELECT codigo, nombre, direccion, telefono, fecha_nac, sexo, especialidad, contrasena FROM doctores WHERE codigo = %s", (int(id_val),))
            row = cur.fetchone()
            cur.close()
            conn.close()

            if not row:
                messagebox.showinfo("Resultado", "No se encontró el doctor")
                return

            labels = ["Nombre", "Dirección", "Teléfono", "Fecha Nac (YYYY-MM-DD)", "Sexo", "Especialidad", "Contraseña"]
            entries = {}
            for i, text in enumerate(labels):
                ttk.Label(main_frame, text=text+":").grid(row=2+i, column=0, padx=8, pady=6, sticky="e")
                ent = ttk.Entry(main_frame, width=40, show="*" if "Contraseña" in text else "")
                ent.grid(row=2+i, column=1, padx=8, pady=6)
                entries[text] = ent

            entries["Nombre"].insert(0, row[1])
            entries["Dirección"].insert(0, row[2])
            entries["Teléfono"].insert(0, row[3])
            entries["Fecha Nac (YYYY-MM-DD)"].insert(0, row[4] if row[4] else "")
            entries["Sexo"].insert(0, row[5] if row[5] else "")
            entries["Especialidad"].insert(0, row[6] if row[6] else "")
            entries["Contraseña"].insert(0, row[7] if row[7] else "")

            def guardar_cambios():
                try:
                    nombre = entries["Nombre"].get().strip()
                    direccion = entries["Dirección"].get().strip()
                    telefono = entries["Teléfono"].get().strip()
                    fecha = entries["Fecha Nac (YYYY-MM-DD)"].get().strip() or None
                    sexo = entries["Sexo"].get().strip()
                    especialidad = entries["Especialidad"].get().strip()
                    contra = entries["Contraseña"].get().strip()

                    conn = conectar()
                    cur = conn.cursor()
                    sql = """
                    UPDATE doctores
                    SET nombre=%s, direccion=%s, telefono=%s, fecha_nac=%s, sexo=%s, especialidad=%s, contrasena=%s
                    WHERE codigo=%s
                    """
                    cur.execute(sql, (nombre, direccion, telefono, fecha, sexo, especialidad, contra, int(id_val)))
                    conn.commit()
                    cur.close()
                    conn.close()

                    messagebox.showinfo("Éxito", "Doctor modificado correctamente")
                    win.destroy()
                except Exception as e:
                    messagebox.showerror("Error", str(e))

            button_frame = tk.Frame(main_frame)
            button_frame.grid(row=2+len(labels), column=0, columnspan=2, pady=20)
            
            ttk.Button(button_frame, text="Guardar cambios", command=guardar_cambios).pack(side='left', padx=10)
            ttk.Button(button_frame, text="Cancelar", command=win.destroy).pack(side='left', padx=10)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Cargar", command=cargar).grid(row=1, column=0, columnspan=2, pady=10)

# ---------------------- ELIMINAR DOCTOR ----------------------
def ventana_eliminar_doctor():
    win = tk.Toplevel()
    win.title("Eliminar doctor")
    win.geometry("400x200")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=20, pady=20)

    ttk.Label(main_frame, text="ID a eliminar:").grid(row=0, column=0, padx=8, pady=8)
    id_entry = ttk.Entry(main_frame, width=20)
    id_entry.grid(row=0, column=1, padx=8, pady=8)

    def eliminar():
        id_val = id_entry.get().strip()
        if not id_val.isdigit():
            messagebox.showwarning("Validación", "ID inválido")
            return

        if not messagebox.askyesno("Confirmar", f"¿Eliminar doctor con ID {id_val}?"):
            return

        try:
            conn = conectar()
            cur = conn.cursor()
            cur.execute("DELETE FROM doctores WHERE codigo = %s", (int(id_val),))
            cambios = cur.rowcount
            conn.commit()
            cur.close()
            conn.close()

            if cambios == 0:
                messagebox.showinfo("Resultado", "No se encontró el doctor")
            else:
                messagebox.showinfo("Éxito", "Doctor eliminado correctamente")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    button_frame = tk.Frame(main_frame)
    button_frame.grid(row=1, column=0, columnspan=2, pady=20)
    
    ttk.Button(button_frame, text="Eliminar", command=eliminar).pack(side='left', padx=10)
    ttk.Button(button_frame, text="Cancelar", command=win.destroy).pack(side='left', padx=10)

# ---------------------- INICIO (VENTANA LOGIN) ----------------------
ventana_login = tk.Tk()
ventana_login.title("Núcleo Diagnóstico - Sistema de Login")
ventana_login.geometry("350x200")
ventana_login.configure(bg='#ecf0f1')

# Frame principal del login
login_frame = tk.Frame(ventana_login, bg='white', relief='raised', bd=2)
login_frame.place(relx=0.5, rely=0.5, anchor='center', width=300, height=150)

ttk.Label(login_frame, text="Usuario/Código:", background='white').grid(row=0, column=0, padx=10, pady=12, sticky="e")
entry_usuario = ttk.Entry(login_frame, width=20)
entry_usuario.grid(row=0, column=1, padx=10, pady=12)

ttk.Label(login_frame, text="Contraseña:", background='white').grid(row=1, column=0, padx=10, pady=8, sticky="e")
entry_contra = ttk.Entry(login_frame, show="*", width=20)
entry_contra.grid(row=1, column=1, padx=10, pady=8)

ttk.Button(login_frame, text="Iniciar sesión", command=validar_login).grid(row=2, column=0, columnspan=2, pady=15)

ventana_login.mainloop()