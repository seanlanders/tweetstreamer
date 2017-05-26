import os, sys, subprocess

from datetime import datetime
from time import sleep

import streaming_tweets-streamer
from streaming_tweets-streamer import Streamer

cwd = os.getcwd()
cwdlist = os.listdir(cwd)
oldout = sys.sysout()

#make logs directory, if not already existing
if 'logs' in cwdlist:
	if os.path.isdir('logs') == 'True':
		pass
else:
	os.mkdir('logs')
	logsdir = 'logs'
	cwdlist = os.listdir(cwd)

#main loop

while True:
	startdate = datetime.now().strftime("%Y%m%d")
	starttime = datetime.now().strftime("%H%M%S")
	logname = startdate + starttime + '-times-square.txt'
	logsdir = logsdir + "/" + startdate + "/" + starttime + "/"
	#Make appropriate log directories, if not already existing
	if os.path.isdir(logsdir) == True:
		pass
	else:	
		os.mkdir(logsdir)
