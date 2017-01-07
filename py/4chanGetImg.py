# -*- coding: utf-8 -*-
import requests
import re
import wget
import time
import argparse
import os

resp = requests.get
foundImg = []
debugging = True

def motd():

	print " _  _     ___ _                 "
	print "| || |   / __\ |__   __ _ _ __  "
	print "| || |_ / /  | '_ \ / _` | '_ \ "
	print "|__   _/ /___| | | | (_| | | | |"
	print "   |_| \____/|_| |_|\__,_|_| |_|"
	print "                                "
	print " REGEX GETimg DOWNLOADER \n"

def getImgz(url):
        urlID = url[33:]

	black_magic = re.compile(ur'<img[^s]\w+\S+[.png|.jpg|.jpeg]')
        lol = resp(url).text

	loot = re.findall(black_magic, lol)
        
        if not os.path.exists(urlID) or os.path.exists("../"+urlID):
            try:
                os.mkdir(urlID)
            except OSError as oserr_mkdir:
                if debugging:
                    print ("OS Error: {0}".format(oserr_mkdir))
            else:   
                os.chdir(urlID)


        elif os.path.exists(urlID):
            os.chdir(urlID)
            print "dir changes"
           
#        try:
        for j in os.listdir("../"+urlID):
            foundImg.append(j)
#        except OSError as oserr:
#            if debugging:
#                print ("OSError: {0}".format(oserr))

	for i in loot:
        	clean = str(i.replace('<img src="//', '').replace("s", ""))

		if clean.count("unknown"):                
                    print ("bad img, not downloading")

                else:
                    try:
                        foundImg.index(clean[13:])
                    except ValueError as valueerr:
                        if debugging:
                            print("Value Error: {0}".format(valueerr))   
                        print (wget.download("http://"+clean))
                    else:
                        print ("Skipping")
        if debugging:            
        	print len(clean)


parser = argparse.ArgumentParser()
parser.add_argument("--url")
args = parser.parse_args()


# Takes inn url as --url <insert u
motd()
while resp(args.url).status_code != 404:
    getImgz(args.url)

print ("Thread is Dead, RIP {0}".format(args.url))

