# based on code from http://adilmoujahid.com/posts/2014/07/twitter-analytics/

# Run from commandline, 'python streaming_tweets.py > location\of\file\<name of textfile to store data>'

# import necessary tweepy modules 
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream




# set credentials
consumer_key = "jJeGn5IMYMGAPTl8ZO2JsWrcU"
consumer_secret = "ZE1ESyQOQ9kFJ8SXv4aGB6pA6Y4gtFX8f3cGpCYT9tlEdVm5Ah"
access_token = "866763740506722304-ynGexPZLbyXHnwhTPF1zqNQp1sJ4rrZ"
access_secret = "lgU9YSsMwR1S3svM0kyfvMm9WpOgzXkkzoyRxjKoJU7Qt"


# define class 

# replace StdOutListener
## rather than write to stdout, write to   
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

def stream-tweets():
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