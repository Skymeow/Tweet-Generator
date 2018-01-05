from requests_oauthlib import OAuth1Session

consumer_key = "QSvRQvhgc2G8S6pOGnA2aUKk1"
consumer_secret = "zKBtynk4EbsYmM7skdNBiQHHh4es2VwyztdFnyARVLJyDpIaxO"
access_token = "949074237968465920-Om8Fx5I6HFBazyD1is0fhlSLEt0xW7S"
access_token_secret = "VebiPHFilNvwPzWOiEfsDO75wFLwpcdKqzWo1IJq95zfL"

session = OAuth1Session(consumer_key,
                        client_secret=consumer_secret,
                        resource_owner_key=access_token,
                        resource_owner_secret=access_token_secret)
url = 'https://api.twitter.com/1.1/statuses/update.json'


def tweet(status):
    resp = session.post(url, { 'status': status })
    return resp.text
