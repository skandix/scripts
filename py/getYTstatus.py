#this is used to see if a video is avaliable, since it migth show a 200ok even though the video isn't playable.
# therefor i wrote this to check the source code for a submessage saying it's not avaliable.. then it's not ok :)

import requests
import re

def getYTstatus(url): 
        
	regexp = re.compile(ur'"submessage">[\n]\S+[a-zA-Z .]+')
	loot = re.findall(regexp, requests.get(url).text)
	if loot:
		return True
	else:
		return False


# uncomment to see that it works when something aren't avaliable, and when they are
# video not avaliable!
#print getYTstatus("https://www.youtube.com/watch?v=hopYXDBQIso")

# video avaliable
#print getYTstatus("https://www.youtube.com/watch?v=NCjgXQ6IGOU")
