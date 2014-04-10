import json
from application_only_auth import Client
import functions

consumer_key = 'jkITE2vTsnbZbO4isffog'
consumer_secret = 'VAUmkrC3Tjj1OgVMLrtkSoNtvD7k4SZ6PhG0elBWHUw'

client = Client(consumer_key, consumer_secret)

# Pretty print of tweet payload
def tweet_payload ():
    tweet = client.request('https://api.twitter.com/1.1/statuses/show.json?id=316683059296624640')
    #print json.dumps(tweet, sort_keys=True, indent=4, separators=(',', ':'))

# Show rate limit status for this application
def rate_limit():
    status = client.rate_limit_status()
    #print status['resources']['search']

# Find a user and get info on him/her. UNNECESSARY DUE TO get_User_Timline
#def findUser (username):
    # url = 'https://api.twitter.com/1/users/show.json?screen_name=%s&include_entities=true' % (username)
    # url = 'https://api.twitter.com/1.1/users/lookup.json?screen_name=%s' % (username)
    # user = client.request(url)
    # print json.dumps(user, sort_keys=True, indent=4, separators=(',', ':'))
  

def get_User_Timeline (username):
    counter = 0
    tweets = []
    #get the users timeline to evaluate their tweet content
    url =  'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=%s&count=200' % (username)
    user_timeline = client.request(url)
    for tweet in  user_timeline:
        tweets.append ({
            "favorite_count":tweet['favorite_count'],
            "retweet_count": tweet['retweet_count'],
            "text" : tweet ['text'],
            "listed_count" : tweet['user']['listed_count'],
            "friends_count" : tweet['user']['friends_count'],
            "followers_count" : tweet['user']['followers_count'],
            "profilePicture" : tweet['user']['profile_image_url'],
            "location" : tweet['user']['location'],
            "description" : tweet['user']['description'],
            "statuses_count" : tweet['user']['statuses_count'],
            "name" : tweet['user']['name']    
        })

    return tweets

def cruchData (tweetArray):
    # Define my variables
    finalData = tweetArray[0]
    favorite_count = 0
    retweet_count = 0
    favorite_vals = []
    retweet_vals = []
    tweet_count = len (tweetArray)

    #Calculate Average Values
    for tweet in tweetArray:
        retweet_count = retweet_count + tweet["retweet_count"]
        retweet_vals.append (tweet["retweet_count"])
        favorite_count = favorite_count + tweet["favorite_count"]
        favorite_vals.append (tweet["favorite_count"])
    avg_retweet_count = retweet_count /  tweet_count
    avg_fav_count = favorite_count /  tweet_count
    
    #Update finalData array
    finalData["favorite_count"] =  avg_fav_count
    finalData["retweet_count"] =  avg_retweet_count
   
    popTweets = []
    #Find awesome tweets
    for tweet in tweetArray:
        retweets = tweet["retweet_count"]
        favs = tweet["favorite_count"]
        var pop = functions.isPopular (favs,favorite_vals)
        var pop2 = functions.isPopular (retweets, retweet_vals)
        if pop = true: 
           popTweets.append (tweet["text"])

    finalData["popularTweets"] = popTweets
    return finalData

if __name__ == '__main__':
     tweets = get_User_Timeline ('nikhilgoya_l')
     data = cruchData (tweets)
     print json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'))


#NOTES/LONG TERM GOALS 
    #A. MONGODB Storage for API Calls
    #This code needs to be modified to cache user data and store it in a mongoDB. Then update with API calls every 15 minutes to avoid too many calls at once. 
    #Then, when user call a search, we search the mongoDB. If the data has been updated in the past week, we use it. Otherwise, we make a distint call.
    
    #B. Don't count retweets!
