#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib2 import urlopen
from pprint import pprint
import cPickle as pickle
import jsonpickle
import requests
import urllib
import json
import re

cli_id = "02gUJC0hH2ct1EGOcYXQIzRFU91c72Ea"
artist = [ ]

def get_sc_uid(username):
	requid = requests.get('http://api.soundcloud.com/resolve.json?url=http://soundcloud.com/%s&client_id=%s' % (username, cli_id), stream=True)
	uid = requid.text.replace(',', '').replace('kind', '').replace('"', '')
	uinfo = uid.split(":")
	
	return uinfo[1]

def follower_scrape():
	url =  'https://api.soundcloud.com/users/%s/followings?client_id=%s&limit=1000' % (get_sc_uid("aulonmujaj"), cli_id)
	spoon = urllib.urlopen(url)
	soup = BeautifulSoup((spoon), 'html.parser')

	frozen = jsonpickle.encode(soup)

	find_username = re.compile(ur'"username\\":\\"[a-zA-Z0-9 ]{3,}')
	regex_magic = re.findall(find_username, frozen)
	
	for i in regex_magic:
		artist.append(i.replace('"', "").replace('username', "").replace('\:', "").replace('\\', ""))
	return artist

def soundscrape_generate():

	for i in follower_scrape():
		pickle.dumps("soundscrape -f " + i, open("soundcloud_scrape.sh", "wb"))

print follower_scrape()
# if you want to generate a bash script to download songs from all the artist you are following
soundscrape_generate()
