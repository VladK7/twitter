import json
import tweepy
from tweepy import OAuthHandler


CONSUMER_KEY = '1ot3DdKC1ebpBmO5hPpNBXtFB'
CONSUMER_SECRET = 'VOLEE9DtQeGplGtgJRMKzrfLqGZfxv2idoHf8Y2GAJWK1UjA6B'
OAUTH_TOKEN = '961035808638726144-VHG2KAHSf5vMv3PDgK60AAqZKziEZHS'
OAUTH_TOKEN_SECRET = 'OsFCPefR6Mb5dkVbYXqlr5aJUblmocVflodR2cAVsn70K'

auth = OAuthHandler(CONSUMER_KEY,  CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

DUB_WOE_ID = 560743
LON_WOE_ID = 44418
NY_WOE_ID = 2459115
TOR_WOE_ID = 4118

ny_trends = api.trends_place(NY_WOE_ID)
tor_trends = api.trends_place(TOR_WOE_ID)

ny_trends_set = set([trend['name']
                    for trend in ny_trends[0]['trends']])

tor_trends_set = set([trend['name']
                    for trend in tor_trends[0]['trends']])

common_trends = set.intersection(ny_trends_set, tor_trends_set)

print(common_trends)
