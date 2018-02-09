#-----------------------------------------------------------------------
# twitter-trends
#  - lists the current global trending topics
#-----------------------------------------------------------------------

import tweepy
from tweepy import OAuthHandler
import sys
import matplotlib.mlab as mlab
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

sys.stdout = open('output_trendstest.txt','wt')

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


# put all the names together with a ' ' separating them
trendsName = ' '.join(trend_list)
print(trendsName)

def get_hashtags(trendsName, order=False):
    tags = set([item.strip("#.,-\"\'&*^!") for item in trendsName.split() if (item.startswith("#") and len(item) < 256)])
    return sorted(tags) if order else tags
print("\n".join(get_hashtags(trendsName, True)))

#counts = Counter(trend_list)
# labels, values = zip(*counts.items())

# # sort your values in descending order
# indSort = np.argsort(values)[::-1]

# # rearrange your data
# labels = np.array(labels)[indSort]
# values = np.array(values)[indSort]

# indexes = np.arange(len(labels))

# bar_width = 0.35

# plt.bar(indexes, values)

# # add labels
# plt.xticks(indexes + bar_width, labels)
# plt.show()