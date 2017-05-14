#!/bin/python
# -*- coding: utf-8 -*-

import requests
import datetime

cp_url = ""
cp_apikey = ""

def get_latest_json(endpoint):                                                           
    return requests.get(cp_url+cp_apikey+endpoint, stream=True).json()           

def return_media_list(s):
	medialsJson = get_latest_json("/media.list/")

	for i in medialsJson:
		
##############################################################
## SHIT DON'T WORK, DON'T BLAME ME FOR BEING LAZY OKAY?!?!? ##
##############################################################
