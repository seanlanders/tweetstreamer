# based on code from http://adilmoujahid.com/posts/2014/07/twitter-analytics/

# Run from commandline, 'python streaming_tweets.py > location\of\file\<name of textfile to store data>'

# import necessary tweepy modules 
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# for timing + unique file-name functions, et c.
from time import sleep
from datetime import datetime

# To archive old version of streams
"""from shutil import copyfile
original_file = './logs/times-square-tweets.txt'
archive_file = './logs/working/working-text' +  '.txt'
ascii_file = './logs/working/working-text-ascii.txt'
"""


# set credentials
# put in your own
#consumer_key = ""
#consumer_secret = ""
#access_token = ""
#access_secret = ""


# define class 

# replace StdOutListener
## rather than write to stdout, write to   
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    while True:
        StartDate=datetime.now().strftime("%Y%m%d")
        StartTime=datetime.now().strftime("%H%M%S")
        

        while StartDate !=    
            #This handles Twitter authetification and the connection to Twitter Streaming API
            l = StdOutListener()
            auth = OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_secret)
            stream = Stream(auth, l)

            #This line filter Twitter Streams to capture data by location: Times Square
            # locations are listed by bounding box - comma separated pair of long/lat pairs
            #  ex: (locations = ['southernmost, westernmost, northernmost, easternmost'])
            # other possible options include 'track' (keywords), 'follow' (userIDs)
            # other switches include 'delimited', and 'stall_warnings'
            #
        	# track & follow should be strings, locations are floats
        	#
            # each option is non-exclusive -- ie, track=['twitter'], locations=['-73.988,40.7546']
            # will retrieve tweets that use 'twitter' (even non-geo) AND/OR tweets from Manhattan
            try:
                stream.filter(locations=[-73.9881430231,40.7546392928,-73.9792344316,40.7629627669])
            except:
                continue
