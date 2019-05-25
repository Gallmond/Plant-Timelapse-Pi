# /home/pi/plantwatcher/delete_img.py
import os, datetime

# how many days a file is allowed to live
DaysToLive = 4
abspath = os.path.abspath(__file__) # absolute file path
parentPath = abspath[0:abspath.rfind("/")]
image_path = parentPath+"/img"

# array of files in dir
filesList = os.listdir(image_path) # like ['20180415T131312.jpg', 'recent.jpg']

# for each file
for fileName in filesList:
	try:
		fileDate = datetime.datetime.strptime(fileName, '%Y%m%dT%H%M%S.jpg').date()
		fileDate = datetime.datetime.combine(fileDate, datetime.datetime.min.time())
		nowDate = datetime.datetime.now()
		twoDays = datetime.timedelta(days=DaysToLive)
		twoDaysAgoDate = nowDate - twoDays
		print("checking if "+str(fileName)+" ("+str(fileDate)+") is older than "+str(twoDaysAgoDate)+"\n")
		if fileDate < twoDaysAgoDate:
			print("removing "+str(fileName)+"\n")
			os.remove(image_path+"/"+fileName)
	except ValueError:
		print("fileDate could not be parsed for "+str(fileName)+"\n")
		continue