from __future__ import absolute_import, print_function
<<<<<<< HEAD
=======

>>>>>>> dc4e6cf78b52506e8eb12ba8b1e1ec2604b8933e
import codecs
import json
import re
from datetime import datetime
<<<<<<< HEAD
=======

>>>>>>> dc4e6cf78b52506e8eb12ba8b1e1ec2604b8933e
from nltk.corpus import stopwords
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = "RtdTtilPMop1lGHBU2EwkTGr4"
consumer_secret = "M1PFruCj7zNRb6a4DGsJQyysz1iGNjcaG8lr3Aj4wRogRUXar5"
access_token = "940709647652196354-VOjpjbJDL95PBFMaIstpx4F0NboGQl7"
access_token_secret = "lD2IscgpN65h9yhiwI7QKhY1dzCcSFWYDoYJ4NZkwlFap"

loc = [-7.9916607813, 50.314954465, 1.8081439062, 60.9157]
LANGUAGES = ['en']

stop = set(stopwords.words('english'))
punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]


class StdOutListener(StreamListener):

    def on_data(self, data):
        # Just write data to one line in the file, Convert the data to a json object
        j = json.loads(data)
        if not j["text"].startswith('RT'):
            unformatted_time = j["created_at"]
<<<<<<< HEAD
            # Use re to get rid of the milliseconds.
            remove_ms = lambda x: re.sub("\+\d+\s", "", x)
=======

            # Use re to get rid of the milliseconds.
            remove_ms = lambda x: re.sub("\+\d+\s", "", x)

>>>>>>> dc4e6cf78b52506e8eb12ba8b1e1ec2604b8933e
            # Make the string into a datetime object.
            mk_dt = lambda x: datetime.strptime(remove_ms(x), "%a %b %d %H:%M:%S %Y")
            my_form = lambda x: "{:%Y-%m-%d %H:%M:%S}".format(mk_dt(x))
            formatted_time = my_form(unformatted_time)

            tweet_text = j["text"]
<<<<<<< HEAD
            print(tweet_text)

            # Stripping the URLs
            #tweetText = re.sub(r"http\S+", "", tweet_text, flags=re.MULTILINE)
            #tweetText = re.sub(r"(?:\|https?\://)\S+", "", tweetText, flags=re.MULTILINE)
            #print('Stripping the URLs', tweetText)

            # Removing the Hex characters
            tweetText = re.sub(r'[^\x00-\x7f]', r'', tweet_text)
            print('Removing the Hex characters', tweetText)

            # removing punctuations
            tweetText = re.sub(r'[^a-zA-Z0-9@\S]', ' ', tweetText)
            remove_pun = str.maketrans({key: None for key in punctuation})
            tweetText = tweetText.translate(remove_pun)
            print('removing punctuation', tweetText)
=======
            # Stripping the URLs
            tweetText = re.sub(r"(?:\|https?\://)\S+", "", tweet_text, flags=re.MULTILINE)
            # Removing HASH
            # tweetText = re.sub(r'#\w+ ?', '', tweetText)
            # Removing the Hex characters
            tweetText = re.sub(r'[^\x00-\x7f]', r'', tweetText)
            # removing puntuations
            tweetText = re.sub(r'[^a-zA-Z0-9@\S]', ' ', tweetText)
>>>>>>> dc4e6cf78b52506e8eb12ba8b1e1ec2604b8933e

            fhOut.write("\n%s,%s" % (formatted_time, tweetText))
            print(formatted_time, tweetText)
            return True

    def on_error(self, status_code):
        if status_code == 420:
            return False


if __name__ == '__main__':
    try:
        cur_time = datetime.now().strftime("%Y%m%d-%H%M%S")
        file_name = "tweets" + str(cur_time) + ".csv"

        fhOut = codecs.open('tweets/' + file_name, "w+", "utf-8")
        fhOut.write('date,text')
        listener = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, listener)
        stream.filter(locations=loc, languages=LANGUAGES)

    except KeyboardInterrupt:
        pass
    fhOut.close()
