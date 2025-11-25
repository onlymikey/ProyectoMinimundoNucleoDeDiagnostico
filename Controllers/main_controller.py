from tkinter import messagebox
from Views.main_view import abrir_menu_principal_admin, abrir_menu_principal_empleado
from DAOS.db import conectar
from Controllers.empleado_controller import EmpleadoController
from Controllers.doctor_controller import DoctorController
from Controllers.paciente_controller import PacienteController

def validar_login(usuario, contra, ventana_login):
    usuario = usuario.strip()
    contra = contra.strip()

    if usuario == "admin" and contra == "12345":
        messagebox.showinfo("Acceso permitido", "Bienvenido administrador")
        ventana_login.destroy()
        empleado_controller = EmpleadoController()
        doctor_controller = DoctorController()
        abrir_menu_principal_admin(
            usuario, 
            empleado_controller.mostrar_menu_empleados, 
            doctor_controller.mostrar_menu_doctores
        )
    else:
        try:
            conn = conectar()
            cur = conn.cursor()
            cur.execute("SELECT codigo, nombre FROM empleado WHERE codigo = %s AND contrasena = %s", 
                       (usuario, contra))
            empleado = cur.fetchone()
            cur.close()
            conn.close()

            if empleado:
                messagebox.showinfo("Acceso permitido", f"Bienvenido empleado: {empleado[1]}")
                ventana_login.destroy()
                paciente_controller = PacienteController()
                abrir_menu_principal_empleado(
                    empleado[0], 
                    empleado[1], 
                    paciente_controller.mostrar_gestion_pacientes
                )
            else:
                messagebox.showerror("Acceso denegado", "Código o contraseña incorrectos")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo validar el empleado: {e}")
