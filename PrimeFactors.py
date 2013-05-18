
#http://content.codersdojo.org/code-kata-catalogue/prime-factors/

def FactorPrimes(number):
	primeFactors = []
	counter = number
	#otherwise 1 is included
	while counter > 2:
		counter = counter - 1
		#The recursion removes factors that aren't prime.
		if number % counter == 0 and FactorPrimes(counter) == []:
			primeFactors.append(counter)
	return primeFactors

#just testing to make sure it works
i = 1
while i < 40:
	print FactorPrimes(i)
	i = i + 1
	
