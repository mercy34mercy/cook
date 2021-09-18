import tweepy
import time
import urllib.request
import urllib.error

# 検索キーワード
TARGET = '#ベストオブ藤吉夏鈴2020'

# 画像の保存先
IMG_DIR = '画像の保存先を絶対パスで記述'

# 環境変数
API_KEY = "goRrBpS261OBxxjXsSZhsBP1n"
API_SECRET = "9S2PfhdZWNbgWxzlUZQj8QSBorCUu36YPmx4tn32KvoVmdj4oa"
ACCESS_TOKEN_KEY = "2773244862-PbpeoggUQUDJPxyrfn21DkCDC1mxfcODlBzMm3U載"
ACCESS_TOKEN_SECRET = "WVaXUEVfFQ2Lo7NqgOvOwJRVCUqoSluLFWfopih6PXuj2"

# 検索オプション
SEARCH_PAGES_NUMBER = 100  # 読み込むページ数
PER_PAGE_NUMBER = 100  # ページごとに返されるツイートの数


class execute(object):
   def __init__(self):
      # 初期設定
      super(imageDownloader, self).__init__()
      self.set_api()

   def run(self):
      # ページを跨ぐ検索対象IDの初期化
      self.max_id = None

      for page in range(SEARCH_PAGES_NUMBER):
         # ページごとに画像のURLを取得
         ret_url_list = self.search(TARGET, PER_PAGE_NUMBER)

         # 画像をダウンロード
         for url in ret_url_list:
            print('OK ' + url)
            self.download(url)

         # TimeOut防止
         time.sleep(0.1) 

   def set_api(self):
      # APIの設定
      auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
      auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
      self.api = tweepy.API(auth)

   def search(self, target, rpp):
      # 検索結果
      ret_url_list = []

      try:
         # 検索実行
         if self.max_id:
            res_search = self.api.search(q=target, lang='ja', rpp=rpp, max_id=self.max_id)
         else:
            res_search = self.api.search(q=target, lang='ja', rpp=rpp)

         # 結果を保存
         for result in res_search:
            if 'media' not in result.entities:
               continue

            for media in result.entities['media']:
               url = media['media_url_https']
               if url not in ret_url_list:
                  ret_url_list.append(url)

         # 検索済みidの更新
         self.max_id = result.id

         # 検索結果の返却
         return ret_url_list
      except Exception as e:
         self.error_catch(e)

   def download(self, url):
      # 画像のダウンロード
      url_orig = '%s:orig' % url
      path = IMG_DIR + url.split('/')[-1]
      try:
         response = urllib.request.urlopen(url=url_orig)
         with open(path, "wb") as f:
            f.write(response.read())
      except Exception as e:
         self.error_catch(e)

   def error_catch(self, error):
      # エラー処理
      print("NG ", error)


def main():
   # メイン処理
   execute = execute()
   execute()


if __name__ == '__main__':
   main()