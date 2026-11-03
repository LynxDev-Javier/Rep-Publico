import sqlite3

# Variable con nombre y contenido sospechoso
DB_PASSWORD = "SuperSecretPassword123!"

def autenticar_usuario(usuario):
    # CodeQL rastreará este flujo: la variable de credencial 
    # se utiliza directamente en una operación de base de datos o conexión.
    conexion = sqlite3.connect("mi_sistema.db")
    cursor = conexion.cursor()
    
    # Al pasar la contraseña hardcodeada a la consulta, CodeQL detectará la vulnerabilidad
    query = f"SELECT * FROM usuarios WHERE user = '{usuario}' AND pass = '{DB_PASSWORD}'"
    cursor.execute(query)
