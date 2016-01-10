def optimus_prime(prime,iterations=8):
	print ""
	print "\nChoosen Prime %s \n" % prime
	for i in xrange(iterations):
		print (prime**i % 29),
		#print is_prime(prime**i % 29),

def is_prime(intake):
	return all(intake % p for p in xrange(2, intake))

optimus_prime(3301)
optimus_prime(1033)
optimus_prime(761)
