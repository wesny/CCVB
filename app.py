from flask import Flask, session, render_template, request, redirect, url_for
from py import *
from py import Twitter
import os
#from alchemy import analyze

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

@app.route ("/DCtesting")
def DCtesting():
    tweets = Twitter.get_User_Timeline ('nikhilgoya_l')
    data = Twitter.cruchData (tweets)
    favorite_vals = data["favorite_vals"]
    print favorite_vals
    return render_template ("Post_Popularity.html",favorite_vals=favorite_vals)

@app.route("/tester", methods = ['GET', 'POST'])
def tester():
    if request.method == "GET": 
        return render_template("tester.html")
    if request.method == "POST": 
        word = request.form['word'].encode ('ascii',"ignore")
        os.system("python analyze.py reagan 10")
        with open ("Output.txt", "r") as myfile:
            data=myfile.readlines()
            print data
        
        return render_template ("popularity_results.html", data=data, word=word)


if __name__ == '__main__':
    app.debug = True;
    app.run()
