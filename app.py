from flask import Flask, session, render_template, request, redirect, url_for
from py import *
from alchemy import analyze

app = Flask(__name__)
app.config.from_object('py.config')

env = app.jinja_env
env.line_statement_prefix = '='

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/peopleresults")
def peopleresults():
    return render_template("peopleresults.html")

@app.route("/thingresults")
def thingresults():
    return render_template("thingresults.html")

@app.route("/tester", methods = ['GET', 'POST'])
def tester():
    if request.method == "GET": 
        return render_template("tester.html")
    if request.method == "POST": 
        word = request.form['word'].encode ('ascii',"ignore")
        
        return render_template("tester.html")


if __name__ == '__main__':
    app.debug = True;
    app.run()
