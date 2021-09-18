import os
import tweepy
from time import sleep
import urllib.error
import urllib.request

def get_tweet():

    CONSUMER_KEY = os.environ.get("goRrBpS261OBxxjXsSZhsBP1n")
    CONSUMER_SECRET = os.environ.get("9S2PfhdZWNbgWxzlUZQj8QSBorCUu36YPmx4tn32KvoVmdj4oa")
    ACCESS_TOKEN = os.environ.get("2773244862-PbpeoggUQUDJPxyrfn21DkCDC1mxfcODlBzMm3U")
    ACCESS_SECRET = os.environ.get("WVaXUEVfFQ2Lo7NqgOvOwJRVCUqoSluLFWfopih6PXuj2")

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)


    api = tweepy.API(auth)
    user = api.get_user('twitter')

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)
        return tweet.text