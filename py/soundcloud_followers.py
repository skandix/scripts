# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
from pprint import pprint
from urllib2 import urlopen
import requests
import json

cli_id = "<insert client id>"
artist = [ ]
uinfo = [ ]

def get_sc_uid(username):
	requid = requests.get('http://api.soundcloud.com/resolve.json?url=http://soundcloud.com/%s&client_id=%s' % (username, cli_id), stream=True)
	uid = requid.text.replace(',', '').replace('kind', '').replace('"', '')
	uinfo = uid.split(":")
	
	return uinfo[1]

def follower_scrape():
	url =  'https://api.soundcloud.com/users/%s/followings?client_id=%s&limit=1000' % (get_sc_uid("jonas_bengtson"), cli_id)
	#info = json.loads(urlopen(url).read())
	spoon = urllib.urlopen(url)
	soup = BeautifulSoup(spoon)
	for i in soup.findAll('a'):
			print spoon.get('href')

	#first_elem = info[0]
	pprint(soup)

follower_scrape()
