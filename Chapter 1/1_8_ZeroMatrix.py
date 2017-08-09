'''
1.8 Zero Matrix:
Write an algorithm such that if an element in an MxN matrix is 0, it's entire
row and column are set to 0.
'''

# input will be an MxN matrix
# if matrix[1][1] = 0, then [all rows][1] = 0 and [1][all columns] = 0

input1 =[[1, 4, 2, 6],
		 [3, 6, 0, 5],
		 [6, 8, 4, 1],
		 [4, 8, 2, 3]]

'''
input1[1][2] = 0, so output should be:

		[[1, 4, 0, 6],
		 [0, 0, 0, 0],
		 [6, 8, 0, 1],
		 [4, 8, 0, 3]]
'''

input2 = [[0, 2, 4, 6],
		  [-1, 1, 3, 5],
		  [-2, 0, 2, 4],
		  [-3, -1, 1, 3]]

def zero_matrix(m):
	zero_row = []
	zero_col = []
	found_zero = False
	for row in range(len(m)):
		for col in range(len(m)):
			if m[row][col] == 0:
				zero_row.append(row)
				zero_col.append(col)
	for row in range(len(m)):
		for col in range(len(m)):
			for rowzero in zero_row:
				for colzero in zero_col:
					m[rowzero][col] = 0
					m[row][colzero] = 0
	return m

print zero_matrix(input1)
print zero_matrix(input2)
