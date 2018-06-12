import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter


CONSUMER_KEY = '1ot3DdKC1ebpBmO5hPpNBXtFB'
CONSUMER_SECRET = 'VOLEE9DtQeGplGtgJRMKzrfLqGZfxv2idoHf8Y2GAJWK1UjA6B'
OAUTH_TOKEN = '961035808638726144-VHG2KAHSf5vMv3PDgK60AAqZKziEZHS'
OAUTH_TOKEN_SECRET = 'OsFCPefR6Mb5dkVbYXqlr5aJUblmocVflodR2cAVsn70K'

auth = OAuthHandler(CONSUMER_KEY,  CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

count = 150
query = 'Ireland'

#get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

min_retweets = 10 #the min amount of times a status is retweeted to gain entry to the list
                    #reset this value to suit your own tastes
                    
pop_tweets = [status
            for status in results
                if status._json['retweet_count'] > min_retweets]
            
#create a list of tweet tuples associating each tweet's text with its retweet count
tweet_tups = [(tweet._json['text'].encode('utf-8'), tweet._json['retweet_count'])
                for tweet in pop_tweets]

#Sort the tuple entries in descending order
most_popular_tups = sorted(tweet_tups, key=itemgetter(1), reverse=True)[:5]

# prettify
table = PrettyTable(field_names=['Text', 'Retweet Count'])
for key, val in most_popular_tups:
    table.add_row([key, val])
table.max_width['Text'] = 50
table.align['Text'], table.align['Retweet Count'] = '1', 'r' #align the columns
print(table)
    
    
    
    
    
    
    
    







