import tkinter as tk
from tkinter import ttk, messagebox
from decimal import Decimal

# ---------------------- GESTIÓN DE PACIENTES (PARA EMPLEADOS) ----------------------
def abrir_gestion_pacientes(controller):
    ventana_pacientes = tk.Toplevel()
    ventana_pacientes.title("Gestión de Pacientes")
    ventana_pacientes.geometry("400x400")
    ventana_pacientes.configure(bg='#ecf0f1')

    main_frame = tk.Frame(ventana_pacientes, bg='white', relief='raised', bd=2)
    main_frame.pack(expand=True, fill='both', padx=20, pady=20)

    ttk.Label(main_frame, text="Gestión de Pacientes", 
              font=("Arial", 16, "bold"),
              background='white').pack(pady=20)

    botones_frame = tk.Frame(main_frame, bg='white')
    botones_frame.pack(expand=True)

    ttk.Button(botones_frame, text="Registrar paciente", width=30, 
               command=lambda: ventana_registrar_paciente(controller)).pack(pady=8)
    ttk.Button(botones_frame, text="Mostrar paciente por ID", width=30, 
               command=lambda: ventana_mostrar_paciente_por_id(controller)).pack(pady=8)
    ttk.Button(botones_frame, text="Mostrar todos los pacientes", width=30, 
               command=lambda: ventana_mostrar_todos_pacientes(controller)).pack(pady=8)
    ttk.Button(botones_frame, text="Modificar paciente", width=30, 
               command=lambda: ventana_modificar_paciente(controller)).pack(pady=8)
    ttk.Button(botones_frame, text="Eliminar paciente", width=30, 
               command=lambda: ventana_eliminar_paciente(controller)).pack(pady=8)
    ttk.Button(botones_frame, text="Cerrar", width=30, 
               command=ventana_pacientes.destroy).pack(pady=15)

# ---------------------- REGISTRAR PACIENTE ----------------------
def ventana_registrar_paciente(controller):
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
        datos = {
            "nombre": entries["Nombre"].get().strip(),
            "direccion": entries["Dirección"].get().strip(),
            "telefono": entries["Teléfono"].get().strip(),
            "fecha_nac": entries["Fecha Nac (YYYY-MM-DD)"].get().strip(),
            "sexo": entries["Sexo"].get().strip(),
            "edad": entries["Edad"].get().strip(),
            "estatura": entries["Estatura"].get().strip()
        }
        controller.registrar_paciente(datos, win)

    button_frame = tk.Frame(main_frame)
    button_frame.grid(row=len(labels), column=0, columnspan=2, pady=20)
    
    ttk.Button(button_frame, text="Guardar", command=guardar).pack(side='left', padx=10)
    ttk.Button(button_frame, text="Cancelar", command=win.destroy).pack(side='left', padx=10)

# ---------------------- MOSTRAR PACIENTE POR ID ----------------------
def ventana_mostrar_paciente_por_id(controller):
    win = tk.Toplevel()
    win.title("Mostrar paciente por ID")
    win.geometry("500x300")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=20, pady=20)

    ttk.Label(main_frame, text="ID del paciente:").grid(row=0, column=0, padx=8, pady=8)
    id_entry = ttk.Entry(main_frame, width=20)
    id_entry.grid(row=0, column=1, padx=8, pady=8)

    def buscar():
        id_val = id_entry.get().strip()
        paciente = controller.mostrar_paciente_por_id(id_val)
        
        if paciente:
            result_frame = tk.Frame(main_frame, relief='sunken', bd=2)
            result_frame.grid(row=2, column=0, columnspan=2, padx=8, pady=8, sticky='we')
            
            txt = tk.Text(result_frame, width=60, height=8, wrap='word')
            txt.pack(padx=5, pady=5)
            txt.delete("1.0", tk.END)
            txt.insert(tk.END, f"ID: {paciente[0]}\nNombre: {paciente[1]}\nDirección: {paciente[2]}\nTeléfono: {paciente[3]}\nFecha Nac: {paciente[4]}\nSexo: {paciente[5]}\nEdad: {paciente[6]}\nEstatura: {paciente[7]}")
            txt.config(state="disabled")

    ttk.Button(main_frame, text="Buscar", command=buscar).grid(row=1, column=0, columnspan=2, pady=10)

# ---------------------- MOSTRAR TODOS LOS PACIENTES ----------------------
def ventana_mostrar_todos_pacientes(controller):
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

    pacientes = controller.mostrar_todos_los_pacientes()
    if pacientes:
        for r in pacientes:
            tree.insert("", tk.END, values=r)

# ---------------------- MODIFICAR PACIENTE ----------------------
def ventana_modificar_paciente(controller):
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
        paciente = controller.mostrar_paciente_por_id(id_val)

        if paciente:
            labels = ["Nombre", "Dirección", "Teléfono", "Fecha Nac (YYYY-MM-DD)", "Sexo", "Edad", "Estatura"]
            entries = {}
            for i, text in enumerate(labels):
                ttk.Label(main_frame, text=text+":").grid(row=2+i, column=0, padx=8, pady=6, sticky="e")
                ent = ttk.Entry(main_frame, width=40)
                ent.grid(row=2+i, column=1, padx=8, pady=6)
                entries[text] = ent

            entries["Nombre"].insert(0, paciente[1])
            entries["Dirección"].insert(0, paciente[2])
            entries["Teléfono"].insert(0, paciente[3])
            entries["Fecha Nac (YYYY-MM-DD)"].insert(0, paciente[4] if paciente[4] else "")
            entries["Sexo"].insert(0, paciente[5] if paciente[5] else "")
            entries["Edad"].insert(0, str(paciente[6]) if paciente[6] is not None else "")
            entries["Estatura"].insert(0, str(paciente[7]) if paciente[7] is not None else "")

            def guardar_cambios():
                datos = {
                    "nombre": entries["Nombre"].get().strip(),
                    "direccion": entries["Dirección"].get().strip(),
                    "telefono": entries["Teléfono"].get().strip(),
                    "fecha_nac": entries["Fecha Nac (YYYY-MM-DD)"].get().strip(),
                    "sexo": entries["Sexo"].get().strip(),
                    "edad": entries["Edad"].get().strip(),
                    "estatura": entries["Estatura"].get().strip(),
                    "codigo": id_val
                }
                controller.modificar_paciente(datos, win)

            button_frame = tk.Frame(main_frame)
            button_frame.grid(row=2+len(labels), column=0, columnspan=2, pady=20)
            
            ttk.Button(button_frame, text="Guardar cambios", command=guardar_cambios).pack(side='left', padx=10)
            ttk.Button(button_frame, text="Cancelar", command=win.destroy).pack(side='left', padx=10)

    ttk.Button(main_frame, text="Cargar", command=cargar).grid(row=1, column=0, columnspan=2, pady=10)

# ---------------------- ELIMINAR PACIENTE ----------------------
def ventana_eliminar_paciente(controller):
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
        controller.eliminar_paciente(id_val, win)

    button_frame = tk.Frame(main_frame)
    button_frame.grid(row=1, column=0, columnspan=2, pady=20)
    
    ttk.Button(button_frame, text="Eliminar", command=eliminar).pack(side='left', padx=10)
    ttk.Button(button_frame, text="Cancelar", command=win.destroy).pack(side='left', padx=10)
