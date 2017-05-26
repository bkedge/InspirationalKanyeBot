import tweepy
from config import *

#Setup OAuth
auth = tweepy.OAuthHandler(Consumer_Key, Consumer_Secret)

auth.set_access_token(Access_Key, Access_Secret)

api = tweepy.API(auth)

#Main
#user = api.get_user(screen_name = 'OfficiaIKanye')

KanyeID = 74346390

#print KanyeID

lastTweet = None

recentTweet = api.user_timeline('OfficiaIKanye')[0]
print(recentTweet.text)
