import praw
from pushbullet import Pushbullet
import re
import time

pb = Pushbullet("")
regexp = re.compile(ur'.[\[O]][a-zA-Z0-9 .]{3,}')
r = praw.Reddit(user_agent='PBUSNTINVNOTIF')
submissions = r.get_subreddit('UsenetInvites').get_new(limit=1)

def main(zTime=1):
	foo = [str(x) for x in submissions]
	loot = re.findall(regexp, str(foo))
	for i in loot:
		if loot != None:
			print i
			print "Pushing To Pushbullet \n"
			pb.push_note("NEW INVITE FETCHED!", i)
			main()
			
	if len(loot) == 0:
		print ("No Invites Found :(\n Checking Back in 30min")
		time.sleep(zTime*60)
		main()

main()
