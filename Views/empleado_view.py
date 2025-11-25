# Este módulo contiene todas las vistas (ventanas de interfaz de usuario)
# relacionadas con la gestión de empleados.

import tkinter as tk
from tkinter import ttk, messagebox

def abrir_menu_empleados(controller):
    """
    Crea y muestra el menú principal para la gestión de empleados.

    Args:
        controller: La instancia del controlador de empleados para manejar la lógica.
    """
    ventana_empleados = tk.Toplevel()
    ventana_empleados.title("Sistema - Empleados")
    ventana_empleados.geometry("400x400")
    ventana_empleados.configure(bg='#ecf0f1')

    main_frame = tk.Frame(ventana_empleados, bg='white', relief='raised', bd=2)
    main_frame.pack(expand=True, fill='both', padx=20, pady=20)

    ttk.Label(main_frame, text="Gestión de Empleados", 
              font=("Arial", 16, "bold"),
              background='white').pack(pady=20)

    botones_frame = tk.Frame(main_frame, bg='white')
    botones_frame.pack(expand=True)

    # Botones que disparan las diferentes ventanas de gestión de empleados.
    ttk.Button(botones_frame, text="Registrar empleado", width=30, 
               command=lambda: ventana_registrar_empleado(controller)).pack(pady=8)
    ttk.Button(botones_frame, text="Mostrar empleado por ID", width=30, 
               command=lambda: ventana_mostrar_empleado_por_id(controller)).pack(pady=8)
    ttk.Button(botones_frame, text="Mostrar todos los empleados", width=30, 
               command=lambda: ventana_mostrar_todos_empleados(controller)).pack(pady=8)
    ttk.Button(botones_frame, text="Modificar empleado", width=30, 
               command=lambda: ventana_modificar_empleado(controller)).pack(pady=8)
    ttk.Button(botones_frame, text="Eliminar empleado", width=30, 
               command=lambda: ventana_eliminar_empleado(controller)).pack(pady=8)
    ttk.Button(botones_frame, text="Cerrar", width=30, 
               command=ventana_empleados.destroy).pack(pady=15)

def ventana_registrar_empleado(controller):
    """
    Crea la ventana con el formulario para registrar un nuevo empleado.

    Args:
        controller: La instancia del controlador de empleados.
    """
    win = tk.Toplevel()
    win.title("Registrar empleado")
    win.geometry("500x500")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=10, pady=10)

    labels = ["Nombre", "Dirección", "Teléfono", "Fecha Nac (YYYY-MM-DD)", "Sexo (M/F)", "Sueldo", "Turno", "Contraseña"]
    entries = {}

    # Creación dinámica de etiquetas y campos de entrada.
    for i, text in enumerate(labels):
        ttk.Label(main_frame, text=text+":").grid(row=i, column=0, padx=8, pady=8, sticky="e")
        ent = ttk.Entry(main_frame, width=40, show="*" if "Contraseña" in text else "")
        ent.grid(row=i, column=1, padx=8, pady=8)
        entries[text] = ent

    def guardar():
        """Recopila datos del formulario y los pasa al controlador para su registro."""
        datos = {
            "nombre": entries["Nombre"].get().strip(),
            "direccion": entries["Dirección"].get().strip(),
            "telefono": entries["Teléfono"].get().strip(),
            "fecha_nac": entries["Fecha Nac (YYYY-MM-DD)"].get().strip(),
            "sexo": entries["Sexo (M/F)"].get().strip(),
            "sueldo": entries["Sueldo"].get().strip(),
            "turno": entries["Turno"].get().strip(),
            "contrasena": entries["Contraseña"].get().strip()
        }
        controller.registrar_empleado(datos, win)

    button_frame = tk.Frame(main_frame)
    button_frame.grid(row=len(labels), column=0, columnspan=2, pady=20)
    
    ttk.Button(button_frame, text="Guardar", command=guardar).pack(side='left', padx=10)
    ttk.Button(button_frame, text="Cancelar", command=win.destroy).pack(side='left', padx=10)

def ventana_mostrar_empleado_por_id(controller):
    """
    Crea la ventana para buscar un empleado por ID y mostrar sus detalles.

    Args:
        controller: La instancia del controlador de empleados.
    """
    win = tk.Toplevel()
    win.title("Mostrar empleado por ID")
    win.geometry("500x300")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=20, pady=20)

    ttk.Label(main_frame, text="ID del empleado:").grid(row=0, column=0, padx=8, pady=8)
    id_entry = ttk.Entry(main_frame, width=20)
    id_entry.grid(row=0, column=1, padx=8, pady=8)

    def buscar():
        """Obtiene el ID, llama al controlador y muestra los datos del empleado si se encuentra."""
        id_val = id_entry.get().strip()
        empleado = controller.mostrar_empleado_por_id(id_val)
        
        if empleado:
            result_frame = tk.Frame(main_frame, relief='sunken', bd=2)
            result_frame.grid(row=2, column=0, columnspan=2, padx=8, pady=8, sticky='we')
            
            txt = tk.Text(result_frame, width=60, height=8, wrap='word')
            txt.pack(padx=5, pady=5)
            txt.delete("1.0", tk.END)
            txt.insert(tk.END, f"ID: {empleado[0]}\nNombre: {empleado[1]}\nDirección: {empleado[2]}\nTeléfono: {empleado[3]}\nFecha Nac: {empleado[4]}\nSexo: {empleado[5]}\nSueldo: {empleado[6]}\nTurno: {empleado[7]}")
            txt.config(state="disabled")

    ttk.Button(main_frame, text="Buscar", command=buscar).grid(row=1, column=0, columnspan=2, pady=10)

def ventana_mostrar_todos_empleados(controller):
    """
    Crea una ventana con una tabla (Treeview) para mostrar todos los empleados.

    Args:
        controller: La instancia del controlador de empleados.
    """
    win = tk.Toplevel()
    win.title("Todos los empleados")
    win.geometry("900x400")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=10, pady=10)

    cols = ("codigo","nombre","direccion","telefono","fecha_nac","sexo","sueldo","turno")
    tree = ttk.Treeview(main_frame, columns=cols, show="headings")
    
    # Configuración de las columnas de la tabla.
    for c in cols:
        tree.heading(c, text=c.capitalize())
        tree.column(c, width=110, anchor="center")

    vsb = ttk.Scrollbar(main_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    
    tree.pack(side='left', fill='both', expand=True)
    vsb.pack(side='right', fill='y')

    # Carga de datos en la tabla.
    empleados = controller.mostrar_todos_los_empleados()
    if empleados:
        for r in empleados:
            tree.insert("", tk.END, values=r)

def ventana_modificar_empleado(controller):
    """
    Crea la ventana para modificar un empleado, cargando primero sus datos por ID.

    Args:
        controller: La instancia del controlador de empleados.
    """
    win = tk.Toplevel()
    win.title("Modificar empleado")
    win.geometry("500x600")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=10, pady=10)

    ttk.Label(main_frame, text="ID a modificar:").grid(row=0, column=0, padx=8, pady=8)
    id_entry = ttk.Entry(main_frame, width=20)
    id_entry.grid(row=0, column=1, padx=8, pady=8)

    def cargar():
        """Busca el empleado y, si existe, puebla un formulario con sus datos."""
        id_val = id_entry.get().strip()
        empleado = controller.mostrar_empleado_por_id(id_val)

        if empleado:
            # Creación del formulario de edición.
            labels = ["Nombre", "Dirección", "Teléfono", "Fecha Nac (YYYY-MM-DD)", "Sexo (M/F)", "Sueldo", "Turno", "Contraseña"]
            entries = {}
            for i, text in enumerate(labels):
                ttk.Label(main_frame, text=text+":").grid(row=2+i, column=0, padx=8, pady=6, sticky="e")
                ent = ttk.Entry(main_frame, width=40, show="*" if "Contraseña" in text else "")
                ent.grid(row=2+i, column=1, padx=8, pady=6)
                entries[text] = ent

            # Inserción de los datos actuales en los campos.
            entries["Nombre"].insert(0, empleado[1])
            entries["Dirección"].insert(0, empleado[2])
            entries["Teléfono"].insert(0, empleado[3])
            entries["Fecha Nac (YYYY-MM-DD)"].insert(0, empleado[4] if empleado[4] else "")
            entries["Sexo (M/F)"].insert(0, empleado[5] if empleado[5] else "")
            entries["Sueldo"].insert(0, str(empleado[6]) if empleado[6] is not None else "")
            entries["Turno"].insert(0, empleado[7] if empleado[7] else "")
            entries["Contraseña"].insert(0, empleado[8] if empleado[8] else "")

            def guardar_cambios():
                """Recopila los nuevos datos y los envía al controlador."""
                datos = {
                    "nombre": entries["Nombre"].get().strip(),
                    "direccion": entries["Dirección"].get().strip(),
                    "telefono": entries["Teléfono"].get().strip(),
                    "fecha_nac": entries["Fecha Nac (YYYY-MM-DD)"].get().strip(),
                    "sexo": entries["Sexo (M/F)"].get().strip(),
                    "sueldo": entries["Sueldo"].get().strip(),
                    "turno": entries["Turno"].get().strip(),
                    "contrasena": entries["Contraseña"].get().strip(),
                    "codigo": id_val
                }
                controller.modificar_empleado(datos, win)

            button_frame = tk.Frame(main_frame)
            button_frame.grid(row=2+len(labels), column=0, columnspan=2, pady=20)
            
            ttk.Button(button_frame, text="Guardar cambios", command=guardar_cambios).pack(side='left', padx=10)
            ttk.Button(button_frame, text="Cancelar", command=win.destroy).pack(side='left', padx=10)

    ttk.Button(main_frame, text="Cargar", command=cargar).grid(row=1, column=0, columnspan=2, pady=10)

def ventana_eliminar_empleado(controller):
    """
    Crea la ventana para eliminar un empleado por ID.

    Args:
        controller: La instancia del controlador de empleados.
    """
    win = tk.Toplevel()
    win.title("Eliminar empleado")
    win.geometry("400x200")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=20, pady=20)

    ttk.Label(main_frame, text="ID a eliminar:").grid(row=0, column=0, padx=8, pady=8)
    id_entry = ttk.Entry(main_frame, width=20)
    id_entry.grid(row=0, column=1, padx=8, pady=8)

    def eliminar():
        """Pasa el ID al controlador para que se procese la eliminación."""
        id_val = id_entry.get().strip()
        controller.eliminar_empleado(id_val, win)

    button_frame = tk.Frame(main_frame)
    button_frame.grid(row=1, column=0, columnspan=2, pady=20)
    
    ttk.Button(button_frame, text="Eliminar", command=eliminar).pack(side='left', padx=10)
    ttk.Button(button_frame, text="Cancelar", command=win.destroy).pack(side='left', padx=10)
