from __future__ import absolute_import, print_function
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.api import API
import csv
import json
import numpy as np
import codecs
from datetime import datetime
import sys, tweepy, csv
import numpy as np
import re, string, timeit
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

consumer_key="RtdTtilPMop1lGHBU2EwkTGr4"
consumer_secret="M1PFruCj7zNRb6a4DGsJQyysz1iGNjcaG8lr3Aj4wRogRUXar5"
access_token="940709647652196354-VOjpjbJDL95PBFMaIstpx4F0NboGQl7"
access_token_secret="lD2IscgpN65h9yhiwI7QKhY1dzCcSFWYDoYJ4NZkwlFap"

#loc = [-0.351468,51.38494,0.148271,51.672343]
loc = [-7.9916607813,50.314954465,1.8081439062,60.9157]



LANGUAGES = ['en']

stop = set(stopwords.words('english'))
punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"] 

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout."""
    def on_data(self, data):
        #Just write data to one line in the file, Convert the data to a json object
        j=json.loads(data)

        #date time formatting from json data 
        unformatted = j["created_at"]
        remove_ms = lambda x:re.sub("\+\d+\s","",x) # Use re to get rid of the milliseconds.
        mk_dt = lambda x:datetime.strptime(remove_ms(x), "%a %b %d %H:%M:%S %Y")# Make the string into a datetime object.
        my_form = lambda x:"{:%Y-%m-%d %H:%M:%S}".format(mk_dt(x))# Format your datetime object.
        l = my_form(unformatted)
        print(l)
        
        tweet_text = j["text"]
        #Stripping the URLs    
        tweetText = re.sub(r"(?:\|https?\://)\S+", "", tweet_text, flags=re.MULTILINE)    
        
        # Removing HASH
        tweetText = re.sub(r'#\w+ ?', '', tweetText)

        # Removing the Hex characters
        tweetText = re.sub(r'[^\x00-\x7f]',r'', tweetText)

        #removing puntuations
        tweetText = re.sub(r'[^a-zA-Z0-9@\S]', ' ', tweetText)

        fhOut.write("\n%s,%s" % (l, tweetText))

        print(tweetText)
        return 1

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    try:
        fhOut = codecs.open("tweet_v6.csv", "w+", "utf-8")
        fhOut.write('date,text')

        #Create the listener
        listener = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        
        stream = Stream(auth, listener)
        stream.filter(locations = loc, languages=LANGUAGES)
    except KeyboardInterrupt:
    #User pressed ctrl+c -- get ready to exit the program
        pass
    fhOut.close()