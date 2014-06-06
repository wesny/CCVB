import pymongo
from datetime import datetime
myTime = datetime.now()

connection = pymongo.MongoClient ("ds029658.mongolab.com", 29658)
db = connection ["heroku_app25983966"]
db.authenticate("softdev", "softdev")
Twitter = db.Twitter
Instagram = db.Instagram

def addUserTwitter (username,data):
    Twitter.insert({"username": username, "data":data, "date":myTime})

def checkDateTwitter (username):
    myUser= Twitter.find_one({"username": username})
    dateSaved = myUser["date"]
    print myTime - dateSaved

def getUserTwitter (username):
    myUser= Twitter.find_one({"username": username})
    return myUser["data"]

def addUserInstagram (username,data):
    Instagram.insert({"username": username, "data":data,"date":myTime})

def checkDateInstagram (username):
    myUser= Instagram.find_one({"username": username})
    dateSaved = myUser["date"]
    print myTime - dateSaved

def getUserInstagram (username):
    myUser= Instagram.find_one({"username": username})
    return myUser["data"]

if __name__ == '__main__':
    addUserTwitter ('cahnda',[1,2,3,4])
    print getUserTwitter('cahnda')
    checkDateTwitter('cahnda')

