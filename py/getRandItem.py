import random

#tests
#text = ['hai', 'paa','daig','maan','hvordan','gaar', 'det']
#fib = [1,2,3,5,8,13]

def getRandItem(targetList):
	return targetList[random.randint(0, len(targetList)-1)] #-1 so it never goes out of range.

#print getRandItem(text)
