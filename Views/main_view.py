import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

# Placeholder functions for commands that will be implemented in the controllers
def placeholder_command():
    print("Command not implemented yet")

# ---------------------- MENÚ PRINCIPAL ADMIN ----------------------
def abrir_menu_principal_admin(usuario, abrir_menu_empleados_func, abrir_menu_doctores_func):
    global ventana_menu_admin, bg_image_admin
    
    ventana_menu_admin = tk.Tk()
    ventana_menu_admin.title("Sistema - Menú Principal Administrador")
    ventana_menu_admin.geometry("800x600")
    
    try:
        image = Image.open("fondo_nucleo.png")
        image = image.resize((800, 600), Image.Resampling.LANCZOS)
        bg_image_admin = ImageTk.PhotoImage(image)
        
        background_label = tk.Label(ventana_menu_admin, image=bg_image_admin)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print(f"Error cargando imagen de fondo: {e}")
        ventana_menu_admin.configure(bg='#2c3e50')
    
    main_frame = tk.Frame(ventana_menu_admin, bg='white', relief='raised', bd=3)
    main_frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=350)

    saludo_frame = tk.Frame(main_frame, bg='white')
    saludo_frame.pack(anchor='nw', fill='x', pady=(0, 10))
    
    ttk.Label(saludo_frame, text=f"Administrador: {usuario}", 
              font=("Arial", 12, "bold"), 
              background='white',
              foreground='#2c3e50').pack(side='left')

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

    botones_frame = tk.Frame(main_frame, bg='white')
    botones_frame.pack(pady=20)
    
    estilo_botones = ttk.Style()
    estilo_botones.configure('Botones.TButton', font=('Arial', 10), width=25)
    
    ttk.Button(botones_frame, text="Empleados", 
               style='Botones.TButton',
               command=abrir_menu_empleados_func).pack(pady=10)
    ttk.Button(botones_frame, text="Doctores", 
               style='Botones.TButton',
               command=abrir_menu_doctores_func).pack(pady=10)
    ttk.Button(botones_frame, text="Salir", 
               style='Botones.TButton',
               command=ventana_menu_admin.destroy).pack(pady=10)
    
    pie_frame = tk.Frame(main_frame, bg='#ecf0f1', height=40)
    pie_frame.pack(fill='x', side='bottom')
    pie_frame.pack_propagate(False)
    
    ttk.Label(pie_frame, text="Sistema de Gestión Hospitalaria v1.0", 
              font=("Arial", 8), 
              background='#ecf0f1',
              foreground='#7f8c8d').pack(expand=True)

    ventana_menu_admin.mainloop()

# ---------------------- MENÚ PRINCIPAL EMPLEADO ----------------------
def abrir_menu_principal_empleado(codigo_empleado, nombre_empleado, abrir_gestion_pacientes_func):
    global ventana_menu_empleado, bg_image_empleado
    
    ventana_menu_empleado = tk.Tk()
    ventana_menu_empleado.title("Sistema - Menú Principal Empleado")
    ventana_menu_empleado.geometry("800x600")
    
    try:
        image = Image.open("fondo_nucleo.png")
        image = image.resize((800, 600), Image.Resampling.LANCZOS)
        bg_image_empleado = ImageTk.PhotoImage(image)
        
        background_label = tk.Label(ventana_menu_empleado, image=bg_image_empleado)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print(f"Error cargando imagen de fondo: {e}")
        ventana_menu_empleado.configure(bg='#2c3e50')
    
    main_frame = tk.Frame(ventana_menu_empleado, bg='white', relief='raised', bd=3)
    main_frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=350)

    saludo_frame = tk.Frame(main_frame, bg='white')
    saludo_frame.pack(anchor='nw', fill='x', pady=(0, 10))
    
    ttk.Label(saludo_frame, text=f"Hola, {nombre_empleado}", 
              font=("Arial", 12, "bold"), 
              background='white',
              foreground='#2c3e50').pack(side='left')

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

    botones_frame = tk.Frame(main_frame, bg='white')
    botones_frame.pack(pady=20)
    
    ttk.Button(botones_frame, text="Administrar pacientes", width=25, 
               command=abrir_gestion_pacientes_func).pack(pady=8)
    ttk.Button(botones_frame, text="Administrar citas", width=25, 
               command=menu_citas_no_disponible).pack(pady=8)
    ttk.Button(botones_frame, text="Administrar medicamentos", width=25, 
               command=menu_medicamentos_no_disponible).pack(pady=8)
    ttk.Button(botones_frame, text="Salir", width=25, 
               command=ventana_menu_empleado.destroy).pack(pady=8)
    
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

# ---------------------- INICIO (VENTANA LOGIN) ----------------------
def crear_ventana_login(login_func):
    ventana_login = tk.Tk()
    ventana_login.title("Núcleo Diagnóstico - Sistema de Login")
    ventana_login.geometry("450x350")
    ventana_login.resizable(False, False)
    ventana_login.configure(bg='#ecf0f1')

    login_frame = tk.Frame(ventana_login, bg='white', relief='raised', bd=2)
    login_frame.place(relx=0.5, rely=0.5, anchor='center')

    ttk.Label(login_frame, text="Inicio de Sesión",
              font=("Arial", 16, "bold"),
              background='white',
              foreground='#34495e').grid(row=0, column=0, columnspan=2, pady=25, padx=40)

    ttk.Label(login_frame, text="Usuario/Código:", background='white', font=("Arial", 10)).grid(row=1, column=0, padx=(20, 5), pady=10, sticky="e")
    entry_usuario = ttk.Entry(login_frame, width=25, font=("Arial", 10))
    entry_usuario.grid(row=1, column=1, padx=(0, 20), pady=10)

    ttk.Label(login_frame, text="Contraseña:", background='white', font=("Arial", 10)).grid(row=2, column=0, padx=(20, 5), pady=10, sticky="e")
    entry_contra = ttk.Entry(login_frame, show="*", width=25, font=("Arial", 10))
    entry_contra.grid(row=2, column=1, padx=(0, 20), pady=10)

    style = ttk.Style()
    style.configure('Login.TButton', font=('Arial', 10, 'bold'))

    # We pass the entries to the login function
    ttk.Button(login_frame, text="Iniciar sesión", style='Login.TButton', command=lambda: login_func(entry_usuario.get(), entry_contra.get(), ventana_login)).grid(row=3, column=0, columnspan=2, pady=25)

    ventana_login.mainloop()
