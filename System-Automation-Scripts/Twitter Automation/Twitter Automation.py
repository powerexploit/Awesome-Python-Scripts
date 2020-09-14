

#Importing Library
import tweepy
import time

#Twitter Authentication APIs
CONSUMER_KEY = '<enter-your-consumer-key>'
CONSUMER_SECRET = '<enter-your-consumer-secret-key>'
ACCESS_KEY = '<enter-your-access-key>'
ACCESS_SECRET = '<enter-your-access-secret-key>'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#Likes & Retweeting
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()
search = '#india'
numTweet = 500
for tweet in tweepy.Cursor(api.search, search).items(numTweet):
    try:
        print('Tweet Liked')   #Like
        tweet.favorite()
        print("Retweet done")  #Retweet
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

##Press 'i' to stop iteration in jupyter notebook