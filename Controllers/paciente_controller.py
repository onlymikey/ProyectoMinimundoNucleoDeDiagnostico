# Este módulo contiene el controlador para la lógica de negocio de la gestión de pacientes.
# Actúa como intermediario entre las vistas de paciente y el DAO de paciente.

from tkinter import messagebox
from decimal import Decimal
import DAOS.paciente_dao as paciente_dao
from Views.paciente_view import (
    abrir_gestion_pacientes, 
    # Las siguientes vistas son invocadas por este controlador.
    # ventana_registrar_paciente, 
    # ventana_mostrar_paciente_por_id, 
    # ventana_mostrar_todos_pacientes, 
    # ventana_modificar_paciente, 
    # ventana_eliminar_paciente
)

class PacienteController:
    """
    Clase controladora para manejar la lógica de las operaciones CRUD de pacientes.
    """
    def __init__(self):
        """Inicializa el controlador de pacientes."""
        pass

    def mostrar_gestion_pacientes(self):
        """Abre el menú principal de gestión de pacientes."""
        abrir_gestion_pacientes(self)

    def registrar_paciente(self, datos, win):
        """
        Valida los datos de un nuevo paciente y lo pasa al DAO para su registro.

        Args:
            datos (dict): Diccionario con los datos del paciente.
            win (tk.Toplevel): La ventana de registro para cerrarla al finalizar.
        """
        try:
            # Validaciones de los datos de entrada.
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

            # Actualiza el diccionario de datos con los valores convertidos y validados.
            datos["edad"] = edad_val
            datos["estatura"] = estatura_val

            paciente_dao.registrar_paciente(datos)
            messagebox.showinfo("Éxito", "Paciente registrado correctamente")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar: {e}")

    def mostrar_paciente_por_id(self, id_val):
        """
        Solicita al DAO los datos de un paciente por su ID.

        Args:
            id_val (str): El ID del paciente a buscar.

        Returns:
            tuple or None: Tupla con los datos del paciente o None si no se encuentra.
        """
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
        """
        Solicita al DAO la lista completa de pacientes.

        Returns:
            list or None: Lista de tuplas con los pacientes, o None en caso de error.
        """
        try:
            return paciente_dao.mostrar_todos_los_pacientes()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return None

    def modificar_paciente(self, datos, win):
        """
        Valida los datos de un paciente y los pasa al DAO para modificar el registro.

        Args:
            datos (dict): Diccionario con los datos actualizados del paciente.
            win (tk.Toplevel): Ventana de modificación para cerrarla al finalizar.
        """
        try:
            # Validaciones de tipo para edad y estatura.
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
        """
        Pasa la solicitud de eliminación de un paciente al DAO, previa confirmación.

        Args:
            id_val (str): ID del paciente a eliminar.
            win (tk.Toplevel): Ventana de eliminación.
        """
        if not id_val.isdigit():
            messagebox.showwarning("Validación", "ID inválido")
            return

        # Solicita confirmación del usuario.
        if not messagebox.askyesno("Confirmar", f"¿Eliminar paciente con ID {id_val}?"):
            return

        try:
            # Llama al DAO y comprueba si se realizó la eliminación.
            cambios = paciente_dao.eliminar_paciente(id_val)
            if cambios == 0:
                messagebox.showinfo("Resultado", "No se encontró el paciente")
            else:
                messagebox.showinfo("Éxito", "Paciente eliminado correctamente")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
