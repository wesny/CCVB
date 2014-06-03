import pymongo

connection = pymongo.MongoClient ("ds029658.mongolab.com", 29658)
db = connection ["heroku_app25983966"]
db.authenticate("softdev", "softdev")
Twitter = db.Twitter
Instagram = db.Instagram

def addUserTwitter (username,data):
    Twitter.insert({"username": username, "data":data})

def getUserTwitter (username):
    myUser= Twitter.find_one({"username": username})
    return myUser["data"]


if __name__ == '__main__':
    addUserTwitter ('cahnda',[1,2,3,4])
    print getUserTwitter('cahnda')

