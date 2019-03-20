#modulo de flask
from flask import Flask
#modulo de date time
from datetime import datetime
#modulo pi time zone
from pytz import timezone

app=Flask(__name__)

@app.route("/")
def time():
    now=datetime.now(timezone('America/New_York'))
    return "The current time in Cambridge is:  {}".format(now)

@app.route("/show/<number>")
def show(number):
    return "You pased in {}".format(number)