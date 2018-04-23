from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import tweepy
#from geoloc import coordinates

ckey='RtdTtilPMop1lGHBU2EwkTGr4'
csecret='M1PFruCj7zNRb6a4DGsJQyysz1iGNjcaG8lr3Aj4wRogRUXar5'
atoken='940709647652196354-VOjpjbJDL95PBFMaIstpx4F0NboGQl7'
asecret='lD2IscgpN65h9yhiwI7QKhY1dzCcSFWYDoYJ4NZkwlFap'

address=raw_input("Enter the location whose top trend you want to know.\n")

# coo=coordinates(address)
# lati=coo[0]
# longi=coo[1]

auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
api = tweepy.API(auth)

trendslist=[]

# loc=api.trends_closest(lat=lati,long=longi)      #Returns the locations closest to the specified location
# place=loc[0]['name']
# woeid=loc[0]['woeid']                            #extracting the woeid of the first location

trends=api.trends_place(id=23424975)                #Returns the top 10 trending topics #united_kingdom_woeid = 23424975

for item in trends[0]['trends']:                 #trends is a list whose first element is of type dict
    trendslist.append(item['name'])

first_trend=trendslist[0]                       #top trend

if first_trend[0]=='#':
    first_trend=first_trend[1:]

file_name=str(address)+" "+str(first_trend)+".txt"

print("Top trending in "+str(address)+" is: "+str(first_trend))
print('')

print("Current tweets about "+str(first_trend)+" :\n")
print('')

class listener(StreamListener):
    def on_data(self,data):
        try:
            #user_name=data.split('"screen_name":"')[1].split('","location"')[0]
            text=data.split(',"text":"')[1].split('","source')[0]

            unformatted = j["created_at"]
            remove_ms = lambda x:re.sub("\+\d+\s","",x) # Use re to get rid of the milliseconds.
            mk_dt = lambda x:datetime.strptime(remove_ms(x), "%a %b %d %H:%M:%S %Y")# Make the string into a datetime object.
            my_form = lambda x:"{:%Y-%m-%d %H:%M:%S}".format(mk_dt(x))# Formatting datetime object.
            l = my_form(unformatted)

            print(str(l)+' tweeted: '+str(text))
            print('\n')
            #file_name=str(first_trend)+".txt"
            savefile=open(file_name,'a')
            savefile.write('@'+str(date)+' tweeted: '+str(text))
            savefile.write('\n')
            savefile.write('\n')
            savefile.close()
            return True
        except BaseException as e:
            print('failed '+ str(e))
            time.sleep(5)
    def on_error(self,status):
        print(status)

auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream=Stream(auth,listener())
twitterStream.filter(track=[first_trend])