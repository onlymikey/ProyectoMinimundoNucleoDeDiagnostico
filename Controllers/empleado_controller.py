# Este módulo define el controlador para las operaciones relacionadas con los empleados.
# Funciona como un puente entre las vistas de empleado y el DAO de empleado,
# gestionando la lógica de negocio y las validaciones de datos necesarias.

from tkinter import messagebox
from decimal import Decimal
import DAOS.empleado_dao as empleado_dao
from Views.empleado_view import (
    abrir_menu_empleados,
    # Las siguientes vistas son invocadas por los métodos de este controlador.
    # No se llaman directamente, pero es útil conocer su origen.
    # ventana_registrar_empleado,
    # ventana_mostrar_empleado_por_id,
    # ventana_mostrar_todos_empleados,
    # ventana_modificar_empleado,
    # ventana_eliminar_empleado
)

class EmpleadoController:
    """
    Controlador para la lógica de negocio de la gestión de empleados.
    """
    def __init__(self):
        """Inicializa el controlador de empleados."""
        pass

    def mostrar_menu_empleados(self):
        """Abre la ventana del menú de gestión de empleados."""
        abrir_menu_empleados(self)

    def registrar_empleado(self, datos, win):
        """
        Valida los datos de entrada y solicita al DAO el registro de un nuevo empleado.

        Args:
            datos (dict): Diccionario con la información del empleado.
            win (tk.Toplevel): La ventana de registro, para cerrarla después de la operación.
        """
        try:
            # Validación de que el nombre no esté vacío.
            if not datos["nombre"]:
                messagebox.showwarning("Validación", "El nombre es obligatorio")
                return

            # Validación y conversión del sueldo a tipo Decimal.
            try:
                sueldo_val = Decimal(datos["sueldo"]) if datos["sueldo"] != "" else Decimal("0.00")
            except Exception:
                messagebox.showwarning("Validación", "Sueldo inválido")
                return

            datos["sueldo"] = sueldo_val

            empleado_dao.registrar_empleado(datos)
            messagebox.showinfo("Éxito", "Empleado registrado correctamente")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar: {e}")

    def mostrar_empleado_por_id(self, id_val):
        """
        Busca un empleado por su ID a través del DAO.

        Args:
            id_val (str): El ID del empleado a buscar.

        Returns:
            tuple or None: Una tupla con los datos del empleado si se encuentra, de lo contrario None.
        """
        try:
            if not id_val.isdigit():
                messagebox.showwarning("Validación", "ID inválido")
                return None
            
            empleado = empleado_dao.mostrar_empleado_por_id(id_val)

            if not empleado:
                messagebox.showinfo("Resultado", "No se encontró el empleado con ese ID")
            
            return empleado
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return None

    def mostrar_todos_los_empleados(self):
        """
        Solicita y devuelve la lista completa de empleados desde el DAO.

        Returns:
            list or None: Una lista de tuplas con los empleados, o None si hay un error.
        """
        try:
            return empleado_dao.mostrar_todos_los_empleados()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return None

    def modificar_empleado(self, datos, win):
        """
        Valida los datos y solicita al DAO la modificación de un empleado.

        Args:
            datos (dict): Diccionario con los datos actualizados del empleado.
            win (tk.Toplevel): La ventana de modificación para cerrarla post-operación.
        """
        try:
            # Validación y conversión del campo sueldo.
            try:
                sueldo_val = Decimal(datos["sueldo"]) if datos["sueldo"] != "" else None
            except Exception:
                messagebox.showwarning("Validación", "Sueldo inválido")
                return

            datos["sueldo"] = sueldo_val

            empleado_dao.modificar_empleado(datos)
            messagebox.showinfo("Éxito", "Empleado modificado correctamente")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar_empleado(self, id_val, win):
        """
        Solicita al DAO la eliminación de un empleado, previa confirmación.

        Args:
            id_val (str): El ID del empleado a eliminar.
            win (tk.Toplevel): La ventana de eliminación.
        """
        if not id_val.isdigit():
            messagebox.showwarning("Validación", "ID inválido")
            return

        # Confirmación del usuario antes de eliminar.
        if not messagebox.askyesno("Confirmar", f"¿Eliminar empleado con ID {id_val}?"):
            return

        try:
            # Llama al DAO y verifica si la eliminación fue exitosa.
            cambios = empleado_dao.eliminar_empleado(id_val)
            if cambios == 0:
                messagebox.showinfo("Resultado", "No se encontró el empleado")
            else:
                messagebox.showinfo("Éxito", "Empleado eliminado correctamente")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
