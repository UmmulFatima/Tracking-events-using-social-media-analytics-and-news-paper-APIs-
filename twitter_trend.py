import tweepy
from tweepy import OAuthHandler
import numpy as np
from datetime import datetime

consumer_key="RtdTtilPMop1lGHBU2EwkTGr4"
consumer_secret="M1PFruCj7zNRb6a4DGsJQyysz1iGNjcaG8lr3Aj4wRogRUXar5"
access_token="940709647652196354-VOjpjbJDL95PBFMaIstpx4F0NboGQl7"
access_token_secret="lD2IscgpN65h9yhiwI7QKhY1dzCcSFWYDoYJ4NZkwlFap"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# retrieve global trends. Location is specified by looking up WOE IDs:
trends1 = api.trends_place(23424975)
data = trends1[0]
trends = data['trends']

# grab the name from each trend
trend_list = [trend['name'] for trend in trends]
a = np.array(trend_list)
the_list = a.tolist()
cur_time = datetime.now().strftime("%Y%m%d-%H%M%S")
file_name = "trend"+str(cur_time)+".txt"

with open('trends/' + file_name, 'w') as file_handler:
    for item in trend_list:
        file_handler.write("{}\n".format(item))

# start_time = time.time()
# time_dif = 0
# try:
#     while(time_dif<3):
#         trends1 = api.trends_place(23424975)
#         data = trends1[0]
#         trends = data['trends']
#         # grab the name from each trend
#         trend_list = [trend['name'] for trend in trends]
#         cur_time = time.time()
#         file_name = "trend"+str(cur_time)+".txt"
#         a = np.array(trend_list)
#         the_list = a.tolist()
#         with open(file_name, 'w') as file_handler:
#             for item in trend_list:
#                 file_handler.write("{}\n".format(item))
#         time_dif = cur_time - start_time
#         hours, rest = divmod(time_dif, 3600)
#
#         minutes, seconds = divmod(rest, 60)
#
#         time_dif=minutes
#         print(time_dif)
# except:
#     print('r')
