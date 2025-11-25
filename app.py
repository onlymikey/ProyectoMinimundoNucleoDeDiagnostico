# Este es el punto de entrada principal de la aplicación del sistema de diagnóstico.
# Su única responsabilidad es iniciar la interfaz de usuario y la lógica de la aplicación.

# Importa la función para crear la ventana de login desde el módulo de vistas.
from Views.main_view import crear_ventana_login
# Importa la función de validación de login desde el módulo de controladores.
from Controllers.main_controller import validar_login

# El bloque __name__ == "__main__" asegura que el código dentro de él solo se ejecute
# cuando el script es ejecutado directamente.
if __name__ == "__main__":
    # Llama a la función 'crear_ventana_login' para construir y mostrar la ventana de inicio de sesión.
    # Le pasa 'validar_login' como argumento, que es la función que se llamará cuando el usuario
    # intente iniciar sesión. Esta es una forma de inyección de dependencias, donde la vista
    # recibe la lógica del controlador que necesita ejecutar.
    crear_ventana_login(validar_login)
