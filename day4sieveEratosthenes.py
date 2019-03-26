def sieveEratosthenes(i):
	#Generate all primes up to i
	primes = []
	candidates = range(2, i+1)
	while candidates:
		curPrime = candidates[0]
		primes.append(curPrime)
		candidates = [num for num in candidates if num % curPrime != 0]
	return primes
