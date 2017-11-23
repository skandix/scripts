from time import ctime as creation
from shutil import copyfile
from time import strftime
from sys import exit

import platform
#import argparse
import glob
import os

TV = "Y:\\"
EXT = ".mkv"

def today(date):
	# checking the todays date with the given files date
	if date in strftime("%a %b %d %Y"):
		return True
	else:
		return False

def formatFile(path):
	# formating the passed in file path to give out a formated time format
	date = ' '.join(creation(os.path.getctime(path)).split(' ')[:3])
	year = ''.join(creation(os.path.getctime(path)).split(' ')[-1])
	return ("{0:s} {1:s}".format(date, year))

if __name__ == '__main__':
	if platform.system() in "Windows":
		for filePath in glob.glob("{0}*\*\*{1}".format(TV, EXT)):
			if today(formatFile(filePath)):
				print filePath.split('\\')[3]
			else:
				pass		

	elif platform.system() in "Linux":
		for filePath in glob.glob("{0}*/*/*{1}".format(TV, EXT)):
			if today(formatFile(filePath)):
				print filePath.split('/')[4]
			else:
				pass
