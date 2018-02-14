# -*- coding: utf-8 -*-
# pip install isbnlib requests
import re
import os
import time
import shutil
import isbnlib 
import requests

baseDL = "https://link.springer.com/content/pdf/"
#url = 'https://link.springer.com/search/?facet-discipline="Computer+Science"&facet-content-type="Book"'
url = 'https://link.springer.com/search?facet-discipline=%22Computer+Science%22&facet-content-type=%22Book%22&query=security'
dlUrl = []

# gets link data
def getStream(url, strem=False):
		return requests.get(url, stream=strem)

def result(url, elementsPerPage=20):
	source = getStream(url).text
		
	resultLoot = str(re.findall(re.compile(ur'<strong>[\d,]+</strong>'), source)[0]).split('>')
	result = float(resultLoot[1].replace('</strong','').replace(',',''))/elementsPerPage
	
	if "." in str(result):
		pages = int(str(result).split('.')[0]) + 1
	else:
		pages = result 
	
	return pages

def getUrls(url):
	source = getStream(url).text

	loot = re.findall(re.compile(ur'href=\"/book/([\d./-]+)\"'),source)
	for urls in loot:
		dl = baseDL+urls
		if dl not in dlUrl:
			dlUrl.append(dl)

def getBookTitle(isbn):
	isbn = isbn.replace('-','')
	book = isbnlib.meta(isbn)
	return book['Title']

def indexingLinks(pages):
	try:
		endUrl = url.split('/')[4]
	except IndexError as e:
		endUrl = url.split('/')[3]
	startUrl = 'https://link.springer.com/search/'
	# you don't want to use this, this will rip the whole search term result
	#fullRange = result(url)+1

	for ith in range(1, pages):
		nUrl = "{0}page/{1}{2}".format(startUrl, ith, endUrl)
		getUrls(nUrl)
	return "\nFound\n{} Books \nOn {} pages".format(len(dlUrl), ith)

def download():

	for pdfLink in dlUrl:
		try:
			print pdfLink
			dirtyName = getBookTitle(pdfLink.split('/')[-1])+".pdf"
			name = re.sub(r'([,/\\&!\"#%&/()=? ])', '',dirtyName)
			if name is ".pdf":
				print "found invalid isbn"
				break

		except TypeError as e:
			continue

		stream = getStream(pdfLink, strem=True)
		start = time.time()

		try:
			with open(name, 'wb') as file:
				shutil.copyfileobj(stream.raw, file)
			print "Downloaded: {0}\t\t Seconds: {1:4f}".format(name,(time.time()-start))
		except UnicodeEncodeError as e:
			#fixing this later
			print "this is triggering an error\n",name

if __name__ == '__main__':
	try:
		print indexingLinks(10)
		download()
	
	except KeyboardInterrupt as e:
		print "Detected CTRL+C\n ABORTING MISSION!"
		print len(dlUrl)
