import json
from application_only_auth import Client

consumer_key = 'jkITE2vTsnbZbO4isffog'
consumer_secret = 'VAUmkrC3Tjj1OgVMLrtkSoNtvD7k4SZ6PhG0elBWHUw'

client = Client(consumer_key, consumer_secret)

# Pretty print of tweet payload
tweet = client.request('https://api.twitter.com/1.1/statuses/show.json?id=316683059296624640')
print json.dumps(tweet, sort_keys=True, indent=4, separators=(',', ':'))

# Show rate limit status for this application
status = client.rate_limit_status()
print status['resources']['search']
