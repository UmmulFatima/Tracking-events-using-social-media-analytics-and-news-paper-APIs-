#-----------------------------------------------------------------------
# twitter-trends
#  - lists the current global trending topics
#-----------------------------------------------------------------------

import tweepy
from tweepy import OAuthHandler
#import sys
import matplotlib.mlab as mlab
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

#sys.stdout = open('output_trendstest.txt','wt')

consumer_key="RtdTtilPMop1lGHBU2EwkTGr4"
consumer_secret="M1PFruCj7zNRb6a4DGsJQyysz1iGNjcaG8lr3Aj4wRogRUXar5"
access_token="940709647652196354-VOjpjbJDL95PBFMaIstpx4F0NboGQl7"
access_token_secret="lD2IscgpN65h9yhiwI7QKhY1dzCcSFWYDoYJ4NZkwlFap"

#-----------------------------------------------------------------------
# twitter auth
#-----------------------------------------------------------------------
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#-----------------------------------------------------------------------
# retrieve global trends.
# other localised trends can be specified by looking up WOE IDs:
#   http://developer.yahoo.com/geo/geoplanet/
# twitter API docs: https://dev.twitter.com/rest/reference/get/trends/place
#-----------------------------------------------------------------------

#london woeid 44418

trends1 = api.trends_place(44418)
data = trends1[0] 

# grab the trends
trends = data['trends']

# grab the name from each trend
trend_list = [trend['name'] for trend in trends]
#print(trend_list)

#a = np.array(trend_list)
#the_list = a.tolist()
with open('trending_event.txt', 'w') as file_handler:
    for item in trend_list:
    	file_handler.write("{}\n".format(item))