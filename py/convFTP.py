# just generate the link so you can stream files from ftp server to desired player
# -*- coding: utf-8 -*-
import argparse
import os

def makeFTPstream(username, pw, url):
	c = url.replace("ftp://", "")
	compiledftp = "ftp://"+username+":"+pw+"@"+c
	return compiledftp

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--url")
	args = parser.parse_args()
	clean = makeFTPstream("uname", "passwd", args.url)

	os.system("vlc" + clean)
