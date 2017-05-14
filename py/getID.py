# -*- coding: utf-8 -*-
# this module is used to scrape ids from youtube playlists.... 
import re
import requests

onlyid = []
onetime = []

def getHTML(url):
        return requests.get(url).text

def getID(url, s=""):
	regex = re.compile(r'\/watch.[v=]+[^+]{11}')
	loot = re.findall(regex, getHTML(url))
	
        for i in loot:
		clean = i.replace('/watch?v=', '')
		onlyid.append(clean)
		s += str([x for x in onlyid if onlyid.count(x)==1]).replace("[]", '').replace('/watch_videoshelf":', '').replace("['']", '').replace("&", "")[2:-1]

	count = 0
	v = ""
        for j in s:
                count += 1
                v += str(j).replace("'", "").replace("'", "")
                if count == 13:
			onetime.append(v)
			count = 0
			v = ""

	return onetime

