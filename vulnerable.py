
import os
import subprocess

# CORRECCIÓN 1: Se eliminó el secreto hardcodeado del código. 
# En su lugar, las credenciales sensibles deben cargarse mediante variables de entorno.
# Ejemplo de uso seguro: os.environ.get("DB_PASSWORD")
DB_PASSWORD = os.getenv("SuperSecretPassword123!")

def ejecutar_comando():
    archivo = input("Introduce el nombre del archivo a buscar: ")
    
    # CORRECCIÓN 2: Se evita shell=True y se pasa el comando como una lista de argumentos.
    # Esto previene por completo la inyección de comandos, ya que el sistema operativo 
    # interpreta la entrada del usuario estrictamente como un argumento y no como parte de una shell.
    try:
        # Usamos subprocess.run con una lista y shell=False por defecto
        resultado = subprocess.run(["ls", "-la", archivo], capture_output=True, text=True, check=True)
        print(resultado.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")

if __name__ == "__main__":
    ejecutar_comando()
