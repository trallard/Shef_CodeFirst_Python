# importing Requests: HTTP for Humans - installed previously
import requests

# Making a search request to the Spotify API to return
# any artist with **** in their name.

# Info on the Spotify API is https://developer.spotify.com/web-api/endpoint-reference/

# Spotify URLS needed for the authorization and queries

SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API = "https://api.spotify.com/v1"
redirect_uri = 'http://localhost:5000/callback/q'



def auth_spotify():
        """This function will handle the authorisation for
        Spotify API. It will make use of the authorisation
        callback """

        # retrieve the keys from the config file
        client_id = config['spotify']['client_id']
        client_secret = config['spotify']['client_secret']

        # these variables are needed to authenticate into the API
        auth_vars = {'response type': 'code',
                     'redirect_uri': 'redirect_uri',
                     'scope': 'scope',
                     'client_id': client_id}
        SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"

        url_args = "&".join(["{}={}".format(key, urllib.quote(val)) for key, val in auth_vars.iteritems()])
        auth_url = "{}/?{}".format(SPOTIFY_AUTH_URL, url_args)

        return auth_url


data = {'query':'lil',
        'type':'artist',
        'limit':50
}

r = requests.get(url, params = data)

def spotify_query(query, type):
        url = 'https://api.spotify.com/v1/search'
        response = request.get(url, params = data )
        return response