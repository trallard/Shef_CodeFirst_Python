# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:30:02 2017

@author: Tania
"""

import tweepy
import yaml
import os


# This will load the configuration variables for the API's
def get_config():
    # Check if there is already a configuration file
    if not os.path.isfile('config.yml'):
        print('No config file found, make sure you have one')
    else:
        with open("config.yml", 'r') as ymlfile:
            keys = yaml.load(ymlfile)

    return keys


def authenticate():
    config = get_config()
    auth = tweepy.OAuthHandler(config['twitter']['consumer_key'],config['twitter']['consumer_secret'])
    auth.set_access_token(config['twitter']['access_token'],config['twitter']['access_secret'])

    twitter_api = tweepy.API(auth)

    print('Logged in as {}'.format(twitter_api.me().name))
    return twitter_api


def collect_tweets(keyword):
    keyword = keyword.strip()
    twitter = authenticate()
    print('Finding tweets with {} keyword'.format(keyword))
    tweets = twitter.search(keyword)
    return tweets


def stalker(victim, no):
    "This will find a certain number of tweets from our victim"
    tweets = twitter.user_timeline(screen_name=victim, count=no)
    print("Number of tweets extracted: {}.\n".format(len(tweets)))


def show_content(tweets):
    for tweet in tweets:
        print("\n" + tweet.text)


def post_tweet(status):
    twitter.update_status(status=status)


def see_timeline(no):
    for tweet in tweepy.Cursor(twitter.home_timeline).items(no):
        print("\n {} tweeted by {}".format(status.text, status.user.name))


