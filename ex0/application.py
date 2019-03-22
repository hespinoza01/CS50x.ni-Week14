#Importar Framework y Utilidades
from flask import Flask,redirect, render_template, session,url_for
#Declarar que es una aplicacion web
app=Flask(__name__)
#Definir comportamiento con URL vacia
@app.route("/")
def main():
    return render_template("index.html")

@app.route("/<string:name>")
def name(name):
    return render_template("layout.html",name=name)
