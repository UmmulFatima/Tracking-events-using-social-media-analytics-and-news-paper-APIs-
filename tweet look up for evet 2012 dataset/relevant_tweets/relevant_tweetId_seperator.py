import tweepy
from itertools import islice
import re
import  csv

punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]

consumer_key = 'RtdTtilPMop1lGHBU2EwkTGr4'
consumer_secret = 'M1PFruCj7zNRb6a4DGsJQyysz1iGNjcaG8lr3Aj4wRogRUXar5'
access_token = '940709647652196354-VOjpjbJDL95PBFMaIstpx4F0NboGQl7'
access_token_secret = 'lD2IscgpN65h9yhiwI7QKhY1dzCcSFWYDoYJ4NZkwlFap'
with open('relevant_tweets.tsv', 'r') as infile:
    rd = csv.reader(infile, delimiter="\t", quotechar='"')
    tweet_ids = []
    for line in infile:
        lines = line.split("\t")
        ids = lines[-1]
        print(lines[0])
        tweet_ids.append(ids)
    tweet_ids[:] = [line.rstrip('\n') for line in tweet_ids]
    print(tweet_ids)

    # with open('r_tweetIds.csv', 'a') as f:
    #     for i in range(0, len(tweet_ids)):
    #         l = tweet_ids[i]
    #         f.write("\n%s" % (l))
    #         print(l)

