import pyping
import csv
import datetime
import argparse 
import time as tz

# USAGE
# python main.py --ip 10.0.0.43 --export datapor_internal

now = datetime.datetime.now()
time = "{}/{}/{}-{}:{}:{}".format(now.day, now.month, now.year, now.hour, now.minute, now.second)


def _ping(address, dump, irange=255):
    with open(dump+'.csv', 'w') as csvfile:
        felten = ['IP', 'state']
        write = csv.DictWriter(csvfile, fieldnames=felten)
        write.writeheader()
        tot = tz.time()
    
        for j in xrange(1, irange):
                start = tz.time()
                clean =  address.split(".")
                loot = "{}.{}.{}.{}".format(clean[0], clean[1], clean[2], j)
                ping = pyping.ping(loot, timeout=3, count=2)
    
                if ping.ret_code == 0:
                    write.writerow({'IP': loot, 'state':"Online"})
                    print ping.destination
            
                else:
                    pass
    
    print "Total",  tz.time() - tot,  "seconds"

parser = argparse.ArgumentParser()
parser.add_argument("--ip")
parser.add_argument("--export")
args = parser.parse_args()

_ping(args.ip, args.export)
