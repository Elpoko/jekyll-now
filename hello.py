import itertools

var = [1, 2, 3, 4, 5, 6, 7, 8, 9]

perms = list(itertools.permutations(var))

def sumtotals(square):
	row1 = square[0] + square[1] + square[2]
	row2 = square[3] + square[4] + square[5]
	row3 = square[6] + square[7] + square[8]
	col1 = square[0] + square[3] + square[6]
	col2 = square[1] + square[4] + square[7]
	col3 = square[2] + square[5] + square[8]
	diag1 = square[0] + square[4] + square[8]
	diag2 = square[2] + square[4] + square[6]
	result = [row1, row2, row3, col1, col2, col3, diag1, diag2]
	return result
	
def allUnique(x):
	seen = set()
	return not any(i in seen or seen.add(i) for i in x)	

solutions = []
	
for list in perms:
	sums = sumtotals(list)
	if allUnique(sums):
		solutions.append(list)
		
print(solutions)
		
		
		