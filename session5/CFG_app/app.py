from flask import Flask, render_template, request, redirect, session
from helpers.twitter import authenticate, collect_tweets

app = Flask("Tweets scraper")
session = {}

@app.route('/')
def index():
    """ This will be the landing page for the app we will be using:
    this is intended to serve as an app accessing and displaying data from
    APIS"""
    return render_template('index.html', title = 'Landing page')

@app.route("/twitter")
def twitter_example():
    return render_template("twitter.html")

@app.route("/twitter_search", methods = ['POST'])
def twitter_search_app():
    query = request.form['query']

    tweets = collect_tweets(query)


    return render_template('tweets_show.html', search_string=query,
                           tweets =tweets)


# "debug=True" causes Flask to automatically refresh upon any changes you
# make to this file.
app.run(debug=True)