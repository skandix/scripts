# Work in progress, does not quite work as i had hoped yet.. will work on it later
import requests
import logging 
import shutil
import sys
import re

# fcuking encoding shit
reload(sys)
sys.setdefaultencoding('utf-8')

foundLinks = []

response = requests.get('http://paste.debian.net/')

patt = re.compile(ur'\S{2}paste.debian.net\/\d+')
loot = re.findall(patt, response.text)

#while response.status_code != 404:
for links in loot:
	clean = links.replace('//','')
	foundLinks.append(clean)
#print foundLinks

for Flinks in foundLinks:
	urlID = Flinks[17:]
	print urlID
	with open(urlID+".txt", 'wb') as textValve:
		stream = requests.get(u'http://'+Flinks, stream=True)

	if not stream.ok():
		print "shit fucked up"
		sys.exit(1)

	for block in response.ither_content(1024):
		textValve.write(blcok)
		


	print ("downloaded {0}").format(stream)
