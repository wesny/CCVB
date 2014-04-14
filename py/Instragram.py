import requests
import json
from urllib2 import urlopen
#AccountCreated
#https://github.com/Instagram/python-instagram
#pip install python-instagram SUCCESSFUL

CLIENT_ID = 'fc3ea612a2124506b409ac77b5b3c068'
CLIENT_SECRET = '95ff2f2aedd248498b1a79535c05107d'
access_token='1267672900.1fb234f.ab78269e1b754039b0e900a966e14fdb'
count = 1
api = InstagramAPI(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET')


def get_User_Timeline (username):
    #url = ("https://api.instagram.com/v1/users/search?q=%s&count=1&access_token=%s") % (username,access_token)
    #response = urlopen(url)
   # print json.dumps(response, sort_keys=True, indent=4, separators=(',', ':'))
