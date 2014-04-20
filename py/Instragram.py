import requests
import json
from urllib2 import urlopen
from instagram.client import InstagramAPI

#AccountCreated
#https://github.com/Instagram/python-instagram
#pip install python-instagram SUCCESSFUL

CLIENT_ID = 'fc3ea612a2124506b409ac77b5b3c068'
CLIENT_SECRET = '95ff2f2aedd248498b1a79535c05107d'
access_token='1267672900.1fb234f.ab78269e1b754039b0e900a966e14fdb'
count = 1
#api = InstagramAPI(client_id="CLIENT_ID", client_secret='CLIENT_SECRET')
api = InstagramAPI(access_token=access_token)

def get_User_Timeline (username):
    user =  api.user_search(username, 1)[0]
        
#    api.user(user_id) = userID
    

    #url = ("https://api.instagram.com/v1/users/search?q=%s&count=1&access_token=%s") % (username,access_token)
    #response = urlopen(url)
   # print json.dumps(response, sort_keys=True, indent=4, separators=(',', ':'))
   

if __name__ == '__main__':
     user = get_User_Timeline ('sophieheinberg')
