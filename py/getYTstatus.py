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
