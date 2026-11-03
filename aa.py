import hashlib
import logging
import pickle
import sqlite3
import subprocess
import traceback

import requests
import yaml
from flask import Flask, redirect, request

app = Flask(__name__)


# 1. Inyección SQL (py/sql-injection)
@app.route("/usuario")
def buscar_usuario():
    nombre = request.args.get("nombre")
    conn = sqlite3.connect("tienda.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM usuarios WHERE nombre = '{nombre}'")
    return str(cursor.fetchall())


# 2. Inyección de comandos (py/command-line-injection)
@app.route("/ping")
def ping():
    host = request.args.get("host")
    subprocess.call("ping -c 1 " + host, shell=True)
    return "listo"


# 3. Path traversal (py/path-injection)
@app.route("/leer")
def leer():
    archivo = request.args.get("archivo")
    with open("/var/datos/" + archivo) as f:
        return f.read()


# 4. XSS reflejado (py/reflective-xss)
@app.route("/saludo")
def saludo():
    nombre = request.args.get("nombre")
    return "<h1>Hola " + nombre + "</h1>"


# 5. Ejecución de código (py/code-injection)
@app.route("/calcular")
def calcular():
    expresion = request.args.get("expr")
    return str(eval(expresion))


# 6. Deserialización insegura (py/unsafe-deserialization)
@app.route("/cargar", methods=["POST"])
def cargar():
    objeto = pickle.loads(request.data)
    return str(objeto)


@app.route("/config", methods=["POST"])
def config():
    datos = yaml.load(request.data)  # sin SafeLoader
    return str(datos)


# 7. SSRF (py/full-ssrf)
@app.route("/fetch")
def fetch():
    url = request.args.get("url")
    return requests.get(url).text


# 8. Redirección abierta (py/url-redirection)
@app.route("/ir")
def ir():
    destino = request.args.get("next")
    return redirect(destino)


# 9. Hash débil para contraseñas (py/weak-sensitive-data-hashing)
@app.route("/registro", methods=["POST"])
def registro():
    password = request.form["password"]
    hash_pw = hashlib.md5(password.encode()).hexdigest()
    # 10. Contraseña en logs (py/clear-text-logging-sensitive-data)
    logging.info("Nuevo usuario con password: " + password)
    return hash_pw


# 11. Exposición del stack trace (py/stack-trace-exposure)
@app.route("/error")
def error():
    try:
        1 / 0
    except Exception:
        return traceback.format_exc()


if __name__ == "__main__":
    # 12. Debug activado (py/flask-debug)
    app.run(debug=True, host="0.0.0.0")
