import csv
from itertools import islice
import tweepy

punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'", '!', '#', '$', '%', '&', '*', '+', '-', '<', '=', '>', '^', '_', '{', '|','}', '~']

consumer_key = 'RtdTtilPMop1lGHBU2EwkTGr4'
consumer_secret = 'M1PFruCj7zNRb6a4DGsJQyysz1iGNjcaG8lr3Aj4wRogRUXar5'
access_token = '940709647652196354-VOjpjbJDL95PBFMaIstpx4F0NboGQl7'
access_token_secret = 'lD2IscgpN65h9yhiwI7QKhY1dzCcSFWYDoYJ4NZkwlFap'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

with open('relevant_tweets.tsv', 'r') as file:

    event_counter = 0
    counter = 0
    event_dict = dict()

    for line in file:
        line = line.split("\t")
        event_id = int(line[0])
        tweet_id = line[-1]

        tweet_id =[tweet_id.rstrip('\n')]
        tweets = api.statuses_lookup(tweet_id)
        print(tweets)

        if tweets:
            # print(tweets[0].text)
            if event_id == counter:
                event_counter += 1
            else:
                event_dict[counter] = event_counter
                print(event_dict)
                event_counter = 0
                counter += 1
    print(event_dict)