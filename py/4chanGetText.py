from fake_useragent import UserAgent
from datetime import datetime
from os import getcwd
import argparse
import requests
import re

session = requests.Session()
ua = UserAgent()

parser = argparse.ArgumentParser()
parser.add_argument("--board")
parser.add_argument("--path")
args = parser.parse_args()

#=====================#
the_choose_one = args.board
storagePath = args.path
searchType = "text"
#=====================#

def getData(webPath, thread_id=""):
    session.headers.update({'User-Agent': ua.random})
    if webPath is "thread":
        return session.get("https://boards.4chan.org/{0}/thread/{1}".format(the_choose_one, thread_id)).text
    elif webPath is "board":
        return session.get("https://boards.4chan.org/{0}/catalog".format(the_choose_one)).text

def fileName(searchType,ext):
    if storagePath is None:
        i = datetime.now()
        return ("{:s}//{:s}_{:s}_{:d}-{:d}-{:d}_{:d}-{:d}-{:d}.{:s}".format(getcwd(), searchType, the_choose_one, i.day, i.month, i.year, i.hour, i.minute, i.second, str(ext)))
    elif storagePath:
        i = datetime.now()
        return ("{:s}/{:s}_{:s}_{:d}-{:d}-{:d}_{:d}-{:d}-{:d}.{:s}".format(storagePath, searchType, the_choose_one, i.day, i.month, i.year, i.hour, i.minute, i.second, str(ext)))
        

def findText(loot):
    pattern = re.compile(
        u'class=\"quotelink\"\S+<br>([\w ?:(<br>|&#;)/.,]+)</blockquote>')
    return re.findall(pattern, loot)

def sanitizeText(loot):
    pattern = re.compile(
        u'(</blockquote|</div|>|<div class|<span class|<a href|<hr|<br|<wbr|&lt;3|&quot;|&gt;)')
    return re.sub(pattern, '', loot)

def Links(loot, action):
    if action is "del":
        pattern = re.compile(u'(https?|ftp|http)://[^\s/$.?#].[^\s]*')
        return re.sub(pattern, '', loot)
    
    elif action is "find":
        pattern = re.compile(u'((https?|http?|ftp)://[^\s/$.?#].[^\s]*)')
        match = re.search(pattern, loot)
        if match:
            return (match).group(0)
        else:
            pass

def findBoards():
    pattern = (u',\"(\d{6,})\":{\"date\"')
    return (re.findall(pattern, getData("board")))

def convertApostrof(loot):
    pattern = re.compile(u'(&#039;)')
    return re.sub(pattern, "'", loot)

if __name__ == '__main__':
    name = fileName(searchType,"txt")
    print (name)
    for threadid in (findBoards()):
        print(threadid)
        for k in (findText(getData("thread", threadid))):
            try:
                if searchType is "text":
                    open(name, 'a').write(Links(convertApostrof(sanitizeText(k))+("\n"),"del"))
                elif searchType is "links":
                    if (Links(convertApostrof(sanitizeText(k)) + ("\n"), "find")) is None:
                        pass
                    else:
                        open(name, 'a').write(Links(convertApostrof(sanitizeText(k)), "find") + ("\n"))
            except UnicodeEncodeError as e:
                pass
