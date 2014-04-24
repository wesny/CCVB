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


def get_User_ID (username):
    #find user_id
    #user =  api.user_search(username, 1)[0]    
    url = ("https://api.instagram.com/v1/users/search?q=%s&access_token=1267672900.1fb234f.ab78269e1b754039b0e900a966e14fdb") %(username)
    response = urlopen(url)
    json_raw = response.read()
    json_data = json.loads(json_raw)
    user_id = json_data["data"][0]["id"]

def get_User_Data (username):
    user_id = get_User_ID (username)
    #find user
    #doing it myself because the library is aweful...
    url = ("https://api.instagram.com/v1/users/%s/?access_token=1267672900.1fb234f.ab78269e1b754039b0e900a966e14fdb") %(user_id)
    response = urlopen(url)
    json_raw = response.read()
    json_data = json.loads(json_raw)
    full_name = json_data["data"]["full_name"]
    counts = json_data["data"]["counts"]
    total_media = counts ["media"]
    followed_by  = counts ["followed_by"]

    data = {}
    data ["full_name"] = full_name
    data ["total_media"] = total_media
    data ["followed_by"] = followed_by
    try:
        media = get_media (user_id)
    except: 
        media = []
    data ["media"] = media
    return data

def get_media (user_id):
    url = ("https://api.instagram.com/v1/users/%s/media/recent/?access_token=%s") % (user_id,access_token)
    response = urlopen(url)
    json_raw = response.read()
    json_data = json.loads(json_raw)["data"][0]
    for x in json_data:
       # print x
        for x in json_data["user"]:
            print x
        for x in json_data["likes"]:
            print x
        for x in json_data["comments"][0]:
            print x

if __name__ == '__main__':
  #  data = get_User_Timeline ('jennamarbles')
    media = get_media(6717525)

