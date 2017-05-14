# -*- coding: utf-8 -*-
# @Author: skandix
# @Date:   2016-08-07 20:27:48
# @Last Modified by:   skandix
# @Last Modified time: 2016-08-07 20:29:31
import datetime

def diffDateTime(start, stop):
	_Diffstart = datetime.datetime.strptime(start, "%H:%M:%S %d/%m/%Y")
	_Diffstop = datetime.datetime.strptime(stop, "%H:%M:%S %d/%m/%Y")
	diff = _Diffstop - _Diffstart
	return diff