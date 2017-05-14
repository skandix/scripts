#!/bin/python
# -*- coding: utf-8 -*-
import requests
import datetime
from config import api_key

sonarr_url = "http://localhost:8989/api"
gb = 1.0 * 10**(-9)

headers = {
    'x-api-key': api_key,
    'cache-control': "no-cache",
    }

def get_latest_json(endpoint):                                                           
    return requests.get(sonarr_url+endpoint, stream=True, headers=headers).json()

#find out what is wrong with this function ?!?!
def get_latest_cal(s):
	calendarJson = get_latest_json("/calendar/")
	for i in calendarJson:
		show = i['series']['title']
		snr  = i['seasonNumber']
		epnr = i['episodeNumber']
		airdt = i['airDate']
		hzfl = i['hasFile']
		s += str('{:s} S{:d}E{:d}, {:} Airing: {:}\n'.format(show, snr, epnr, hzfl, airdt))
		print i
	print s
	return s

"""def post_latest_cal(s):
	getcalendarJson = get_latest_json("/calendar/")

	for i in getcalendarJson:
		if i['hasFile'] == True:
			loot = "Today's Loot\n"
			show = i['series']['title']
			snr  = i['seasonNumber']
			epnr = i['episodeNumber']
			s += str('{:s} S{:d}E{:d}\n'.format(show, snr, epnr))
	#print loot + s
	return loot + s"""

def get_latest_diskspace(s):
	diskspaceJson = get_latest_json("/diskspace/")

	for i in diskspaceJson:
		path = i['path']
		totSpace = i['totalSpace']
		freeSpace = i['freeSpace']
		s +=  str('{:s} Total: {:.2f} GB Free: {:.2f} GB\n'.format(path, totSpace*gb, freeSpace*gb))
	
	print s
	return s

