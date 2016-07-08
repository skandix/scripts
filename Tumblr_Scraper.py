# Scrapes for all img urls and downloads them
# How To Use It
# python main --username tumblr_username

import re
import requests
import argparse
import sys
import wget

debug = True 

def profile(username):
    return "http://"+username+ ".tumblr.com"

def pageRotation(username):

    for n in xrange(1,200):
        page_n="/page/"+str(n)

        compiled = profile(username) + page_n
        string = requests.get(compiled).text
        p = re.compile(ur'<\w{3}\ssrc\S+')
        loot = re.findall(p, string)
        
        for j in loot:

            if len(loot) <= 3:
                sys.exit(0)
                print "There was no more pages to scrape from"

            else:
                clean = str(j.replace('<img src="','').replace('"', ''))
                print wget.download(clean)


        if debug:
            print "Loot Len:", len(loot)
            print "pagenr: ", page_n

parser = argparse.ArgumentParser()
parser.add_argument("--username")
args = parser.parse_args()

pageRotation(args.username)
