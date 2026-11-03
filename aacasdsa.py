
from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/buscar")
def buscar():
    archivo = request.args.get("archivo", "")

    conexion = sqlite3.connect("mi_base.db")
    cursor = conexion.cursor()

    # Vulnerabilidad intencional para pruebas SAST
    query = "SELECT * FROM archivos WHERE nombre = '" + archivo + "'"

    cursor.execute(query)

    resultado = cursor.fetchall()
    conexion.close()

    return {"resultados": resultado}

if __name__ == "__main__":
    app.run()
