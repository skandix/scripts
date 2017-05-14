# -*- coding: utf-8 -*-
from sys import platform as _os
import os

def clearTerm():
    # linux or cygwin or the pro mac book pro pro
	if _os == "linux" or _os == "linux2" or _os == "cygwin" or _os =="darwin":
		os.system('clear')

    # Windows...
	elif _os == "win32":
		os.system('cls')
