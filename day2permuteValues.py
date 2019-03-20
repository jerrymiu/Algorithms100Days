def permute(valuesInput):
	lenValues = len(valuesInput)
	for i in reversed(range(lenValues-1)):
		if valuesInput[i] < valuesInput[i+1]:
			break
	else:
		valuesInput[:] = reversed(valuesInput[:])
		return valuesInput

	#In remaining portion
	for k in reversed(range(i, n)):
		if valuesInput[i] < valuesInput[k]:
			valuesInput[i], valuesInput[k] = valuesInput[k], valuesInput[i]
			valuesInput[i+1:] = reversed(valuesInput[i+1:])
			break

	return valuesInput