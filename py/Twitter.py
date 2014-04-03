import tweepy

Consumer_Key = 'jkITE2vTsnbZbO4isffog'
Consumer_Secret = 'VAUmkrC3Tjj1OgVMLrtkSoNtvD7k4SZ6PhG0elBWHUw'
Access_Token = '1531685562-9OgrUddG7L5bP9zUJETYf4sfABGC5U1cI2rxXeo'
Access_Token_Secret = '5v43cr0rax5fLhYKF67lAHlobNVjQqVncCm4GgtEFyl8o'
usrname = 'twitter'

public_tweets = tweepy.API.get_user(usrname)
for tweet in public_tweets:
    print tweet.text
