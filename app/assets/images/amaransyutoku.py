import feedparser
import URL_Shortening
import tweepy
import random

CONSUMER_KEY = "avp78vgzl5YhHrS7MGWU5cEOE"
CONSUMER_SECRET = "6Qj1dXs0dPjoKHP1JIwxFyLwj9XIdbcsuAwnA3ANqFcTokM9QB"
ACCESS_TOKEN = "948531295310630912-7SQqE0VWkjYLpoJ9BMSkFlErDQjw6Cl"
ACCESS_TOKEN_SECRET = "iPBxqf9L5krkt9j8L8Gw1fiUNIiADH15APmuVBEJsNuWe"

url = [
    "http://www.amazon.co.jp/gp/rss/bestsellers/books/466284/", #文学・評論
    "https://www.amazon.co.jp/gp/rss/bestsellers/videogames/", #ゲーム
    "https://www.amazon.co.jp/gp/rss/bestsellers/dvd/", #DVD
    "https://www.amazon.co.jp/gp/rss/bestsellers/electronics/", #家電・カメラ
    "https://www.amazon.co.jp/gp/rss/bestsellers/appliances/", #大型家電
    "https://www.amazon.co.jp/gp/rss/bestsellers/kitchen/", #ホーム・キッチン
    "https://www.amazon.co.jp/gp/rss/bestsellers/beauty/", #ビューティー
    "https://www.amazon.co.jp/gp/rss/bestsellers/digital-text/", #KINDLE
    ]
feed = feedparser.parse(random.choice(url))
access_token2 = "ce8729b129adb8e4eb0a6eda7d4ae3a987c11f51"

def main():
    makeApi().update_status(STATUS_DATA)


def makeApi():
    """Return tweepy.API object"""

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

for entry in feed['entries']:
    print("売上ランキング　第", entry.title)
    print("published: ", entry.published)
    print("link: ", URL_Shortening.GET_Url(access_token2,entry.link + "&tag=makito0420-22"))
    print("link1: ", entry.link + "&tag=makito0420-22")
    STATUS_DATA = "　第" + entry.title[1:2] + "位 " + entry.title[4:] + " " + entry.link + "&tag=makito0420-22"

    # print("description: ", entry.description)
    if __name__ == "__main__" and entry.title[1:3] == '1:':
        main()
