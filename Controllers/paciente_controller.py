from tkinter import messagebox
from decimal import Decimal
import DAOS.paciente_dao as paciente_dao
from Views.paciente_view import (
    abrir_gestion_pacientes, 
    ventana_registrar_paciente, 
    ventana_mostrar_paciente_por_id, 
    ventana_mostrar_todos_pacientes, 
    ventana_modificar_paciente, 
    ventana_eliminar_paciente
)

class PacienteController:
    def __init__(self):
        pass

    def mostrar_gestion_pacientes(self):
        abrir_gestion_pacientes(self)

    def registrar_paciente(self, datos, win):
        try:
            if not datos["nombre"]:
                messagebox.showwarning("Validación", "El nombre es obligatorio")
                return

            try:
                edad_val = int(datos["edad"]) if datos["edad"] else None
            except ValueError:
                messagebox.showwarning("Validación", "Edad debe ser un número entero")
                return

            try:
                estatura_val = Decimal(datos["estatura"]) if datos["estatura"] else None
            except:
                messagebox.showwarning("Validación", "Estatura debe ser un número válido")
                return

            datos["edad"] = edad_val
            datos["estatura"] = estatura_val

            paciente_dao.registrar_paciente(datos)
            messagebox.showinfo("Éxito", "Paciente registrado correctamente")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar: {e}")

    def mostrar_paciente_por_id(self, id_val):
        try:
            if not id_val.isdigit():
                messagebox.showwarning("Validación", "ID inválido")
                return None
            
            paciente = paciente_dao.mostrar_paciente_por_id(id_val)

            if not paciente:
                messagebox.showinfo("Resultado", "No se encontró el paciente con ese ID")
            
            return paciente
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return None

    def mostrar_todos_los_pacientes(self):
        try:
            return paciente_dao.mostrar_todos_los_pacientes()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return None

    def modificar_paciente(self, datos, win):
        try:
            try:
                edad_val = int(datos["edad"]) if datos["edad"] != "" else None
            except ValueError:
                messagebox.showwarning("Validación", "Edad debe ser un número entero")
                return

            try:
                estatura_val = Decimal(datos["estatura"]) if datos["estatura"] != "" else None
            except:
                messagebox.showwarning("Validación", "Estatura debe ser un número válido")
                return

            datos["edad"] = edad_val
            datos["estatura"] = estatura_val

            paciente_dao.modificar_paciente(datos)
            messagebox.showinfo("Éxito", "Paciente modificado correctamente")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar_paciente(self, id_val, win):
        if not id_val.isdigit():
            messagebox.showwarning("Validación", "ID inválido")
            return

        if not messagebox.askyesno("Confirmar", f"¿Eliminar paciente con ID {id_val}?"):
            return

        try:
            cambios = paciente_dao.eliminar_paciente(id_val)
            if cambios == 0:
                messagebox.showinfo("Resultado", "No se encontró el paciente")
            else:
                messagebox.showinfo("Éxito", "Paciente eliminado correctamente")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
