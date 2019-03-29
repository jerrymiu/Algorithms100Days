ops = {
	'^': float.__pow__,
	'/': float.__truediv__,
	'*': float.__mul__,
	'+': float.__add__,
	'-': float.__sub__,
}

def postFix(inputExpression):
	stack = []
	for curChar in inputExpression.split():
		if curChar in ops:
			curChar = ops[curChar](stack.pop(-2), stack.pop(-1))
		else:
			curChar = float(curChar)
		stack.append(curChar)
	return stack.pop()