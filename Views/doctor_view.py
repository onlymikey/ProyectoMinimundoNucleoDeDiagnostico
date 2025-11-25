# Este módulo define todas las ventanas y componentes de la interfaz de usuario
# relacionados con la gestión de doctores. Utiliza tkinter para crear las ventanas.

import tkinter as tk
from tkinter import ttk, messagebox

def abrir_menu_doctores(controller):
    """
    Crea y muestra el menú principal para la gestión de doctores.

    Args:
        controller: La instancia del controlador de doctores que manejará la lógica de los botones.
    """
    # Toplevel es como una nueva ventana que depende de la ventana principal.
    ventana_doctores = tk.Toplevel()
    ventana_doctores.title("Sistema - Doctores")
    ventana_doctores.geometry("400x400")
    ventana_doctores.configure(bg='#ecf0f1')
    
    # Frame principal para organizar el contenido.
    main_frame = tk.Frame(ventana_doctores, bg='white', relief='raised', bd=2)
    main_frame.pack(expand=True, fill='both', padx=20, pady=20)

    ttk.Label(main_frame, text="Gestión de Doctores", 
              font=("Arial", 16, "bold"),
              background='white').pack(pady=20)

    # Frame para los botones de acción.
    botones_frame = tk.Frame(main_frame, bg='white')
    botones_frame.pack(expand=True)
    
    # Cada botón llama a una función que abre una nueva ventana para la acción correspondiente.
    # Se usa 'lambda' para pasar el controlador a la función que abre la ventana.
    ttk.Button(botones_frame, text="Registrar doctor", width=30, 
               command=lambda: ventana_registrar_doctor(controller)).pack(pady=8)
    ttk.Button(botones_frame, text="Mostrar doctor por ID", width=30, 
               command=lambda: ventana_mostrar_doctor_por_id(controller)).pack(pady=8)
    ttk.Button(botones_frame, text="Mostrar todos los doctores", width=30, 
               command=lambda: ventana_mostrar_todos_doctores(controller)).pack(pady=8)
    ttk.Button(botones_frame, text="Modificar doctor", width=30, 
               command=lambda: ventana_modificar_doctor(controller)).pack(pady=8)
    ttk.Button(botones_frame, text="Eliminar doctor", width=30, 
               command=lambda: ventana_eliminar_doctor(controller)).pack(pady=8)
    ttk.Button(botones_frame, text="Cerrar", width=30, 
               command=ventana_doctores.destroy).pack(pady=15)

def ventana_registrar_doctor(controller):
    """
    Crea la ventana con el formulario para registrar un nuevo doctor.

    Args:
        controller: La instancia del controlador de doctores.
    """
    win = tk.Toplevel()
    win.title("Registrar doctor")
    win.geometry("500x450")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=10, pady=10)

    labels = ["Nombre", "Dirección", "Teléfono", "Fecha Nac (YYYY-MM-DD)", "Sexo", "Especialidad", "Contraseña"]
    entries = {}

    # Crea etiquetas y campos de entrada para cada dato del doctor.
    for i, text in enumerate(labels):
        ttk.Label(main_frame, text=text+":").grid(row=i, column=0, padx=8, pady=8, sticky="e")
        # Oculta la entrada de texto para la contraseña.
        ent = ttk.Entry(main_frame, width=40, show="*" if "Contraseña" in text else "")
        ent.grid(row=i, column=1, padx=8, pady=8)
        entries[text] = ent

    def guardar():
        """Recopila los datos del formulario y los envía al controlador para ser guardados."""
        datos = {
            "nombre": entries["Nombre"].get().strip(),
            "direccion": entries["Dirección"].get().strip(),
            "telefono": entries["Teléfono"].get().strip(),
            "fecha_nac": entries["Fecha Nac (YYYY-MM-DD)"].get().strip(),
            "sexo": entries["Sexo"].get().strip(),
            "especialidad": entries["Especialidad"].get().strip(),
            "contrasena": entries["Contraseña"].get().strip()
        }
        controller.registrar_doctor(datos, win)

    button_frame = tk.Frame(main_frame)
    button_frame.grid(row=len(labels), column=0, columnspan=2, pady=20)
    
    ttk.Button(button_frame, text="Guardar", command=guardar).pack(side='left', padx=10)
    ttk.Button(button_frame, text="Cancelar", command=win.destroy).pack(side='left', padx=10)

def ventana_mostrar_doctor_por_id(controller):
    """
    Crea la ventana para buscar un doctor por su ID y mostrar su información.

    Args:
        controller: La instancia del controlador de doctores.
    """
    win = tk.Toplevel()
    win.title("Mostrar doctor por ID")
    win.geometry("500x300")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=20, pady=20)

    ttk.Label(main_frame, text="ID del doctor:").grid(row=0, column=0, padx=8, pady=8)
    id_entry = ttk.Entry(main_frame, width=20)
    id_entry.grid(row=0, column=1, padx=8, pady=8)

    def buscar():
        """Llama al controlador para buscar el doctor y muestra los resultados."""
        id_val = id_entry.get().strip()
        doctor = controller.mostrar_doctor_por_id(id_val)
        
        if doctor:
            # Frame para mostrar los resultados de la búsqueda.
            result_frame = tk.Frame(main_frame, relief='sunken', bd=2)
            result_frame.grid(row=2, column=0, columnspan=2, padx=8, pady=8, sticky='we')
            
            # Widget de texto para mostrar la información del doctor.
            txt = tk.Text(result_frame, width=60, height=8, wrap='word')
            txt.pack(padx=5, pady=5)
            txt.delete("1.0", tk.END)
            txt.insert(tk.END, f"ID: {doctor[0]}\nNombre: {doctor[1]}\nDirección: {doctor[2]}\nTeléfono: {doctor[3]}\nFecha Nac: {doctor[4]}\nSexo: {doctor[5]}\nEspecialidad: {doctor[6]}")
            txt.config(state="disabled") # Hace el texto de solo lectura.

    ttk.Button(main_frame, text="Buscar", command=buscar).grid(row=1, column=0, columnspan=2, pady=10)

def ventana_mostrar_todos_doctores(controller):
    """
    Crea una ventana que muestra todos los doctores en una tabla (Treeview).

    Args:
        controller: La instancia del controlador de doctores.
    """
    win = tk.Toplevel()
    win.title("Todos los doctores")
    win.geometry("900x400")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=10, pady=10)

    # Define las columnas para el Treeview.
    cols = ("codigo","nombre","direccion","telefono","fecha_nac","sexo","especialidad")
    tree = ttk.Treeview(main_frame, columns=cols, show="headings")
    
    # Configura las cabeceras y el ancho de las columnas.
    for c in cols:
        tree.heading(c, text=c.capitalize())
        tree.column(c, width=110, anchor="center")

    # Agrega una barra de desplazamiento vertical.
    vsb = ttk.Scrollbar(main_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    
    tree.pack(side='left', fill='both', expand=True)
    vsb.pack(side='right', fill='y')

    # Obtiene los datos del controlador y los inserta en la tabla.
    doctores = controller.mostrar_todos_los_doctores()
    if doctores:
        for r in doctores:
            tree.insert("", tk.END, values=r)

def ventana_modificar_doctor(controller):
    """
    Crea la ventana para modificar un doctor. Primero se busca por ID y luego se cargan los datos.

    Args:
        controller: La instancia del controlador de doctores.
    """
    win = tk.Toplevel()
    win.title("Modificar doctor")
    win.geometry("500x550")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=10, pady=10)

    # Campo para ingresar el ID del doctor a modificar.
    ttk.Label(main_frame, text="ID a modificar:").grid(row=0, column=0, padx=8, pady=8)
    id_entry = ttk.Entry(main_frame, width=20)
    id_entry.grid(row=0, column=1, padx=8, pady=8)

    def cargar():
        """Busca el doctor por ID y, si lo encuentra, crea el formulario para editar sus datos."""
        id_val = id_entry.get().strip()
        doctor = controller.mostrar_doctor_por_id(id_val)

        if doctor:
            # Crea el formulario de edición dinámicamente una vez que se carga el doctor.
            labels = ["Nombre", "Dirección", "Teléfono", "Fecha Nac (YYYY-MM-DD)", "Sexo", "Especialidad", "Contraseña"]
            entries = {}
            for i, text in enumerate(labels):
                ttk.Label(main_frame, text=text+":").grid(row=2+i, column=0, padx=8, pady=6, sticky="e")
                ent = ttk.Entry(main_frame, width=40, show="*" if "Contraseña" in text else "")
                ent.grid(row=2+i, column=1, padx=8, pady=6)
                entries[text] = ent

            # Llena los campos del formulario con los datos actuales del doctor.
            entries["Nombre"].insert(0, doctor[1])
            entries["Dirección"].insert(0, doctor[2])
            entries["Teléfono"].insert(0, doctor[3])
            entries["Fecha Nac (YYYY-MM-DD)"].insert(0, doctor[4] if doctor[4] else "")
            entries["Sexo"].insert(0, doctor[5] if doctor[5] else "")
            entries["Especialidad"].insert(0, doctor[6] if doctor[6] else "")
            entries["Contraseña"].insert(0, doctor[7] if doctor[7] else "")

            def guardar_cambios():
                """Recopila los datos modificados y los envía al controlador."""
                datos = {
                    "nombre": entries["Nombre"].get().strip(),
                    "direccion": entries["Dirección"].get().strip(),
                    "telefono": entries["Teléfono"].get().strip(),
                    "fecha_nac": entries["Fecha Nac (YYYY-MM-DD)"].get().strip(),
                    "sexo": entries["Sexo"].get().strip(),
                    "especialidad": entries["Especialidad"].get().strip(),
                    "contrasena": entries["Contraseña"].get().strip(),
                    "codigo": id_val
                }
                controller.modificar_doctor(datos, win)

            button_frame = tk.Frame(main_frame)
            button_frame.grid(row=2+len(labels), column=0, columnspan=2, pady=20)
            
            ttk.Button(button_frame, text="Guardar cambios", command=guardar_cambios).pack(side='left', padx=10)
            ttk.Button(button_frame, text="Cancelar", command=win.destroy).pack(side='left', padx=10)

    # Botón para iniciar la búsqueda y carga de datos.
    ttk.Button(main_frame, text="Cargar", command=cargar).grid(row=1, column=0, columnspan=2, pady=10)

def ventana_eliminar_doctor(controller):
    """
    Crea la ventana para eliminar un doctor por su ID.

    Args:
        controller: La instancia del controlador de doctores.
    """
    win = tk.Toplevel()
    win.title("Eliminar doctor")
    win.geometry("400x200")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=20, pady=20)

    ttk.Label(main_frame, text="ID a eliminar:").grid(row=0, column=0, padx=8, pady=8)
    id_entry = ttk.Entry(main_frame, width=20)
    id_entry.grid(row=0, column=1, padx=8, pady=8)

    def eliminar():
        """Llama al controlador para ejecutar la eliminación."""
        id_val = id_entry.get().strip()
        controller.eliminar_doctor(id_val, win)

    button_frame = tk.Frame(main_frame)
    button_frame.grid(row=1, column=0, columnspan=2, pady=20)
    
    ttk.Button(button_frame, text="Eliminar", command=eliminar).pack(side='left', padx=10)
    ttk.Button(button_frame, text="Cancelar", command=win.destroy).pack(side='left', padx=10)
