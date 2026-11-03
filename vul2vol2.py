import os
import subprocess

# Leer el secreto desde una variable de entorno
DB_PASSWORD = os.environ.get("DB_PASSWORD")

def ejecutar_comando():
    archivo = input("Introduce el nombre del archivo a buscar: ")
    # Lista de argumentos y sin shell=True
    subprocess.run(["ls", "-la", "--", archivo], check=False)

if __name__ == "__main__":
    ejecutar_comando()
