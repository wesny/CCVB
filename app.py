from flask import Flask, session, render_template, request, redirect, url_for
from py import *
from py import Twitter
from py import utils
from py import Instagram
import json
import os

#from alchemy import analyze

app = Flask(__name__)
app.config.from_object('py.config')

env = app.jinja_env
env.line_statement_prefix = '='

#@app.route("/")
#def index():
#    return render_template("index.html")

@app.route("/peopleresults")
def peopleresults():
    return render_template("peopleresults.html")

@app.route("/thingresults")
def thingresults():
    return render_template("thingresults.html")

@app.route ("/Twitter1/<user>")
def TwitterFavorite(user):
    try:
       tweets = utils.getUserTwitter(user)
       if tweets == -1:
           tweets = Twitter.get_User_Timeline (user)
           utils.addUserTwitter (user,tweets)
    except:
        tweets = Twitter.get_User_Timeline (user)
        utils.addUserTwitter (user,tweets)
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
    try:
        tweets = utils.getUserTwitter(user)
        if tweets == -1:
            tweets = Twitter.get_User_Timeline (user)
            utils.addUserTwitter (user,tweets)
    except:
        tweets = Twitter.get_User_Timeline (user)
        utils.addUserTwitter (user,tweets)
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
    try:
        tweets = utils.getUserTwitter(user)
        if tweets == -1:
            tweets = Twitter.get_User_Timeline (user)
            utils.addUserTwitter (user,tweets)
    except:
        tweets = Twitter.get_User_Timeline (user)
        utils.addUserTwitter (user,tweets)    
    data = Twitter.cruchData (tweets)
    vals = data["eng_vals"]
    print vals
    return render_template ("/Graphs/TwitterEngTime.html",vals=vals)

@app.route ("/Twitter4/<user>")
def TwitterRetFav(user):
    try:
        tweets = utils.getUserTwitter(user)
        if tweets == -1:
            tweets = Twitter.get_User_Timeline (user)
            utils.addUserTwitter (user,tweets)
    except:
        tweets = Twitter.get_User_Timeline (user)
        utils.addUserTwitter (user,tweets)   
    data = Twitter.cruchData (tweets)
    favorites = data["favorite_vals"]
    retweets = data["retweet_vals"]
    text_vals = data ["tweet_text"]
    return render_template ("/Graphs/TwitterRetFav.html",favorites=favorites,retweets=retweets,text_vals=text_vals)

@app.route ("/TwitterProfile/<user>")
def TwitterProfile(user):
    try:
        tweets = utils.getUserTwitter(user)
        if tweets == -1:
            tweets = Twitter.get_User_Timeline (user)
            utils.addUserTwitter (user,tweets)
    except:
        tweets = Twitter.get_User_Timeline (user)
        utils.addUserTwitter (user,tweets)   
    data = Twitter.cruchData (tweets)
    return render_template ("/Graphs/TwitterReport.html",data=data)

@app.route ("/InstagramProfile/<user>")
def InstagramProfile(user):
    try:
        pics = utils.getUserInstagram(user)
        if pics == -1:
            pics = Instagram.get_User_Data (user)
            utils.addUserInstagram(user,pics)
    except:
        pics = Instagram.get_User_Data (user)
        utils.addUserInstagram(user,pics)
    return render_template ("/Graphs/InstagramReport.html",data=pics)


@app.route ("/Instagram1/<user>")
def InstagramCluster (user):
    try:
        pics = utils.getUserInstagram(user)
        if pics == -1:
            pics = Instagram.get_User_Data (user)
            utils.addUserInstagram(user,pics)
    except:
        pics = Instagram.get_User_Data (user)
        utils.addUserInstagram(user,pics)
    mediaStats = pics["media_stats"]
    commentVals = mediaStats ["comments_vals"]
    likesVals =  mediaStats ["likes_vals"]
    textVals =  mediaStats ["text_vals"]
    return render_template ("/Graphs/InstagramLikesFavorites.html",textVals=textVals, likesVals=likesVals,commentVals=commentVals)


@app.route ("/Instagram2/<user>")
def InstagramEngagements(user):
    try:
        pics = utils.getUserInstagram(user)
        if pics == -1:
            pics = Instagram.get_User_Data (user)
            utils.addUserInstagram(user,pics)
    except:
        pics = Instagram.get_User_Data (user)
        utils.addUserInstagram(user,pics)
    
    vals = pics["media_stats"]["eng_vals"]
    return render_template ("/Graphs/InstagramEngTime.html",vals=vals)

@app.route ("/Instagram3/<user>")
def InstagamLikesTime(user):
    try:
        pics = utils.getUserInstagram(user)
        if pics == -1:
            pics = Instagram.get_User_Data (user)
            utils.addUserInstagram(user,pics)
    except:
        pics = Instagram.get_User_Data (user)
        utils.addUserInstagram(user,pics)

    likes_val= pics["media_stats"]["likes_vals"]
    img_vals = pics["media_stats"]["images"]
    text_vals = pics["media_stats"]["text_vals"]
    return render_template ("/Graphs/InstagramLikesTime.html", likes_val= likes_val,img_vals=img_vals,text_vals=text_vals)

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == "GET": 
        return render_template("index.html")
    if request.method == "POST" and request.form['id'] == "things":
        word = request.form['word'].encode ('ascii',"ignore")
        os.system("python analyze.py " + word + " 150")
        with open ("Output.txt", "r") as myfile:
            data=myfile.readlines()
            print data
        
        return render_template ("thingresults.html", data=data, word=word)
    if request.method == "POST" and request.form['id'] == "people":
        return render_template ("peopleresults.html")


if __name__ == '__main__':
    app.debug = True;
    app.run()
