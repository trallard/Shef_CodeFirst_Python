# -*- coding: utf-8 -*-
"""
@author: Tania @trallard
This script contains the necessary functions to query the Spotify API and
return json data with the relevant results for the queries.
The queries are done using requests (HTTP for humans, enables GET, POST, PUT requests)
and the Spotify endpoints. Info on the Spotify API can be found at
https://developer.spotify.com/web-api/endpoint-reference/

Note that the Spotify API has a number of steps that should be followed for explicit
authorisation from the user. All of the steps are detailed here.

"""

# importing Requests: HTTP for Humans - installed previously
import requests
import yaml
import json

# ******* All of the needed URLS and functions to use the Spotify API ****


# ----------------- SPOTIFY BASE URL ----------------

SPOTIFY_API_BASE_URL = 'https://api.spotify.com/v1'


# -----------------  USER AUTHORIZATION ----------------

# spotify endpoints
SPOTIFY_AUTH_BASE_URL = "https://accounts.spotify.com/{}"
SPOTIFY_AUTH_URL = SPOTIFY_AUTH_BASE_URL.format('authorize')
SPOTIFY_TOKEN_URL = SPOTIFY_AUTH_BASE_URL.format('api/token')

# Spotify APi base URL
SPOTIFY_API_URL = "https://api.spotify.com/v1"


# server side parameters
# feel free to change it if you want to, but make sure to change in
# your Spotify dev account as well *
CLIENT_SIDE_URL = "http://127.0.0.1"
PORT = 5000
REDIRECT_URI = "{}:{}/callback/".format(CLIENT_SIDE_URL, PORT)
# the scope will determine the level of permissions you are granting the app
SCOPE = "playlist-modify-public playlist-modify-private user-read-recently-played user-top-read"
STATE = ""
# the following forces the user to click on the login dialog
# even if previsously logged in
SHOW_DIALOG_bool = True
SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()

# https://developer.spotify.com/web-api/authorization-guide/ has all the details

# Client keys
with open("config.yml", 'r') as ymlfile:
        config = yaml.load(ymlfile)

# retrieve the keys from the config data
client_id = config['spotify']['client_id']
client_secret = config['spotify']['client_secret']

def get_auth(REDIRECT_URI = REDIRECT_URI, client_id = client_id,
             SPOTIFY_AUTH_URL = SPOTIFY_AUTH_URL):

        auth_vars = {'response_type': 'code',
                             'redirect_uri': REDIRECT_URI,
                             'client_id': client_id}

        AUTH_URL = requests.get(SPOTIFY_AUTH_URL, auth_vars)

        return AUTH_URL

def auth_spotify(client_id = client_id, redirect_uri = REDIRECT_URI):
        """This function will handle the authorisation for
        Spotify API. It will make use of the authorisation
        callback """


        auth_vars = {'response type': 'code',
                     'redirect_uri': redirect_uri,
                     'client_id': client_id}

        endpoint = "https://accounts.spotify.com/authorize"

        response = requests.get(endpoint, params = auth_vars)

        return response.url


def authorize_spotify(auth_token, client_id = client_id, client_secret = client_secret,
                      REDIRECT_URI = REDIRECT_URI, SPOTIFY_TOKEN_URL = SPOTIFY_TOKEN_URL):
        """Auth Step 4: Requests refresh and access tokens"""

        code_payload = {
                "grant_type": "authorization_code",
                "code": auth_token,
                "redirect_uri": REDIRECT_URI,
                "client_id": client_id,
                "client_secret": client_secret
        }

        # Auth Step 5: tokens are returned to the app
        post_request = requests.post(SPOTIFY_TOKEN_URL, data = code_payload)

        # convert to json
        response_data = json.loads(post_request.text)
        access_token = response_data['access_token']

        auth_header = {"Authorization": "Bearer {}".format(access_token)}

        return auth_header


# -----------------  ACCESSING THE API----------------

def spotify_search( search_type, query, auth_header):

        endpoint = 'https://api.spotify.com/v1/search'

        data = {'query': query,
                'type': search_type,
                'limit': 50
                }

        response = requests.get(endpoint, params = data, headers = auth_header)
        
        response_json = response.json()

        print(search_type)
        filtered = {}

        if search_type == ['artist']:
                filtered = response_json['artists']['items']
        elif search_type == 'album':
                filtered = response_json['albums']['items']
        elif search_type == 'playlist':
                filtered = response_json['playlists']['items']
        else:
                filtered = {}

        print(filtered)
        return  filtered


