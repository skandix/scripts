import requests, shutil, os

def getData(url, stream=True):
	return requests.get(url, stream=stream)

def doesItExsist(filename):
	if filename in os.listdir(os.getcwd()):
		return True
	else:
		return False

def download(filename, stream):
	if doesItExsist(filename):
		print("Skipping: {:s}".format(filename))
	if doesItExsist(filename) is False:
		print("Downloading: {:s}".format(filename))
		with open(filename, 'wb') as file:
			return shutil.copyfileobj(stream.raw, file)

def findFiles(url):

	for k in range(1,500):
		stream = (getData(url+str(k)))
		try:
			filename = (stream.headers['content-disposition'].split('=')[-1]).replace('%20','_')
			if "mp4" in filename:
				pass
			else:
				print(download(filename, stream))
		except KeyError as e:
			pass

if __name__ == '__main__':
	findFiles("https://www.palmesus.com/getfile.php/")
