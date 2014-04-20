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
    #find user_id
    #user =  api.user_search(username, 1)[0]    
    url = ("https://api.instagram.com/v1/users/search?q=%s&access_token=1267672900.1fb234f.ab78269e1b754039b0e900a966e14fdb") %(username)
    response = urlopen(url)
    json_raw = response.read()
    json_data = json.loads(json_raw)
    user_id = json_data["data"][0]["id"]

    #find user

    url = ("https://api.instagram.com/v1/users/%s") %(user_id)
    response = urlopen(url)
    json_raw = response.read()
    json_data = json.loads(json_raw)
    print json_data

if __name__ == '__main__':
     user = get_User_Timeline ('DavidCahn')
