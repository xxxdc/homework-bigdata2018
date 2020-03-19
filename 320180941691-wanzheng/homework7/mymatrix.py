"""
This module provides the Matrix class.

>>> m = Matrix(3, 3, value=2.0)
>>> m
[[2.0, 2.0, 2.0], [2.0, 2.0, 2.0], [2.0, 2.0, 2.0]]
>>> m.row
3
>>> m.shape
(3, 3)
>>> m[1][1]
2.0
>>> m[1][1] = 20.0
>>> m[1][1]
20.0
>>> m = Matrix(3, 3, value=2.0)
>>> n = Matrix(3, 3, value=2.0)
>>> m == n
True
>>> m != n
False
>>> m = Matrix(3, 3, value=2.0)
>>> n = Matrix(3, 3, value=1.0)
>>> m + n
[[3.0, 3.0, 3.0], [3.0, 3.0, 3.0], [3.0, 3.0, 3.0]]
>>> m - n
[[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]
>>> m * n
[[6.0, 6.0, 6.0], [6.0, 6.0, 6.0], [6.0, 6.0, 6.0]]
>>> m * 5
[[10.0, 10.0, 10.0], [10.0, 10.0, 10.0], [10.0, 10.0, 10.0]]
>>> m
[[2.0, 2.0, 2.0], [2.0, 2.0, 2.0], [2.0, 2.0, 2.0]]
>>> m ** 4
[[2592.0, 2592.0, 2592.0], [2592.0, 2592.0, 2592.0], [2592.0, 2592.0, 2592.0]]
>>> m[1] = [1.0, 1.0, 2.0]
>>> m[2] = [1.0, 2.0, 1.0]
>>> m[3] = [2.0, 1.0, 1.0]
>>> m.invert()
[[-0.25, -0.25, 0.75], [-0.25, 0.75, -0.25], [0.75, -0.25, -0.25]]
>>> m.rank()
3
>>> m
[[1.0, 1.0, 2.0], [1.0, 2.0, 1.0], [2.0, 1.0, 1.0]]
>>> m.transpose()
[[1.0, 1.0, 2.0], [1.0, 2.0, 1.0], [2.0, 1.0, 1.0]]
>>> m.cofactor(1,1)
[[2.0, 1.0], [1.0, 1.0]]
>>> m.det()
-10.0
>>> m.zeros()
[[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
>>> m.ones()
[[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]
>>> m.identity()
[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
>>> m = Matrix(3, 3, value=2.0)
>>> m.show()
2.0  2.0  2.0  
2.0  2.0  2.0  
2.0  2.0  2.0  
"""

import copy


class Matrix:
	'''the Matrix class'''

	def __init__(self, row, column, value=0.0):
		''' Initialize a matrix

		>>> m = Matrix(3, 3, value=2.0)
		>>> m
		[[2.0, 2.0, 2.0], [2.0, 2.0, 2.0], [2.0, 2.0, 2.0]]
		>>> m.row
		3
		>>> m.shape
		(3, 3)
		'''
		self.shape = (row, column)
		self.row = row
		self.column = column
		self._matrix = [[value for i in range(column)] for i in range(row)]

	def __getitem__(self, index):
		''' Returns the value represented on the specified index in the matrix

		>>> m = Matrix(3, 3, value=2.0)
		>>> m[1,1]
		2.0
		'''
		if isinstance(index, int):
			return self._matrix[index - 1]
		elif isinstance(index, tuple):
			return self._matrix[index[0] - 1][index[1] - 1]

	def __setitem__(self, index, value):
		''' To set the value given on the specified index in the matrix

		>>> m = Matrix(3, 3, value=2.0)
		>>> m[1,1] = 20.0
		>>> m[1,1]
		20.0
		'''
		if isinstance(index, int):
			self._matrix[index - 1] = copy.deepcopy(value)
		elif isinstance(index, tuple):
			self._matrix[index[0] - 1][index[1] - 1] = value

	def __eq__(self, N):
		''' Overload the operator "=="
		>>> m = Matrix(3, 3, value=2.0)
		>>> n = Matrix(3, 3, value=2.0)
		>>> m == n
		True
		'''
		assert isinstance(N, Matrix)
		return N._matrix == self._matrix

	def __add__(self, N):
		''' Overload the operator "+"
		>>> m = Matrix(3, 3, value=2.0)
		>>> n = Matrix(3, 3, value=1.0)
		>>> m + n
		[[3.0, 3.0, 3.0], [3.0, 3.0, 3.0], [3.0, 3.0, 3.0]]
		'''
		assert N.shape == self.shape
		M = Matrix(self.row, self.column)
		for r in range(self.row):
			for c in range(self.column):
				M[r, c] = self[r, c] + N[r, c]
		return M

	def __sub__(self, N):
		''' Overload the operator "-"
		>>> m = Matrix(3, 3, value=2.0)
		>>> n = Matrix(3, 3, value=1.0)
		>>> m - n
		[[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]
		'''
		assert N.shape == self.shape
		M = Matrix(self.row, self.column)
		for r in range(self.row):
			for c in range(self.column):
				M[r, c] = self[r, c] - N[r, c]
		return M

	def __mul__(self, N):
		''' Overload the operator "*"
		>>> m = Matrix(3, 3, value=2.0)
		>>> n = Matrix(3, 3, value=1.0)
		>>> m * n
		[[6.0, 6.0, 6.0], [6.0, 6.0, 6.0], [6.0, 6.0, 6.0]]
		>>> m * 5
		[[10.0, 10.0, 10.0], [10.0, 10.0, 10.0], [10.0, 10.0, 10.0]]
		'''
		if isinstance(N, int) or isinstance(N, float):
			M = Matrix(self.row, self.column)
			for r in range(self.row):
				for c in range(self.column):
					M[r, c] = self[r, c] * N
		else:
			assert N.row == self.column
			M = Matrix(self.row, N.column)
			for r in range(self.row):
				for c in range(N.column):
					sum = 0
					for k in range(self.column):
						sum += self[r, k] * N[k, r]
					M[r, c] = sum
		return M

	def __pow__(self, k):
		''' Overload the operator "**"

		>>> m = Matrix(3, 3, value=2.0)
		>>> m ** 4
		[[2592.0, 2592.0, 2592.0], [2592.0, 2592.0, 2592.0], [2592.0, 2592.0, 2592.0]]
		'''
		assert self.row == self.column
		M = copy.deepcopy(self)
		for i in range(k):
			M = M * self
		return M

	def __repr__(self):
		return "{}".format(self._matrix)



	def transpose(self):
		''' Returns a transpose matrix

		>>> m = Matrix(3, 3, value=2.0)
		>>> m.transpose()
		[[2.0, 2.0, 2.0], [2.0, 2.0, 2.0], [2.0, 2.0, 2.0]]
		'''
		M = Matrix(self.column, self.row)
		for r in range(self.column):
			for c in range(self.row):
				M[r, c] = self[c, r]
		return M

	def cofactor(self, row, column):
		'''Returns the one of cofactors of a matrix

		>>> m = Matrix(3, 3, value=2.0)
		>>> m.cofactor(1,1)
		[[2.0, 2.0], [2.0, 2.0]]
		'''
		assert self.row == self.column, "Matrices that are not square matrices have no cofactors"
		assert self.row >= 3, "At least the third order square matrix"
		assert row <= self.row and column <= self.column, "The index is out of range"
		M = Matrix(self.column - 1, self.row - 1)
		for r in range(self.row):
			if r == row:
				continue
			for c in range(self.column):
				if c == column:
					continue
				rr = r - 1 if r > row else r
				cc = c - 1 if c > column else c
				M[rr, cc] = self[r, c]
		return M

	def det(self):
		'''Evaluate the determinant(determinant)

		>>> m = Matrix(3, 3, value=2.0)
		>>> m.det()
		0.0
		'''
		assert self.row == self.column, "Matrices that are not square matrices have no determinant"
		if self.shape == (2, 2):
			return self[1, 1] * self[2, 2] - self[1, 2] * self[2, 1]
		else:
			sum = 0.0
			for c in range(self.column + 1):
				sum += (-1) ** (c + 1) * self[1, c] * self.cofactor(1, c).det()
			return sum



	def invert(self):
		''' Returns an inverse matrix

		>>> m = Matrix(3, 3, value=2.0)
		>>> m[1] = [1.0, 1.0, 2.0]
		>>> m[2] = [1.0, 2.0, 1.0]
		>>> m[3] = [2.0, 1.0, 1.0]
		>>> m.invert()
		[[-0.25, -0.25, 0.75], [-0.25, 0.75, -0.25], [0.75, -0.25, -0.25]]
		'''
		assert self.row == self.column, "Matrices that are not square matrices have no invert matrix "
		M = Matrix(self.row, self.column * 2)

		# The inverse matrix is obtained by splicing
		I = self.identity()	 # Unit matrix
		for r in range(1, M.row + 1):
			temp = copy.deepcopy(self[r])
			temp.extend(I[r])
			M[r] = copy.deepcopy(temp)

		# Elementary row operations
		for r in range(1, M.row + 1):
			# If the first element in the current row(M[r, r])is 0，swap down the rows that are closest when the front row element is non-zero
			if M[r, r] == 0:
				for rr in range(r + 1, M.row + 1):
					if M[rr, r] != 0:
						M[r], M[rr] = M[rr], M[r]  # Exchange of two lines
					break

			assert M[r, r] != 0, 'The rank of an n-order matrix must be n, otherwise the matrix is not invertible'

			# make the first element in the current row one
			temp = M[r, r]
			for c in range(r, M.column + 1):
				M[r, c] /= temp

			# Converts all elements above and below this column to 0
			for rr in range(1, M.row + 1):
				temp = M[rr, r]
				for c in range(r, M.column + 1):
					if rr == r:
						continue
					M[rr, c] -= temp * M[r, c]

		# Intercept the inverse matrix converted from the identity matrix
		N = Matrix(self.row, self.column)
		for r in range(1, self.row + 1):
			N[r] = M[r][self.row:]
		return N

	def rank(self):
		''' Returns the rank of the Matrix
		
		>>> m = Matrix(3, 3, value=2.0)
		>>> m[1] = [1.0, 1.0, 2.0]
		>>> m[2] = [1.0, 2.0, 1.0]
		>>> m[3] = [2.0, 1.0, 1.0]
		>>> m.rank()
		3
		'''
		m = copy.deepcopy(self)
		m = m.jieti()
		sum = 0
		for i in range(1,m.row+1):
			flag = 0
			for j in range(1,m.column+1):
				if(m[i,j] == 1.0): flag = 1
			sum += flag
		return sum

	def adjoint(self):
		''' Returns the adjoint matrix
		
		>>> m = Matrix(3, 3, value=2.0)
		>>> m[1] = [1.0, 1.0, 2.0]
		>>> m[2] = [1.0, 2.0, 1.0]
		>>> m[3] = [2.0, 1.0, 1.0]
		>>> m.adjoint()
		[[2.5, 2.5, -7.5], [2.5, -7.5, 2.5], [-7.5, 2.5, 2.5]]
		'''
		m = copy.deepcopy(self)
		m._matrix = m.invert() * m.det()
		return m

	def jieti(self):
		''' Returns the adjoint matrix
		
		>>> m = Matrix(3, 3, value=2.0)
		>>> m[1] = [1.0, 1.0, 2.0]
		>>> m[2] = [1.0, 2.0, 1.0]
		>>> m[3] = [2.0, 1.0, 1.0]
		>>> m.jieti()
		[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
		'''
		M = copy.deepcopy(self)

		# primary row transformation
		for r in range(1, M.row + 1):
			# If the first element in the current row(M[r, r])is 0，swap down the rows that are closest when the front row element is non-zero
			if M[r, r] == 0:
				for rr in range(r + 1, M.row + 1):
					if M[rr, r] != 0:
						M[r], M[rr] = M[rr], M[r]  # Exchange of two lines
					break

			# make the first element in the current row zero
			temp = M[r, r]
			for c in range(r, M.column + 1):
				M[r, c] /= temp

			# Converts all elements above and below this column to 0
			for rr in range(1, M.row + 1):
				temp = M[rr, r]
				for c in range(r, M.column + 1):
					if rr == r:
						continue
					M[rr, c] -= temp * M[r, c]

		return M



	def zeros(self):
		'''Returns the full zero form of the matrix

		>>> m = Matrix(3, 3, value=2.0)
		>>> m.zeros()
		[[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
		'''
		M = Matrix(self.column, self.row, value=0.0)
		return M

	def ones(self):
		'''Returns the full one form of the matrix

		>>> m = Matrix(3, 3, value=2.0)
		>>> m.ones()
		[[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]
		'''
		M = Matrix(self.column, self.row, value=1.0)
		return M

	def identity(self):
		'''Returns the identity matrix of the matrix

		>>> m = Matrix(3, 3, value=2.0)
		>>> m.identity()
		[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
		'''
		assert self.row == self.column, "Only the square matrix has the identity matrix"
		M = Matrix(self.column, self.row)
		for r in range(self.row):
			for c in range(self.column):
				M[r, c] = 1.0 if r == c else 0.0
		return M

	def show(self):
		'''Show the matrix

		>>> m = Matrix(3, 3, value=2.0)
		>>> m.show()
		2.0  2.0  2.0  
		2.0  2.0  2.0  
		2.0  2.0  2.0  
		'''
		for r in range(self.row):
			for c in range(self.column):
				print(self[r + 1, c + 1],end='  ')
			print()




if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)