# Lambda Lambda Lambda
from fake_useragent import UserAgent
from datetime import datetime
import argparse
import requests
import shutil
import os
import re

session = requests.Session()
ua = UserAgent()

parser = argparse.ArgumentParser()
parser.add_argument("--board", "-b", type=str, help="")
parser.add_argument("--path", "-p", type=str, help="Set a specific path to download to")
parser.add_argument("--type", "-t", type=str, help="set a specific type to download (img, text or links)")
parser.add_argument("--ext", "-e", type=str, help="download a specific image extension, only works for img type downloads")
parser.add_argument("--search", "-s", type=str, help="search for a specific board [EXPERIMENTAL]")
parser.add_argument("--debug", "-d", type=bool, help="will print thread ID for debugging purposes")
args = parser.parse_args()

#=====================#
the_choose_one = args.board
storagePath = args.path
searchType = args.type
img_ext = args.ext
searchTerm = args.search
debug = args.debug
#=====================#

def getData(webPath, thread_id=""):
    session.headers.update({'User-Agent': ua.random})
    if webPath is "thread":
        return session.get("https://boards.4chan.org/{0}/thread/{1}".format(the_choose_one, thread_id)).text
    elif webPath is "board":
        return session.get("https://boards.4chan.org/{0}/catalog".format(the_choose_one)).text

def boardTitle(loot):
    pattern = re.compile(u'<title>[^s]([\S ]+)<\/title>')
    return re.findall(pattern, loot)[0]

def fileName(searchType,ext):
    if storagePath is None:
        i = datetime.now()
        return ("{:s}//{:s}_{:s}_{:d}-{:d}-{:d}_{:d}-{:d}-{:d}.{:s}".format(os.getcwd(), searchType, the_choose_one, i.day, i.month, i.year, i.hour, i.minute, i.second, str(ext)))
    elif storagePath:
        i = datetime.now()
        return ("{:s}/{:s}_{:s}_{:d}-{:d}-{:d}_{:d}-{:d}-{:d}.{:s}".format(storagePath, searchType, the_choose_one, i.day, i.month, i.year, i.hour, i.minute, i.second, str(ext)))

def findText(loot):
    pattern = re.compile(
        u'class=\"quotelink\"\S+<br>([\w ?:(<br>|&#;)/.,]+)</blockquote>')
    return re.findall(pattern, loot)

def find(loot, type):
    if type == 'text':
        pattern = re.compile(u'class=\"quotelink\"\S+<br>([\w ?:(<br>|&#;)/.,]+)</blockquote>')
        return re.findall(pattern, loot)
    elif type == 'img':
        pattern = re.compile(u'File: <a href=\"\/[^s](\S+)\"')
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

def download(url, name):
    url = "https://"+url
    stream = (session.get(url, stream=True))
    with open(name, 'wb+') as file:
        shutil.copyfileobj(stream.raw, file)
        print("Downloaded: ",name)

def findBoards():
    pattern = (u',\"(\d{6,})\":{\"date\"')
    return (re.findall(pattern, getData("board")))

def convertApostrof(loot):
    pattern = re.compile(u'(&#039;)')
    return re.sub(pattern, "'", loot)

def dupeCheck(foldername):    
    for dir in os.walk(foldername):
        for files in dir:
            return (files)

def direktorat(name):

    if os.path.isdir(name):
        os.chdir(name)
    else:
        os.mkdir(name)
        os.chdir(name)

if __name__ == '__main__':
    if searchType == "img":
        direktorat(the_choose_one)
        if searchTerm:
            for threadid in (findBoards()):
                if debug:   
                    print("ThreadID", threadid)
                    
                if re.search(searchTerm,boardTitle(getData("thread", threadid)),flags=re.I):
                    print(boardTitle(getData("thread", threadid)))
                    board_name = boardTitle(getData("thread", threadid))
                    direktorat(board_name.split('-')[1].replace('/', '').replace('\\', ''))
                    

                    for k in (find(getData("thread", threadid), "img")):
                        file_extension = k.split('.')[-1]
                        file_name = (k.split('/')[-1])
                        board_name = boardTitle(getData("thread", threadid))
                        download(k, file_name)
                    os.chdir('..') #hackz
        else:
            for threadid in (findBoards()):
                if debug:   
                    print("ThreadID", threadid)
                else:
                    pass
        
                for k in (find(getData("thread", threadid), "img")):
                    file_extension = k.split('.')[-1]
                    file_name = (k.split('/')[-1])
                    board_name = boardTitle(getData("thread", threadid))
                    if img_ext:
                        if file_extension == img_ext:
                            download(k, file_name)
                        else:
                            pass                   

                    else:
                        download(k, file_name)

    if searchType == "text":
        name = fileName(searchType,"txt")
        for threadid in (findBoards()):
            if debug:   
                print("ThreadID", threadid)
            else:
                pass
            for k in (find(getData("thread", threadid), "text")):
                board_name = boardTitle(getData("thread", threadid))
                print(board_name)
                try:
                    open(name, 'a').write(Links(convertApostrof(sanitizeText(k))+("\n"),"del"))
                except UnicodeEncodeError as e:
                    pass

    if searchType == "links":
        name = fileName(searchType,"txt")
        print (name)
        for threadid in (findBoards()):
            if debug:   
                print("ThreadID", threadid)
            else:
                pass
            for k in (find(getData("thread", threadid), "text")):
                if (Links(convertApostrof(sanitizeText(k)) + ("\n"), "find")) is None:
                    pass
                else:
                    open(name, 'a').write(Links(convertApostrof(sanitizeText(k)), "find") + ("\n"))
