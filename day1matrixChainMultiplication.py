def matrixChainOrder(p):
	n = len(p)
	m = [[0 for x in range(n)] for x in range(n)]

	#Base case
	for i in range(1, n):
		m[i][i] = 0

	#Chain multiply
	for chainLen in range(2, n):
		for i in range(1, n-chainLen+1):
			j = i + chainLen -1
			m[i][j] = float('inf')
			for k in range(i, j):
				cost = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
				m[i][j] = min(cost, m[i][j])
	return m[1][n-1]