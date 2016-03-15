from urllib2 import urlopen
from pushbullet import PushBullet
import json
#import pickle

ips = []
url = 'http://api.hostip.info/get_json.php'
info = json.loads(urlopen(url).read())

def pushbullet_init(ip):
	#init pushbullet with api_key
	#and alias for sending notes/alarms
	pb = PushBullet(api_key)
	note = pb.push_note("PUSH EXT IP",ip)

def getIP():

	ip = info['ip']
	return "IP:", ip

def getCity():

	city = info['city']
	return "City:", city.decode('utf8')

def getCountry():

	country = info['country_name']
	return "Country:", country

def lastLoggedIp():
	ips.append(getIP)
	return ips

def main():
	print getIP()
	print getCity() 
	print getCountry()

	#pushbullet_init(getIP)
	#if getIP =! lastLoggedIp
		#push the new ip to pushbullet...
		#then just go back to the while loop where is queries the ip and saves it to a logfile.
		#and the when the last row in the files is diffrent from the one that just is queryed from getIP
		#push it.

main()