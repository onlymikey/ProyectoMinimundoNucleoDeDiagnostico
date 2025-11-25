import tkinter as tk
from tkinter import ttk, messagebox

def abrir_menu_doctores(controller):
    ventana_doctores = tk.Toplevel()
    ventana_doctores.title("Sistema - Doctores")
    ventana_doctores.geometry("400x400")
    ventana_doctores.configure(bg='#ecf0f1')
    
    main_frame = tk.Frame(ventana_doctores, bg='white', relief='raised', bd=2)
    main_frame.pack(expand=True, fill='both', padx=20, pady=20)

    ttk.Label(main_frame, text="Gestión de Doctores", 
              font=("Arial", 16, "bold"),
              background='white').pack(pady=20)

    botones_frame = tk.Frame(main_frame, bg='white')
    botones_frame.pack(expand=True)
    
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
    win = tk.Toplevel()
    win.title("Mostrar doctor por ID")
    win.geometry("500x300")

    main_frame = tk.Frame(win)
    main_frame.pack(fill='both', expand=True, padx=20, pady=20)

    ttk.Label(main_frame, text="ID del doctor:").grid(row=0, column=0, padx=8, pady=8)
    id_entry = ttk.Entry(main_frame, width=20)
    id_entry.grid(row=0, column=1, padx=8, pady=8)

    def buscar():
        id_val = id_entry.get().strip()
        doctor = controller.mostrar_doctor_por_id(id_val)
        
        if doctor:
            result_frame = tk.Frame(main_frame, relief='sunken', bd=2)
            result_frame.grid(row=2, column=0, columnspan=2, padx=8, pady=8, sticky='we')
            
            txt = tk.Text(result_frame, width=60, height=8, wrap='word')
            txt.pack(padx=5, pady=5)
            txt.delete("1.0", tk.END)
            txt.insert(tk.END, f"ID: {doctor[0]}\nNombre: {doctor[1]}\nDirección: {doctor[2]}\nTeléfono: {doctor[3]}\nFecha Nac: {doctor[4]}\nSexo: {doctor[5]}\nEspecialidad: {doctor[6]}")
            txt.config(state="disabled")

    ttk.Button(main_frame, text="Buscar", command=buscar).grid(row=1, column=0, columnspan=2, pady=10)

def ventana_mostrar_todos_doctores(controller):
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

    doctores = controller.mostrar_todos_los_doctores()
    if doctores:
        for r in doctores:
            tree.insert("", tk.END, values=r)

def ventana_modificar_doctor(controller):
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
        doctor = controller.mostrar_doctor_por_id(id_val)

        if doctor:
            labels = ["Nombre", "Dirección", "Teléfono", "Fecha Nac (YYYY-MM-DD)", "Sexo", "Especialidad", "Contraseña"]
            entries = {}
            for i, text in enumerate(labels):
                ttk.Label(main_frame, text=text+":").grid(row=2+i, column=0, padx=8, pady=6, sticky="e")
                ent = ttk.Entry(main_frame, width=40, show="*" if "Contraseña" in text else "")
                ent.grid(row=2+i, column=1, padx=8, pady=6)
                entries[text] = ent

            entries["Nombre"].insert(0, doctor[1])
            entries["Dirección"].insert(0, doctor[2])
            entries["Teléfono"].insert(0, doctor[3])
            entries["Fecha Nac (YYYY-MM-DD)"].insert(0, doctor[4] if doctor[4] else "")
            entries["Sexo"].insert(0, doctor[5] if doctor[5] else "")
            entries["Especialidad"].insert(0, doctor[6] if doctor[6] else "")
            entries["Contraseña"].insert(0, doctor[7] if doctor[7] else "")

            def guardar_cambios():
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

    ttk.Button(main_frame, text="Cargar", command=cargar).grid(row=1, column=0, columnspan=2, pady=10)

def ventana_eliminar_doctor(controller):
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
        controller.eliminar_doctor(id_val, win)

    button_frame = tk.Frame(main_frame)
    button_frame.grid(row=1, column=0, columnspan=2, pady=20)
    
    ttk.Button(button_frame, text="Eliminar", command=eliminar).pack(side='left', padx=10)
    ttk.Button(button_frame, text="Cancelar", command=win.destroy).pack(side='left', padx=10)
