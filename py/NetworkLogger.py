import socket
import logging
import time

now = time.strftime("%c")
logging.basicConfig(filename='inetconnectionStatus.log',level=logging.DEBUG)

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
    logging.info(now)
    logging.info('\n')
    return "YAY, internet!!!, i can go back to sleep", now
    time.sleep(1)

  elif is_connected() == False:
    logging.warning("Connection Wasn't present at %s" % now)
    logging.info(now)
    logging.info('\n')
    return "NOOOOO, INTERNET?!?! ", now
    time.sleep(1)

while 1:
  print main()
