#!/bin/python
# -*- coding: utf-8 -*-
from datetime import timedelta

def get_latest_time():
	for i in open('/proc/uptime', 'r'):
		return i
		
def uptime(s=""):
        uptime = get_latest_time()
	
        Useconds = float(uptime.split()[0])
	Ustring = str(timedelta(seconds = Useconds))
	s += str('Uptime: {:}').format(Ustring)

	return s

print uptime()
