from tkinter import messagebox
import DAOS.doctor_dao as doctor_dao
from Views.doctor_view import (
    abrir_menu_doctores,
    ventana_registrar_doctor,
    ventana_mostrar_doctor_por_id,
    ventana_mostrar_todos_doctores,
    ventana_modificar_doctor,
    ventana_eliminar_doctor
)

class DoctorController:
    def __init__(self):
        pass

    def mostrar_menu_doctores(self):
        abrir_menu_doctores(self)

    def registrar_doctor(self, datos, win):
        try:
            if not datos["nombre"]:
                messagebox.showwarning("Validación", "El nombre es obligatorio")
                return

            doctor_dao.registrar_doctor(datos)
            messagebox.showinfo("Éxito", "Doctor registrado correctamente")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar: {e}")

    def mostrar_doctor_por_id(self, id_val):
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
        try:
            return doctor_dao.mostrar_todos_los_doctores()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return None

    def modificar_doctor(self, datos, win):
        try:
            doctor_dao.modificar_doctor(datos)
            messagebox.showinfo("Éxito", "Doctor modificado correctamente")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar_doctor(self, id_val, win):
        if not id_val.isdigit():
            messagebox.showwarning("Validación", "ID inválido")
            return

        if not messagebox.askyesno("Confirmar", f"¿Eliminar doctor con ID {id_val}?"):
            return

        try:
            cambios = doctor_dao.eliminar_doctor(id_val)
            if cambios == 0:
                messagebox.showinfo("Resultado", "No se encontró el doctor")
            else:
                messagebox.showinfo("Éxito", "Doctor eliminado correctamente")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
