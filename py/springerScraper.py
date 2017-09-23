import re
import time
import shutil
import requests

searchTerm = '?facet-discipline=%22Computer+Science%22&facet-content-type=%22Book%22"'
baseDL = "https://link.springer.com/content/pdf/"
url = 'https://link.springer.com/search/?facet-discipline="Computer+Science"&facet-content-type="Book"'
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
		dl = baseDL+urls+".pdf"
		if dl not in dlUrl:
			dlUrl.append(dl)

def download():

	endUrl = url.split('/')[4]
	startUrl = 'https://link.springer.com/search/'
	fullRange = result(url)+1

	#gets all pdf links over the n range...
	for ith in range(1, 10):
		nUrl = "{0}page/{1}{2}".format(startUrl, ith, endUrl)
		getUrls(nUrl)

	for pdfLink in dlUrl:
		name = pdfLink.split('/')[-1]
		stream = getStream(pdfLink, strem=True)
		start = time.time()

		with open(name, 'wb') as file:
			shutil.copyfileobj(stream.raw, file)
		print "Downloaded: {0}\t Seconds: {1:4f}".format(name,(time.time()-start))


download()
