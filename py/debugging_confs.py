#simple script to run to check site for codes and see headers when making changes to configs in ngnix
import requests
import time

g = requests.get("https://datapor.no/")

def test(deep, deeper):
	while True:
		if g.status_code == 404:
			print "Route 404, Is Found :("
			print g.headers,
			time.sleep(deep)
			print "\n"

		elif g.status_code == 200:
			print "WE GOT A HEARTBEAT!!!"
			print g.text
			print g.headers
			time.sleep(deep)
			print "\n"

		else:
			print "don't know what happend"
			print g.status_code
			print g.text
			print g.headers
			print "\n"
			time.sleep(deeper)

			g.text

test(5, 15)
