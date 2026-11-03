import os
import subprocess
import sqlite3

DB_PASSWORD = "SuperSecretPassword123!"

def ejecutar_comando():
    archivo = input("Introduce el nombre del archivo a buscar: ")
    
    # VULNERABILIDAD REAL PARA CODEQL: Inyección SQL (py/sql-injection)
    # Al concatenar directamente la entrada del usuario ('archivo') en la consulta, 
    # CodeQL rastreará el flujo de datos inseguro (taint tracking) y generará la alerta.
    conexion = sqlite3.connect("mi_base.db")
    cursor = conexion.cursor()
    query = "SELECT * FROM archivos WHERE nombre = '" + archivo + "'"
    cursor.execute(query)
    
    try:
        resultado = subprocess.run(["ls", "-la", archivo], capture_output=True, text=True, check=True)
        print(resultado.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")

if __name__ == "__main__":
    ejecutar_comando()
