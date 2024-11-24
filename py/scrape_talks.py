import requests
import json
import re

def getData(url:str):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
	return requests.get(url, headers=headers).text

soure_site = getData("https://www.p99conf.io")
complete_list = {}

loot = re.findall('a href\=\"([\S]+)\"', soure_site)
talks = [session for session in loot if "session" in session]
talks = set(talks)

for talk in talks:
	src = getData(talk)
	name = (talk.split('/')[4])
	loot = "".join(re.findall('(watch.[v=]+[^+]{11})', src))
	loot = (f"https://youtube.com/{loot}")
	loot = f"- [{name}]({loot})q"
	print (loot)
