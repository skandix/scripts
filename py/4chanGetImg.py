# -*- coding: utf-8 -*-
import urllib2
import re
import wget
import time
import argparse

def motd():

	print " _  _     ___ _                 "
	print "| || |   / __\ |__   __ _ _ __  "
	print "| || |_ / /  | '_ \ / _` | '_ \ "
	print "|__   _/ /___| | | | (_| | | | |"
	print "   |_| \____/|_| |_|\__,_|_| |_|"
	print "                                "
	print " REGEX GETimg DOWNLOADER \n"

def getImgz(url):
	motd()
	black_magic = re.compile(ur'<img[^s]\w+\S+[.png|.jpg|.jpeg]')
	lol = urllib2.urlopen(url)
	fagz = lol.read()

	loot = re.findall(black_magic, fagz)

	for i in loot:
		#just replace shit, with nothing, if you don't replace the s, you'll only get thumbnails
		clean = str(i.replace('<img src="//', '').replace("s", ""))
		print wget.download("http://"+clean)
	print len(clean)


parser = argparse.ArgumentParser()
parser.add_argument("--url")
args = parser.parse_args()


# Takes inn url as --url <insert url>
getImgz(args.url)
