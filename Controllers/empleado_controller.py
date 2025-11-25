from tkinter import messagebox
from decimal import Decimal
import DAOS.empleado_dao as empleado_dao
from Views.empleado_view import (
    abrir_menu_empleados,
    ventana_registrar_empleado,
    ventana_mostrar_empleado_por_id,
    ventana_mostrar_todos_empleados,
    ventana_modificar_empleado,
    ventana_eliminar_empleado
)

class EmpleadoController:
    def __init__(self):
        pass

    def mostrar_menu_empleados(self):
        abrir_menu_empleados(self)

    def registrar_empleado(self, datos, win):
        try:
            if not datos["nombre"]:
                messagebox.showwarning("Validación", "El nombre es obligatorio")
                return

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
        try:
            return empleado_dao.mostrar_todos_los_empleados()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return None

    def modificar_empleado(self, datos, win):
        try:
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
        if not id_val.isdigit():
            messagebox.showwarning("Validación", "ID inválido")
            return

        if not messagebox.askyesno("Confirmar", f"¿Eliminar empleado con ID {id_val}?"):
            return

        try:
            cambios = empleado_dao.eliminar_empleado(id_val)
            if cambios == 0:
                messagebox.showinfo("Resultado", "No se encontró el empleado")
            else:
                messagebox.showinfo("Éxito", "Empleado eliminado correctamente")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
