from six import int2byte
import tweepy
from time import sleep
import urllib.error
import urllib.request
import random

def get_tweet(kaisu):
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
    ret_tweet_list = []

    kensaku_list = ["美女","ミスコン","浴衣","女優","美人","アイドル"]

    #北海道　　東北　　関東　　中国 　　四国　　九州　関西　中部

    tiho_lkist = ["#北海道 OR #北海道美人 OR #札幌 OR #札幌美人 OR #ミス北海道","#青森 OR #秋田 OR 秋田 OR #岩手 OR #山形 OR #宮城 OR #福島 OR #青森美人 OR #秋田美人 OR 秋田美人 OR #岩手美人 OR #山形美人 OR #宮城美人 OR #福島美人 OR #東北大","#東京 OR #埼玉 OR #茨城 OR #栃木 OR #群馬 OR #千葉 OR #神奈川","#静岡 OR #新潟 OR #岐阜 OR #愛知 OR #長野 OR #福井 OR #石川 OR #富山","#京都 OR #滋賀 OR #大阪 OR #和歌山 OR #奈良 OR #兵庫","#岡山 OR #広島 OR #鳥取 OR #山口 OR #島根","#愛媛 OR #香川 OR #徳島 OR #高知","#福岡 OR #長崎 OR #熊本 OR #大分 OR #佐賀 OR #宮崎 OR #鹿児島 OR #沖縄"]

    i = 0 

    while(len(ret_tweet_list)<20):
        one = (kensaku_list[i],tiho_lkist[kaisu])
        i = i +1 
        #res_search = api.search(q=one + " " + two, lang='ja')

        a = 10


    

        res_search = tweepy.Cursor( api.search, q=one, tweet_mode='extended', result_type="mixed", include_entities=True).items(100)
    


        for result in res_search:
            if 'media' not in result.entities:
                continue

            for media in result.entities['media']:
                url = media['media_url_https']
                tweet = media['url']
                print(url)
                if url not in ret_url_list: ret_url_list.append(url)
                if tweet not in ret_tweet_list: ret_tweet_list.append(tweet)

    
    random_sorce = int(len(ret_url_list)-9)

    

    r = int(random.randint(0,random_sorce))

    r_url = []
    r_tweet = []

    for i in range(r,r+9):
        r_url.append(ret_url_list[i])
        r_tweet.append(ret_tweet_list[i])


    return r_url,r_tweet


get_tweet(0)

    
    

    

    
    
 




    