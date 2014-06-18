#

from flask import Flask, session, render_template, request, redirect, url_for
from py import *
from py import Twitter
from py import Instagram
from py import fbcalls
from py import fbclasses
from py import create_fb_jsons
import json
import os

app = Flask(__name__)
app.config.from_object('py.config')

env = app.jinja_env
env.line_statement_prefix = '='

@app.route("/peopleresults")
def peopleresults(IGUser, FBUser, TWUser):
    data = {}
    #API Calls
    #Instagram API
    if IGUser:
        pics = Instagram.get_User_Data (user)
        session["pics"] = pics
        data["instagram"] = pics
    if TWUser:
        session["TwitterUser"] = user
        tweets = Twitter.get_User_Timeline (user)
        session["tweets"] = tweets
        tweetsUpdate = Twitter.cruchData (tweets)
        data["twitter"] = tweetsUpdate
    return render_template("peopleresults.html", data = data)

@app.route("/thingresults")
def thingresults():
    return render_template("thingresults.html")

@app.route ("/Twitter/<user>")
def TwitterPage(user):
    tweets = Twitter.get_User_Timeline (user)
    # tweets = Twitter.get_User_Timeline ('nikhilgoya_l')
    data = Twitter.cruchData (tweets)
    favorite_vals = data["favorite_vals"]
    text_vals = data ["tweet_text"]
    #favorite_vals = [1,2,3]
    #text_vals =  ['a','b','c']
    #print favorite_vals[1]

    return render_template ("Post_Popularity.html",favoriteVals=favorite_vals, textVals=text_vals)

@app.route ("/Instagram")
def InstagramPage ():
    pics = Instagram.get_User_Data ("jennamarbles")
    mediaStats = pics["media_stats"]
    commentVals = mediaStats ["comments_vals"]
    likesVals =  mediaStats ["likes_vals"]
    textVals =  mediaStats ["text_vals"]
    return render_template ("Instagram_Results.html",textVals=textVals, likesVals=likesVals,commentVals=commentVals)


@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == "GET": 
        return render_template("index.html")
    if request.method == "POST" and request.form['id'] == "things":
        word = request.form['word'].encode ('ascii',"ignore")
        os.system("python analyze.py " + word + " 10")
        with open ("Output.txt", "r") as myfile:
            data=myfile.readlines()
            print data
        
        return render_template ("thingresults.html", data=data, word=word)
    if request.method == "POST" and request.form['id'] == "people":
        peopleresults(request.form['instagram'], request.form['fb'], request.form['twitter'])

@app.route('/graphtest/<user>')
def graphtest(user):
    c = fbcalls.pull_fb_data(user)
    j = create_fb_jsons.createjson_fbpost_likessvstime(c)
    return render_template('graphs.html', d=j)

if __name__ == '__main__':
    app.debug = True;
    app.run()
