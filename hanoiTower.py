def hanoiTower(height, left='left', right='right', middle='middle'):
	"""Recursively solve the tower of hanoi by moving the N-1 disks from
	left to middle
	height: 
	"""
	if height:
		hanoiTower(height-1, left, middle, right)
		print(left, '->', right)
		hanoiTower(height-1, middle, right, left)