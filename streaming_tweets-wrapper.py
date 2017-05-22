# for timing + unique file-name functions, et c.
from time import sleep
from datetime import datetime

# To archive old version of streams
from shutil import copyfile

# put this in a different file

DIRerrormsg = datetime.now().strftime("%Y%m%d-%H%M%S") + ", problem writing new directory, " + logs_directory

# put this in a different file
# make sure logs_directory sends to Box sync'd directory

def set_logs_directory():
	logs_directory = './logs/' + datetime.now().strftime("%Y-%m%d") + '/'
	logs_start = datetime.now().strftime("%Y%m%d")
	if os.path.isdir(logs_directory) == True:
		pass
	else:
		try:
			os.mkdir(logs_directory)
		except:
			with open(errors, "w") as f:
				f.write(DIRerrormsg)
				f.close()
			quit()

def set_filename():
	tweetdata_filename = logs_directory + datetime.now().strftime("%Y%m%d-%H%M%S") + 'times-square-tweets.txt'
	return tweetdata_filename


# set logs directory

# set filename

# run streaming_tweets for 24 hours as a separate/forked process
# python streaming_tweets-streamer.py > tweetdata_filename

# if streaming_tweets throws a network error, wait, then restart
# if i/o error, pause

# interrupt streaming_tweets every 24 hours
# change directory name

while True:

	while int(logs_start) <= int(datetime.now().strftime("%Y%m%d")):
		sleep(3600) # sleep 1 hour

	set_logs_directory()

	filename = set_filename()

	command = "python streaming_tweets-streamer.py > " + filename + ""




