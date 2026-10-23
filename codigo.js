const express = require("express");
const mysql = require("mysql");

const app = express();
const db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "tienda",
});

// VULNERABLE: el dato del usuario se concatena directo en la consulta
app.get("/usuario", (req, res) => {
  const nombre = req.query.nombre;
  const sql = "SELECT * FROM usuarios WHERE nombre = '" + nombre + "'";
  db.query(sql, (err, results) => {
    if (err) return res.status(500).send("Error");
    res.json(results);
  });
});

// VULNERABLE: XSS, el dato del usuario se refleja sin escapar
app.get("/saludo", (req, res) => {
  res.send("<h1>Hola " + req.query.nombre + "</h1>");
});

app.listen(3000);
