from os import listdir, getcwd, mkdir, rename
import re

dldir = getcwd()+'\\'
dirs = []

def getCourseName():
	for k in listdir(dldir):
		if k.endswith('.mp4'):
			return (re.findall(re.compile('(-[a-z-]+)m[1-9]'),k)[0])
		else:
			for k in listdir(dldir):
				return (re.findall(re.compile('(-[a-z-]+)'),k)[0])

def sortAndMove():
	for k in listdir(getcwd()):
		loot = (re.compile('(m\d)|(\d+).mp4').split(k))[5:6]
		for k in loot:
			if k not in dirs:
				dirs.append(k)
			elif k in dirs:
				pass

	try:
		for k in (sorted(dirs)):
			mkdir(dldir+k)
	except FileExistsError:
		print("folders already exists, moving files\n")

	for listing in listdir(getcwd()):
		for k in dirs:
			if k in listing and listing.endswith('mp4'):
				try: 			
					rename(dldir+listing, dldir+k+"\\"+listing)
				except FileExistsError:
					break
			else:
				pass

def moveSortedToCourseFolder():
	for k in listdir(dldir):
		for j in (re.findall(re.compile('(\d{2})'),k)):
			rename(dldir+j, dldir+getCourseName()+"\\"+j)

if __name__ == '__main__':
	mkdir(getCourseName())
	print(getCourseName())
	sortAndMove()
	moveSortedToCourseFolder()


