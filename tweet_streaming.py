from __future__ import absolute_import, print_function
import codecs
import json
import re
from datetime import datetime
from nltk.corpus import stopwords
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = "RtdTtilPMop1lGHBU2EwkTGr4"
consumer_secret = "M1PFruCj7zNRb6a4DGsJQyysz1iGNjcaG8lr3Aj4wRogRUXar5"
access_token = "940709647652196354-VOjpjbJDL95PBFMaIstpx4F0NboGQl7"
access_token_secret = "lD2IscgpN65h9yhiwI7QKhY1dzCcSFWYDoYJ4NZkwlFap"

# loc = [-7.9916607813, 50.314954465, 1.8081439062, 60.9157]
loc = [-1.7326, 51.1233, 0.2999, 51.8892]

LANGUAGES = ['en']

stop = set(stopwords.words('english'))
punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]


class StdOutListener(StreamListener):

    def on_data(self, data):

        # Just write data to one line in the file, Convert the data to a json object
        tweet_data = json.loads(data)
        if "extended_tweet" in tweet_data:
            # tweet = tweet_data['extended_tweet']['full_text']
            # print('full tweet with RT', tweet)
            if not tweet_data['extended_tweet']['full_text'].startswith('RT'):
                tweet_time = tweet_data["created_at"]
                # Use re to get rid of the milliseconds.
                remove_ms = lambda x: re.sub("\+\d+\s", "", x)
                # Make the string into a datetime object.
                mk_dt = lambda x: datetime.strptime(remove_ms(x), "%a %b %d %H:%M:%S %Y")
                my_form = lambda x: "{:%Y-%m-%d %H:%M:%S}".format(mk_dt(x))
                tweet_time = my_form(tweet_time)

                tweet_text = tweet_data['extended_tweet']['full_text']
                # print(tweet_text)

                # Removing HASH symbol
                tweet_text = tweet_text.replace("#", "").replace("_", " ")
                # print('removing hash character and underscore', tweet_text)

                # Removing the Hex characters(emoji)
                tweetText = re.sub(r'[^\x00-\x7f]', r'', tweet_text)
                # print('Removing the Hex characters', tweetText)

                # removing punctuations
                # tweetText = re.sub(r'[^a-zA-Z0-9@\S]', ' ', tweetText)
                remove_pun = str.maketrans({key: None for key in punctuation})
                tweetText = tweetText.translate(remove_pun)
                # print('removing punctuation', tweetText)

                fhOut.write("\n%s;%s" % (tweet_time, tweetText))
                print(tweet_time, tweetText)
                return True

    def on_error(self, status_code):
        if status_code == 420:
            return False


if __name__ == '__main__':
    try:
        cur_time = datetime.now().strftime("%Y%m%d-%H%M%S")
        file_name = "new_tweets" + str(cur_time) + ".csv"

        fhOut = codecs.open('tweets/' + file_name, "w+", "utf-8")
        fhOut.write('date;text')
        listener = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, listener, tweet_mode='extended')
        stream.filter(locations=loc, languages=LANGUAGES)

    except KeyboardInterrupt:
        pass
    fhOut.close()
