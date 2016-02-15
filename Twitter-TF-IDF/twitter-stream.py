from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import json

#Variables that contains the user credentials to access Twitter API
access_token = "563806852-TgZSJkG413GrZ2g0TzRsyGh7lUAluLmrsKTCnKNs"
access_token_secret = "hqwb3QFb82LKXR10RAAbfEg8HBUMBQMsY8roZ9KySyar5"
consumer_key = "Tq20eDbLhvBBGgK2jXcp8Faif"
consumer_secret = "flSsRrcAJQCwgfbpnHbcPBy5bN9YexArVB5pYdHtdC25dbipO6"


#This is a basic listener that just stores received tweets to database.
class StdOutListener(StreamListener):

    def __init__(self, companies):
        self.startTime = time.time()
        self.totalTime = 1800
        self.companies = companies

    def findCompany(self, text):
        comp = []
        for company in self.companies:
            if company in text:
                comp.append(company)
        return comp

    def on_data(self, data):
        if time.time() - self.startTime <= self.totalTime:
            decoded = json.loads(data)

            try:
                if decoded['lang'] == 'en':
                    text = decoded['text'].lower().encode('ascii', 'ignore').decode('ascii')
                    companies = self.findCompany(text)

                    if len(companies) > 0 and len(text) > 0:
                        for company in companies:
                            print "Company: " + company
                            with open("/Company-Tweets/" + company + "_tweets.txt", 'a') as f:
                                f.write(text + '\n')
            except:
                pass
        else:
            twitterStream.disconnect()

    def on_error(self, status):
        print status

if __name__ == '__main__':
    companyList = ["twitter", "google", "apple", "facebook", "amazon"]
    l = StdOutListener(companyList)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitterStream = Stream(auth, l)

    twitterStream.filter(track=companyList)
