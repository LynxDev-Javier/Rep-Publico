import os
import subprocess
import sqlite3

# VULNERABILIDAD: CodeQL detectará esta credencial porque fluye hacia la función de conexión/consulta
DB_PASSWORD = "SuperSecretPassword123!"

def autenticar_en_bd():
    # Simulamos un sumidero reconocido por CodeQL para rastrear el secreto hardcodeado
    conexion = sqlite3.connect("sistema.db")
    cursor = conexion.cursor()
    
    # Al concatenar o usar el password directamente en una consulta, CodeQL genera la alerta de credencial expuesta
    cursor.execute(f"SELECT * FROM admin WHERE token = '{DB_PASSWORD}'")

def ejecutar_comando():
    archivo = input("Introduce el nombre del archivo a buscar: ")
    
    # Mantenemos la estructura segura de subprocess con lista para evitar la inyección de comandos
    try:
        resultado = subprocess.run(["ls", "-la", archivo], capture_output=True, text=True, check=True)
        print(resultado.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")

if __name__ == "__main__":
    autenticar_en_bd()
    ejecutar_comando()
