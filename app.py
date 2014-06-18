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
    return render_template("thingresults2.html")

@app.route ("/Twitter1/<user>")
def TwitterFavorite(user):
    if (session["TwitterUser"] == user):
        tweets = session["tweets"]
    else:
        session["TwitterUser"] = user
        tweets = Twitter.get_User_Timeline (user)
        session["tweets"] = tweets

    data = Twitter.cruchData (tweets)
    favorite_vals = data["favorite_vals"]
    text_vals = data ["tweet_text"]
    retweet_vals = data["retweet_vals"]
    #favorite_vals = [1,2,3]
    #text_vals =  ['a','b','c']
    #print favorite_vals[1]

    return render_template ("/Graphs/TweetsFavoritesTime.html",favoriteVals=favorite_vals, textVals=text_vals)

@app.route ("/Twitter2/<user>")
def TwitterRetweet(user):
    if (session["TwitterUser"] == user):
        tweets = session["tweets"]
    else:
        session["TwitterUser"] = user
        tweets = Twitter.get_User_Timeline (user)
        session["tweets"] = tweets
    data = Twitter.cruchData (tweets)
    favorite_vals = data["favorite_vals"]
    text_vals = data ["tweet_text"]
    retweet_vals = data["retweet_vals"]
    #favorite_vals = [1,2,3]
    #text_vals =  ['a','b','c']
    #print favorite_vals[1]

    return render_template ("/Graphs/TweetsRetweetsTime.html",retweetVals=retweet_vals, textVals=text_vals)

@app.route ("/Twitter3/<user>")
def TwitterEngagements(user):
    if (session["TwitterUser"] == user):
        tweets = session["tweets"]
    else:
        session["TwitterUser"] = user
        tweets = Twitter.get_User_Timeline (user)
        session["tweets"] = tweets
    data = Twitter.cruchData (tweets)
    vals = data["eng_vals"]
    print vals
    return render_template ("/Graphs/TwitterEngTime.html",vals=vals)

@app.route ("/Twitter4/<user>")
def TwitterRetFav(user):
    if (session["TwitterUser"] == user):
        tweets = session["tweets"]
    else:
        session["TwitterUser"] = user
        tweets = Twitter.get_User_Timeline (user)
        session["tweets"] = tweets 
    data = Twitter.cruchData (tweets)
    favorites = data["favorite_vals"]
    retweets = data["retweet_vals"]
    text_vals = data ["tweet_text"]
    return render_template ("/Graphs/TwitterRetFav.html",favorites=favorites,retweets=retweets,text_vals=text_vals)

@app.route ("/TwitterProfile/<user>")
def TwitterProfile(user):
    if (session["TwitterUser"] == user):
        tweets = session["tweets"]
    else:
        session["TwitterUser"] = user
        tweets = Twitter.get_User_Timeline (user)
        session["tweets"] = tweets
    data = Twitter.cruchData (tweets)
    return render_template ("/Graphs/TwitterReport.html",data=data)

@app.route ("/InstagramProfile/<user>")
def InstagramProfile(user):
    if (session["InstagramUser"] == user):
        pics = session["pics"]
    else:
        session["InstagramUser"] = user
        pics = Instagram.get_User_Data (user)
        session["pics"] = pics
    return render_template ("/Graphs/InstagramReport.html",data=pics)


@app.route ("/Instagram1/<user>")
def InstagramCluster (user):
    if (session["InstagramUser"] == user):
        print "Session"
        pics = session["pics"]
    else:
        session["InstagramUser"] = user
        pics = Instagram.get_User_Data (user)
        session["pics"] = pics

    mediaStats = pics["media_stats"]
    commentVals = mediaStats ["comments_vals"]
    likesVals =  mediaStats ["likes_vals"]
    textVals =  mediaStats ["text_vals"]
    return render_template ("/Graphs/InstagramLikesFavorites.html",textVals=textVals, likesVals=likesVals,commentVals=commentVals)


@app.route ("/Instagram2/<user>")
def InstagramEngagements(user):
    if (session["InstagramUser"] == user):
        pics = session["pics"]
    else:
        session["InstagramUser"] = user
        pics = Instagram.get_User_Data (user)
        session["pics"] = pics
    
    vals = pics["media_stats"]["eng_vals"]
    return render_template ("/Graphs/InstagramEngTime.html",vals=vals)

@app.route ("/Instagram3/<user>")
def InstagamLikesTime(user):
    if (session["InstagramUser"] == user):
        pics = session["pics"]
    else:
        session["InstagramUser"] = user
        pics = Instagram.get_User_Data (user)
        session["pics"] = pics

    likes_val= pics["media_stats"]["likes_vals"]
    img_vals = pics["media_stats"]["images"]
    text_vals = pics["media_stats"]["text_vals"]
    return render_template ("/Graphs/InstagramLikesTime.html", likes_val= likes_val,img_vals=img_vals,text_vals=text_vals)

@app.route("/", methods = ['GET', 'POST'])
def index():
    session["TwitterUser"] = ""
    session["InstagramUser"] = ""
    if request.method == "GET": 
        return render_template("index.html")
    if request.method == "POST" and request.form['id'] == "things":
        word = request.form['word'].encode ('ascii',"ignore")
        os.system("python analyze.py " + word + " 10")
        with open ("Output.txt", "r") as myfile:
            data=myfile.readlines()
            print data
        with open ("Output2.txt", "r") as myfile:
            data2=myfile.readlines()
            print data2

        
        return render_template ("thingresults2.html", data=data, data2=data2, word=word)
    if request.method == "POST" and request.form['id'] == "people":
        #return render_template ("peopleresults2.html")
        peopleresults(request.form['instagram'], request.form['fb'], request.form['twitter'])

if __name__ == '__main__':
    app.debug = True;
    app.run()
