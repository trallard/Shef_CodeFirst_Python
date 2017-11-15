from flask import Flask, render_template, request, redirect, session
from helpers.twitter import authenticate, collect_tweets, get_config
from helpers.spotify import  authorize_spotify, AUTH_URL, spotify_search

import requests

app = Flask("APIs query for CFG")
session = {}

# -------------- This is where you'll start accessing the app --------------
@app.route('/')
def index():
    """ This will be the landing page for the app we will be using:
    this is intended to serve as an app accessing and displaying data from
    APIS"""
    keys = get_config()
    return render_template('index.html')


# -------------- For Twitter API queries --------------

@app.route("/twitter")
def twitter_handler():
    """ This should display a form where the users introduce the terms
    they want to look for in Twitter"""
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
    """Auth Step 1: Authorization"""

    return redirect(AUTH_URL.url)

@app.route('/callback/')
def callback():
    """Auth Step 4: Requests refresh and access tokens"""
    auth_token = request.args['code']
    auth_header = authorize_spotify(auth_token)

    session['auth_header'] = auth_header

    return render_template("spotify.html", auth_header = auth_header)


@app.route("/spotify_search", methods = ['POST'])
def spotify_search_app():
    """When the search is submitted from the previous page,
    this function passes the form data to our python scripts
    and uses them to perform the query. It will then return the tweets
    and display them in /tweets_show"""

    if 'auth_header' in session:
        auth_header = session['auth_header']

    query = request.form['query']
    search_type = request.form.getlist('type')

    data = spotify_search(search_type, query, auth_header)

    return render_template('spotify_show.html', data = data, query = query, search_type = search_type)

# "debug=True" causes Flask to automatically refresh upon any changes you
# make to this file.
app.run(debug=True)