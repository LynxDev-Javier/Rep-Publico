from flask import Flask, request
import subprocess

app = Flask(__name__)


@app.route("/buscar")
def buscar():
    archivo = request.args.get("archivo")
    # Lista de argumentos y sin shell=True
    subprocess.run(["ls", "-la", "--", archivo], check=False)
    return "listo"
