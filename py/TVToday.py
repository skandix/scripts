from time import ctime as creation
from shutil import copyfile
from time import strftime
from sys import exit

import argparse
import glob
import os

TV = "/mnt/TV"


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
	parser = argparse.ArgumentParser(prog='EditedToday.py', usage='%(prog)s [--path /mnt/TV] [--ext .mkv')
	parser.add_argument("--path", help='the path to the folder')
	parser.add_argument("--ext", help='extension to look for')
	args = parser.parse_args()

	if args.path and args.ext:
		for filePath in glob.glob("{0}*\*\*{1}".format(args.path, args.ext)):
			if today(formatFile(filePath)):
				print filePath.split('\\')[3]
			else:
				pass
	else:
		exit(127)
#only works on windows atm.. fixing linux later..kek
