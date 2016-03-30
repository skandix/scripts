#!/bin/python
import random
import hashlib

def RandomPinCode(a, b, pin_len = 4, output = ""):
	for i in xrange(pin_len):
		output += str(random.randint(a, b))
	print "Random Pin Code; ", output, "\n"

	#print "SHA512 HASH; ", hashlib.sha512(output).hexdigest(), "\n"
	#print "SHA1 HASH; ", hashlib.sha1(output).hexdigest()
	#print "MD5 HASH; ", hashlib.md5(output).hexdigest()

RandomPinCode(1, 9)
