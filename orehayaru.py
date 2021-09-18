import os
import tweepy
from time import sleep
import urllib.error
import urllib.request
import random

def get_tweet():
    #"goRrBpS261OBxxjXsSZhsBP1n"
    #"9S2PfhdZWNbgWxzlUZQj8QSBorCUu36YPmx4tn32KvoVmdj4oa"

    CONSUMER_KEY = "goRrBpS261OBxxjXsSZhsBP1n"
    CONSUMER_SECRET = "9S2PfhdZWNbgWxzlUZQj8QSBorCUu36YPmx4tn32KvoVmdj4oa"
    ACCESS_TOKEN = "2773244862-PbpeoggUQUDJPxyrfn21DkCDC1mxfcODlBzMm3U"
    ACCESS_SECRET = "WVaXUEVfFQ2Lo7NqgOvOwJRVCUqoSluLFWfopih6PXuj2"

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)


    api = tweepy.API(auth)
    user = api.get_user('twitter')

    ret_url_list = []

    kensaku_list = ["水着","美女","女性","かわいい","cute","girl","彼女","美人","アイドル","グラビア"]
    kensaku_list2 = ["美形","JK","ビューティー","マドンナ","色気","美少女","美魔女","pretty","可憐","かわいい"] 
    one = kensaku_list[random.randrange(9)]
    two = kensaku_list2[random.randrange(9)]

    res_search = api.search(q=one + " " + two, lang='ja')

         # 結果を保存
    for result in res_search:
        if 'media' not in result.entities:
            continue

        for media in result.entities['media']:
            url = media['media_url_https']
            if url not in ret_url_list: ret_url_list.append(url)
    
    if(len(ret_url_list) == 0):
        get_tweet()
    else:
        print("sccsess")
        return ret_url_list[random.randrange(len(ret_url_list))]



    
   




get_tweet()