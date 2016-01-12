# List to add the decrypted letters to.
text = [ ]

def optimus_prime(prime,iterations=101,q=29):
	print ""
	print "\nChoosen Prime %s \n" % prime
	for i in xrange(iterations):
		print (prime**i % q),
		collection(prime**i % q),
		#print is_prime(prime**i % q),
	print text

# Check if Prime or not
def is_prime(intake):
	return all(intake % p for p in xrange(2, intake))

# To Translate the primes to Text
def collection(number):

	if number == 2:
		text.append("F")
	if number == 3:
		text.append("U")
	if number == 5:
		text.append("TH")
	if number == 7:
		text.append("O")
	if number == 11:
		text.append("R")
	if number == 13:
		text.append("C/K")
	if number == 17:
		text.append("G")
	if number == 19:
		text.append("W")
	if number == 23:
		text.append("H")
	if number == 29:
		text.append("N")
	if number == 29:
		text.append("N")
	if number == 29:
		text.append("N")
	if number == 29:
		text.append("N")
	if number == 29:
		text.append("N")
	if number == 29:
		text.append("N")



#optimus_prime(733161671143113171353)
#optimus_prime(1033)
#optimus_prime(761)
optimus_prime(6603)
