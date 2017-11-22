# -*- coding: utf-8 -*-
"""
@author: Tania @trallard
This script contains the necessary functions to query the Twitter API and
return lists containing the tweets data.
The queries are done using Tweepy, a Python library for Twitter's API
In this case we are not using callback urls to request explicit permission
of the user although this could be adopted easily.
The functions to do this can be found in: helpers/twitter_auth.py
Note that in order to use the various functions here you have to authenticate first

"""

import tweepy
import yaml
import os


# This will load the configuration variables for the API's
def get_config():
    """This function checks if there is a configuration file
    and if so loads the keys stored in it. Note the config file can have
    extension .py, .ini. yaml .json
    The method to access it should be changed accordingly to the
    type of file you have in your project"""
    if not os.path.isfile('config.yml'):
        print('No config file found, make sure you have one')
    else:
        with open("config.yml", 'r') as ymlfile:
            keys = yaml.load(ymlfile)

    return keys


def authenticate():
    """This function will use Twitter's app keys provided in the config file
    to authenticate the user if successful, the login will be displayed on the screen"""
    config = get_config()
    auth = tweepy.OAuthHandler(config['twitter']['consumer_key'],config['twitter']['consumer_secret'])
    auth.set_access_token(config['twitter']['access_token'],config['twitter']['access_secret'])

    twitter_api = tweepy.API(auth)

    print('Logged in as {}'.format(twitter_api.me().name))
    return twitter_api


def collect_tweets(keyword):
    """This function will take the query terms for the form submitted by the user. The
     queries can be simple words, hashtags and or a mixture of both.
     It can receive multiple keywords at a time.
     Once the query is submitted via the form, the function access the API and retrieves
     the tweets which are stored in a list"""
    keyword = keyword.strip()
    twitter = authenticate()
    print('Finding tweets with {} keyword'.format(keyword))
    tweets = twitter.search(keyword)
    return tweets


def stalker(victim, no = 50):
    """The user needs to provide a Twitter handle e.g. @ixek to
    query the tweets for that user. If no number is provided
    the query will retrieve the last 50 tweets"""
    tweets = twitter.user_timeline(screen_name=victim, count=no)
    print("Number of tweets extracted: {}.\n".format(len(tweets)))
    return tweets


def show_content(tweets):
    """Once yiu have collected all your tweets using the previous functions
    e.g. stalker() or collect_tweets() you can print their content by calling
    this function"""
    for tweet in tweets:
        print("\n" + tweet.text)


def post_tweet(status):
    """This Function will submit a Tweet for you. In order to do this
    you need to call the function with a valid string. Note you can also
    add emojis. E.g
    post_status("Python is awesome") """
    twitter.update_status(status=status)


def see_timeline(no):
    """This function acts as a spy on your own timeline. When used it will
    collect all the visible Tweets in your timeline until it reaches the specified
    limit. The tweets will be printed on the terminal as they are being collected"""
    for tweet in tweepy.Cursor(twitter.home_timeline).items(no):
        print("\n {} tweeted by {}".format(status.text, status.user.name))


