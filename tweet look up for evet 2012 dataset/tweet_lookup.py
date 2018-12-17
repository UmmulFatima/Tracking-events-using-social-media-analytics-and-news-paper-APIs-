import tweepy
from itertools import islice
import re
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS

punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'", '!', '#', '$', '%', '&', '*', '+', '-', '<', '=', '>', '^', '_', '{', '|','}', '~']

consumer_key = 'RtdTtilPMop1lGHBU2EwkTGr4'
consumer_secret = 'M1PFruCj7zNRb6a4DGsJQyysz1iGNjcaG8lr3Aj4wRogRUXar5'
access_token = '940709647652196354-VOjpjbJDL95PBFMaIstpx4F0NboGQl7'
access_token_secret = 'lD2IscgpN65h9yhiwI7QKhY1dzCcSFWYDoYJ4NZkwlFap'

# for(i =0; i< 121535665; i=i+100)
for i in range(1, 121535665, 100):
    j = i + 99
    with open('tweet_ids_only.txt', 'r') as infile:
        #j = i + 99
        print('value of i and j', i, j)
        lines_gen = islice(infile, i, j)
        lines = []
        for line in lines_gen:
            lines.append(line)
        lines[:] = [line.rstrip('\n') for line in lines]
        #print('list of ids', lines)
        #print('length of list', len(lines))

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        tweets = api.statuses_lookup(lines)
        with open('tweetText.csv', 'a') as f:
            for tweet in tweets:
                date = tweet.created_at
                text = tweet.text
                # Removing HASH symbol
                tweet_text = text.replace("#", "").replace("_", " ")
                tweet_text = tweet_text.replace("&", "").replace("_", " ")
                # Removing the Hex characters(emoji)
                tweetText = re.sub(r'[^\x00-\x7f]', r'', tweet_text)
                # removing punctuations
                tweetText = re.sub(r'[^a-zA-Z0-9@\S]', ' ', tweetText)
                remove_pun = str.maketrans({key: None for key in punctuation})
                tweetText = tweetText.translate(remove_pun)
                #f.write("\n%s;%s" % (date, tweetText))
                #print(date,tweetText)
f.close()