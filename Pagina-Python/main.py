from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """ 
    <h1> Hello, world </h1>
<a href="/saludo">¡Ver un Saludo!</a>
"""

@app.route("/saludo")
def saludo():
    return "<hi>Hola, bienvenido a mi página en Python</hi>"

@app.route("/saludo/<nombre>")
def saludo1(nombre):
    return f"<hi>Hola {nombre} bienvenido a mi página</hi>"

@app.route("/suma/<int:numero1>/<int:numero2>")
def suma(numero1:int, numero2:int):
    return f"<hi>La suma es: {numero1 + numero2}</hi>"

@app.route("/moneda")
def moneda():
    moneda = random.randint(1, 2)
    if moneda == 1:
        return "<hi> Escudo </hi>" 
    if moneda == 2:
        return "<hi> Cruz </hi>"

app.run(debug=True)