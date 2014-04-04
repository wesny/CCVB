import json
from application_only_auth import Client

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

# Find a user and get info on him/her
def findUser (username):
    #url = 'https://api.twitter.com/1/users/show.json?screen_name=%s&include_entities=true' % (username)
    url = 'https://api.twitter.com/1.1/users/lookup.json?screen_name=%s' % (username)
    user = client.request(url)
    print json.dumps(user, sort_keys=True, indent=4, separators=(',', ':'))

if __name__ == '__main__':
    print findUser ('nikhilgoya_l')
