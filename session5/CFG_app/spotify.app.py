# importing Requests: HTTP for Humans - installed previsouly
import requests

# making a search request to the Spotify API to return
# any artist with **** in their name.

# Info on the Spotify API is https://developer.spotify.com/web-api/endpoint-reference/

response = requests.get('https://api.spotify.com/v1/search?query=lil&type=artist&limit=50&market=US')
# converts the response from a string to a json object that can be parsed in Python.
data = response.json()


url = 'https://api.spotify.com/v1/search'

data = {'query':'lil',
        'type':'artist',
        'limit':50
}

r = requests.get(url, params = data)