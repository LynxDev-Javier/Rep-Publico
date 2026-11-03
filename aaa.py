import pymysql

# CodeQL rastreará esta asignación si fluye hacia una función de autenticación/conexión
DB_PASSWORD = "SuperSecretPassword123!"

def conectar_base_datos():
    # Al pasar la variable directamente a una función de conexión reconocida, 
    # CodeQL detectará el flujo de datos del secreto hardcodeado.
    conexion = pymysql.connect(
        host="localhost",
        user="root",
        password=DB_PASSWORD,  # <--- Aquí es donde CodeQL detecta el "sink" de credencial
        database="test_db"
    )
    return conexion
