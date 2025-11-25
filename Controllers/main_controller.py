# Este módulo actúa como el controlador principal de la aplicación.
# Se encarga de la lógica de autenticación de usuarios y de la navegación
# inicial hacia los menús correspondientes según el rol del usuario.

from tkinter import messagebox
from Views.main_view import abrir_menu_principal_admin, abrir_menu_principal_empleado
from DAOS.db import conectar
from Controllers.empleado_controller import EmpleadoController
from Controllers.doctor_controller import DoctorController
from Controllers.paciente_controller import PacienteController

def validar_login(usuario, contra, ventana_login):
    """
    Valida las credenciales del usuario y le da acceso al menú correspondiente.

    Esta función es llamada por la vista de login. Comprueba si las credenciales
    corresponden a un administrador o a un empleado registrado en la base de datos.

    Args:
        usuario (str): El nombre de usuario o código de empleado ingresado.
        contra (str): La contraseña ingresada.
        ventana_login (tk.Tk): La instancia de la ventana de login, para poder cerrarla si el login es exitoso.
    """
    # Limpia espacios en blanco de las entradas del usuario.
    usuario = usuario.strip()
    contra = contra.strip()

    # Caso especial para el administrador con credenciales hardcodeadas.
    if usuario == "admin" and contra == "12345":
        messagebox.showinfo("Acceso permitido", "Bienvenido administrador")
        ventana_login.destroy()  # Cierra la ventana de login.
        
        # Instancia los controladores que necesitará el menú de administrador.
        empleado_controller = EmpleadoController()
        doctor_controller = DoctorController()
        
        # Abre el menú principal de administrador, pasando las funciones de los controladores.
        abrir_menu_principal_admin(
            usuario, 
            empleado_controller.mostrar_menu_empleados, 
            doctor_controller.mostrar_menu_doctores
        )
    else:
        # Si no es el admin, intenta validar como empleado contra la base de datos.
        try:
            conn = conectar()
            cur = conn.cursor()
            
            # Busca un empleado que coincida con el código y contraseña.
            # NOTA: En una aplicación real, las contraseñas deben ser hasheadas y verificadas, no almacenadas en texto plano.
            cur.execute("SELECT codigo, nombre FROM empleado WHERE codigo = %s AND contrasena = %s", 
                       (usuario, contra))
            empleado = cur.fetchone()  # Obtiene el primer resultado.
            
            cur.close()
            conn.close()

            if empleado:
                # Si se encontró un empleado, se le da la bienvenida.
                messagebox.showinfo("Acceso permitido", f"Bienvenido empleado: {empleado[1]}")
                ventana_login.destroy() # Cierra la ventana de login.
                
                # Instancia el controlador de pacientes.
                paciente_controller = PacienteController()

                # Abre el menú de empleado, pasando los datos del empleado y la función del controlador de pacientes.
                abrir_menu_principal_empleado(
                    empleado[0],  # Código del empleado
                    empleado[1],  # Nombre del empleado
                    paciente_controller.mostrar_gestion_pacientes
                )
            else:
                # Si no se encontró el empleado, se muestra un error.
                messagebox.showerror("Acceso denegado", "Código o contraseña incorrectos")
        except Exception as e:
            # Manejo de errores en caso de problemas con la base de datos.
            messagebox.showerror("Error", f"No se pudo validar el empleado: {e}")
