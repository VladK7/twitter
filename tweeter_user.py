import tweepy
from tweepy import OAuthHandler



CONSUMER_KEY = '1ot3DdKC1ebpBmO5hPpNBXtFB'
CONSUMER_SECRET = 'VOLEE9DtQeGplGtgJRMKzrfLqGZfxv2idoHf8Y2GAJWK1UjA6B'
OAUTH_TOKEN = '961035808638726144-VHG2KAHSf5vMv3PDgK60AAqZKziEZHS'
OAUTH_TOKEN_SECRET = 'OsFCPefR6Mb5dkVbYXqlr5aJUblmocVflodR2cAVsn70K'

auth = OAuthHandler(CONSUMER_KEY,  CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    #Process a tweet
    print(status.text)