#Iterates triough a list, spits all the number out
#Then checks if the number is a prime number.

def optimus_prime(prime,iterations=101):
	print ""
	print "\nChoosen Prime %s \n" % prime
	for i in xrange(iterations):
		print is_prime(prime**i % 29)

def is_prime(intake):
	print "%s a prime number?" % intake,
	print all(intake % p for p in xrange(2, intake)),

optimus_prime(3301)
optimus_prime(1033)
optimus_prime(761)
