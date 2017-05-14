#!/bin/python
# -*- coding: utf-8 -*-
import requests
import datetime

v = ""
k = ""
def get_latest_json(endpoint):                                                           
    return requests.get(plexpy_url+plexpy_apikey+endpoint, stream=True).json()


def return_latest_plays(s):
	playsJson = get_latest_json("&cmd=get_plays_by_top_10_users")

	#for i in playsJson['response']['data']['series'][:5]:
		#for j in i['data'][:5]:
			#if j != 0:
				#print j
	
	for v in playsJson['response']['data']['categories']:
		print v	
		
	for k in xrange(len(playsJson['response']['data']['categories'])):
		print k

#return_latest_plays("")

### Work in progress, will fix later when i have the time and the amounts of coffee for it
