'''
1.7: Rotate Matrix
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degrees. Can you do this in place?
'''

input1 = [[1, 4, 2, 6],
		 [3, 6, 0, 5],
		 [6, 8, 4, 1],
		 [4, 8, 2, 0]]

input2 = [[0, 2, 4, 6],
		  [-1, 1, 3, 5],
		  [-2, 0, 2, 4],
		  [-3, -1, 1, 3]]


'''
input2 rotated 90:
   [[-3, -2, -1, 0],
	[-1, 0, 1, 2],
	[1, 2, 3, 4],
	[3, 4, 5, 6]]
'''

def rotate_matrix(m):
	flipzip = list(list(x)[::-1] for x in zip(*m))
	return flipzip


print rotate_matrix(input1)
print rotate_matrix(input2)


'''
Also a solution:

def rotate_matrix(m):
	matrix_length = len(m)
	for layer in range(matrix_length // 2):
		first = layer
		last = matrix_length - layer - 1
		for i in range(first, last):
			top = m[layer][i] # save top

			m[layer][i] = m[-i - 1][layer] # left -> top

			m[-i - 1][layer] = m[-layer - 1][-i - 1] # bottom -> left

			m[-layer - 1][-i - 1] = m[i][-layer - 1] # right -> bottom

			m[i][-layer - 1] = top # top -> right
	return m
'''





