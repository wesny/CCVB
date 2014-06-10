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

def getUserTwitter (username):
    myUser= Twitter.find_one({"username": username})
    dateSaved = myUser["date"]
    dif =  myTime - dateSaved
    difDays = dif.days
    if difDays > 7:
        Twitter.remove({"username":username})
        return -1
    else:
        return myUser["data"]

def addUserInstagram (username,data):
    Instagram.insert({"username": username, "data":data,"date":myTime})

def getUserInstagram (username):
    myUser= Instagram.find_one({"username": username})
    dateSaved = myUser["date"]
    dif =  myTime - dateSaved
    difDays = dif.days
    if difDays > 7:
        Instagram.remove({"username":username})
        return -1
    else:
        return myUser["data"]


if __name__ == '__main__':
    addUserTwitter ('cahnda',[1,2,3,4])
    print getUserTwitter('cahnda')
