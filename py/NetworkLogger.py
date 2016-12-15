import socket
import logging
import time

logging.basicConfig(filename='inetconnectionStatus.log',level=logging.DEBUG,format='%(message)s %(asctime)s')
logging.info('-=Started Logging=- \n')

def is_connected():
  try:
    host = socket.gethostbyname("www.google.com")
    s = socket.create_connection((host, 80), 2)
    
    return True
  except:
     pass
  return False

def main(present, npresent):
  if is_connected():
    logging.info('Connection is present at ')
    time.sleep(present)

  else:
    logging.warning("Connection Wasn't present at ")
    time.sleep(npresent)

while True:
    main(60, 10)
