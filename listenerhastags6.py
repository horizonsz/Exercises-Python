import json
import pandas as pd

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "197481156-OufHbI2EdEp32mF9rQGCftl9pcFbiWrmKWyWGEAe"
access_token_secret = "MXjqQaUCGXtwFZImYh4JYaPUPORGIkM6FUVxRHah5VCYw"
consumer_key = "O82viv9gqRgStE2FKzPswFDH0"
consumer_secret = "wr78xh1jgVB01k7yJTY14yPuzfyo8QDXr4IKEBes8BdiSWnbcl"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        return True
        return data

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    datos = stream.filter(track=['#ea5'])

    print datos








