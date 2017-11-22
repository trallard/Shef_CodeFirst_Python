from flask import Flask, render_template, request, redirect, session
from helpers.twitter import authenticate, collect_tweets, get_config
from helpers.spotify import  authorize_spotify, spotify_search, get_auth
from helpers.NASA import get_APOD

import requests

app = Flask("APIs query for CFG")
session = {}

# -------------- This is what you will see straight away when you start the app --------------
@app.route('/')
def index():
    """ This will be the landing page for the app we will be using:
    this is intended to serve as an app accessing and displaying data from
    APIS"""
    keys = get_config()
    return render_template('index.html')


# -------------- Functions and decorators for Twitter API queries --------------

@app.route("/twitter")
def twitter_handler():
    """ This should display a form where the users introduce the terms
    they want to look for in Twitter, note this will use the keys saved
    to authenticate the user"""
    login = authenticate()
    return render_template("twitter.html", login = login)

@app.route("/twitter_search", methods = ['POST'])
def twitter_search_app():
    """When the search is submitted from the previous page,
    this function passes the form data to our python scripts
    and uses them to perform the query. It will then return the tweets
    and display them in /tweets_show"""
    query = request.form['query']
    tweets = collect_tweets(query)

    return render_template('tweets_show.html', search_string=query,
                           tweets = tweets)

# -------------- For Spotify API queries --------------

@app.route("/spotify")
def spotify_handler():
    """Spotify Authorisation is done in 5 steps:
     Auth Step 1: Authorisation"""
    AUTH_URL = get_auth()
    return redirect(AUTH_URL.url)

@app.route('/callback/')
def callback():
    """Auth Step 4: Requests refresh and access tokens, make sure this
    callback url is the same as the one you declared in your app and
    your functions"""
    auth_token = request.args['code']
    auth_header = authorize_spotify(auth_token)

    # This ensures the user is logged in for the duration of the session
    session['auth_header'] = auth_header

    return render_template("spotify.html", auth_header = auth_header)


@app.route("/spotify_search", methods = ['POST'])
def spotify_search_app():
    """The user can search for artists, playlists, or albums,
    similar to the Twitter example, the search will be passed to the
    API query functions and will return the data to be displayed in
    the appropriate template"""

    if 'auth_header' in session:
        auth_header = session['auth_header']
    else:
        print('User does not seem to be authenticated, return to the previous page')

    query = request.form['query']
    search_type = request.form.getlist('type')

    data = spotify_search(search_type, query, auth_header)

    return render_template('spotify_show.html', data = data, query = query, search_type = search_type)


# -------------- Functions and decorators for NASA API queries --------------

@app.route("/NASA")
def NASA_handler():
    """ This will only take you to the NASA search page"""

    return render_template("NASA.html")


@app.route("/NASA_search", methods = ['POST'])
def NASA_search_app():
    """When the search is submitted from the previous page,
    this function passes the form data to our python scripts
    and uses them to perform the query. It will then return the tweets
    and display them in /tweets_show"""
    date = request.form['date']
    APOD = get_APOD(date)

    return render_template('NASA_show.html', apod = APOD, date = date)


# "debug=True" causes Flask to automatically refresh upon any changes you
# make to this file.
app.run(debug=True)