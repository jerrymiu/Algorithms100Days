def count1bits(k):
	i = 0
	while k:
		k &= k - 1
		i += 1
	return i