#modulo de flask
from flask import Flask,redirect,render_template,request,session,url_for
import csv
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register",methods =["POST"])
def register():
    if request.form["name"]=="" or request.form["dorm"]==""  or request.form["captain"] == "":
        return render_template("failure.html")

    file = open("registrants.csv","a")
    writer = csv.writer(file)
    writer.writerow((request.form["name"], request.form["dorm"], request.form["captain"]))
    file.close()

    return render_template("success.html")
