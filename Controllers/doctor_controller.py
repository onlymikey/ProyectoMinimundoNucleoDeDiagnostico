# Este módulo define el controlador para las operaciones relacionadas con los doctores.
# Sirve como intermediario entre las vistas de doctores y el DAO de doctores,
# manejando la lógica de negocio y la validación de datos.

from tkinter import messagebox
import DAOS.doctor_dao as doctor_dao
from Views.doctor_view import (
    abrir_menu_doctores,
    # Las siguientes ventanas son abiertas por los métodos de este controlador.
    # No se llaman directamente aquí, pero es útil saber de dónde vienen.
    # ventana_registrar_doctor,
    # ventana_mostrar_doctor_por_id,
    # ventana_mostrar_todos_doctores,
    # ventana_modificar_doctor,
    # ventana_eliminar_doctor
)

class DoctorController:
    """
    Controlador que encapsula la lógica de negocio para la gestión de doctores.
    """
    def __init__(self):
        """Inicializa el controlador de doctores."""
        pass

    def mostrar_menu_doctores(self):
        """Abre la ventana del menú de gestión de doctores."""
        abrir_menu_doctores(self)

    def registrar_doctor(self, datos, win):
        """
        Valida los datos y solicita al DAO que registre un nuevo doctor.

        Args:
            datos (dict): Un diccionario con la información del doctor a registrar.
            win (tk.Toplevel): La ventana de registro, para poder cerrarla tras el éxito.
        """
        try:
            # Validación simple: el nombre es un campo obligatorio.
            if not datos["nombre"]:
                messagebox.showwarning("Validación", "El nombre es obligatorio")
                return

            doctor_dao.registrar_doctor(datos)
            messagebox.showinfo("Éxito", "Doctor registrado correctamente")
            win.destroy()  # Cierra la ventana de registro.
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar: {e}")

    def mostrar_doctor_por_id(self, id_val):
        """
        Busca un doctor por su ID y devuelve el resultado.

        Args:
            id_val (str): El ID del doctor a buscar.

        Returns:
            tuple or None: Una tupla con los datos del doctor si se encuentra, de lo contrario None.
        """
        try:
            if not id_val.isdigit():
                messagebox.showwarning("Validación", "ID inválido")
                return None
            
            doctor = doctor_dao.mostrar_doctor_por_id(id_val)

            if not doctor:
                messagebox.showinfo("Resultado", "No se encontró el doctor con ese ID")
            
            return doctor
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return None

    def mostrar_todos_los_doctores(self):
        """
        Solicita al DAO la lista de todos los doctores.

        Returns:
            list or None: Una lista de tuplas con los datos de todos los doctores, o None si ocurre un error.
        """
        try:
            return doctor_dao.mostrar_todos_los_doctores()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return None

    def modificar_doctor(self, datos, win):
        """
        Valida los datos y solicita al DAO que modifique un doctor existente.

        Args:
            datos (dict): Un diccionario con los datos actualizados del doctor.
            win (tk.Toplevel): La ventana de modificación, para cerrarla tras el éxito.
        """
        try:
            doctor_dao.modificar_doctor(datos)
            messagebox.showinfo("Éxito", "Doctor modificado correctamente")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar_doctor(self, id_val, win):
        """
        Solicita al DAO que elimine un doctor por su ID, con confirmación previa.

        Args:
            id_val (str): El ID del doctor a eliminar.
            win (tk.Toplevel): La ventana de eliminación, para cerrarla tras el éxito.
        """
        if not id_val.isdigit():
            messagebox.showwarning("Validación", "ID inválido")
            return

        # Pide confirmación al usuario antes de proceder con la eliminación.
        if not messagebox.askyesno("Confirmar", f"¿Eliminar doctor con ID {id_val}?"):
            return

        try:
            # Llama al DAO para eliminar y comprueba si se afectaron filas.
            cambios = doctor_dao.eliminar_doctor(id_val)
            if cambios == 0:
                messagebox.showinfo("Resultado", "No se encontró el doctor")
            else:
                messagebox.showinfo("Éxito", "Doctor eliminado correctamente")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
