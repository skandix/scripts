import socket
import logging
import time

count=0
now = time.strftime("%c")
logging.basicConfig(filename='inetconnectionStatus.log',level=logging.DEBUG,format='%(asctime)s %(message)s')
logging.info('Started Logging at %s \n' % now)

def is_connected():
  try:
    host = socket.gethostbyname("www.google.com")
    s = socket.create_connection((host, 80), 2)
    
    return True
  except:
     pass
  return False

def main():
  if is_connected() == True:
    logging.info('Connection is present at %s' % now)
    time.sleep(60)
    return "Sleeping 60"
    #return "YAY, internet!!!, i can go back to sleep", now


  elif is_connected() == False:
    logging.warning("Connection Wasn't present at %s" % now)
    time.sleep(30)
    return "Sleeping 30"
    #return "NOOOOO, INTERNET?!?! ", now

while True:
    print main()
