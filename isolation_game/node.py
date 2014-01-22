from math import fabs

class Node:
	def __init__(self, xLoc, oLoc, filledSquares):
		self.xLoc = xLoc
		self.oLoc = oLoc
		self.filledSquares = filledSquares

	# Print board state for node
	def printState(self):
		state = []
		for i in range(8):
			state.append([])
			for j in range(8):
				state[i].append('-')
		state[self.xLoc[0]-1][self.xLoc[1]-1] = 'x'
		state[self.oLoc[0]-1][self.oLoc[1]-1] = 'o'

		for square in self.filledSquares:
			state[square[0]-1][square[1]-1] = '*'
		
		for row in state:
			print
			for element in row:
				print element,
		print

	# List of valid moves from node
	def getValidMoves(self, player):
		validMoves = []

		# Moves for player x
		if player == 'x':
			# Up
			row = self.xLoc[0]
			col = self.xLoc[1]
			while row > 1:
				if (row-1, col) in self.filledSquares or (row-1, col) == self.oLoc:
					break
				else:
					newFilledSquares = list(self.filledSquares)
					newFilledSquares.append((self.xLoc))
					validMoves.append(Node((row-1, col), self.oLoc, newFilledSquares))
					row -= 1
			# Up-Right
			row = self.xLoc[0]
			col = self.xLoc[1]
			while row > 1 and col < 8:
				if (row-1, col+1) in self.filledSquares or (row-1, col+1) == self.oLoc:
					break
				else:
					newFilledSquares = list(self.filledSquares)
					newFilledSquares.append((self.xLoc))
					validMoves.append(Node((row-1, col+1), self.oLoc, newFilledSquares))
					row -= 1
					col += 1
			# Right
			row = self.xLoc[0]
			col = self.xLoc[1]
			while col < 8:
				if (row, col+1) in self.filledSquares or (row, col+1) == self.oLoc:
					break
				else:
					newFilledSquares = list(self.filledSquares)
					newFilledSquares.append((self.xLoc))
					validMoves.append(Node((row, col+1), self.oLoc, newFilledSquares))
					col += 1
			# Down-Right
			row = self.xLoc[0]
			col = self.xLoc[1]
			while row < 8 and col < 8:
				if (row+1, col+1) in self.filledSquares or (row+1, col+1) == self.oLoc:
					break
				else:
					newFilledSquares = list(self.filledSquares)
					newFilledSquares.append((self.xLoc))
					validMoves.append(Node((row+1, col+1), self.oLoc, newFilledSquares))
					row += 1
					col += 1
			# Down
			row = self.xLoc[0]
			col = self.xLoc[1]
			while row < 8:
				if (row+1, col) in self.filledSquares or (row+1, col) == self.oLoc:
					break
				else:
					newFilledSquares = list(self.filledSquares)
					newFilledSquares.append((self.xLoc))
					validMoves.append(Node((row+1, col), self.oLoc, newFilledSquares))
					row += 1
			# Down-Left
			row = self.xLoc[0]
			col = self.xLoc[1]
			while row < 8 and col > 1:
				if (row+1, col-1) in self.filledSquares or (row+1, col-1) == self.oLoc:
					break
				else:
					newFilledSquares = list(self.filledSquares)
					newFilledSquares.append((self.xLoc))
					validMoves.append(Node((row+1, col-1), self.oLoc, newFilledSquares))
					row += 1
					col -= 1
			# Left
			row = self.xLoc[0]
			col = self.xLoc[1]
			while col > 1:
				if (row, col-1) in self.filledSquares or (row, col-1) == self.oLoc:
					break
				else:
					newFilledSquares = list(self.filledSquares)
					newFilledSquares.append((self.xLoc))
					validMoves.append(Node((row, col-1), self.oLoc, newFilledSquares))
					col -= 1
			# Up-Left
			row = self.xLoc[0]
			col = self.xLoc[1]
			while row > 1 and col > 1:
				if (row-1, col-1) in self.filledSquares or (row-1, col-1) == self.oLoc:
					break
				else:
					newFilledSquares = list(self.filledSquares)
					newFilledSquares.append((self.xLoc))
					validMoves.append(Node((row-1, col-1), self.oLoc, newFilledSquares))
					row -= 1
					col -= 1

		# Moves for player o
		elif player == 'o':
			# Up
			row = self.oLoc[0]
			col = self.oLoc[1]
			while row > 1:
				if (row-1, col) in self.filledSquares or (row-1, col) == self.xLoc:
					break
				else:
					newFilledSquares = list(self.filledSquares)
					newFilledSquares.append((self.oLoc))
					validMoves.append(Node(self.xLoc, (row-1, col), newFilledSquares))
					row -= 1
			# Up-Right
			row = self.oLoc[0]
			col = self.oLoc[1]
			while row > 1 and col < 8:
				if (row-1, col+1) in self.filledSquares or (row-1, col+1) == self.xLoc:
					break
				else:
					newFilledSquares = list(self.filledSquares)
					newFilledSquares.append((self.oLoc))
					validMoves.append(Node(self.xLoc, (row-1, col+1), newFilledSquares))
					row -= 1
					col += 1
			# Right
			row = self.oLoc[0]
			col = self.oLoc[1]
			while col < 8:
				if (row, col+1) in self.filledSquares or (row, col+1) == self.xLoc:
					break
				else:
					newFilledSquares = list(self.filledSquares)
					newFilledSquares.append((self.oLoc))
					validMoves.append(Node(self.xLoc, (row, col+1), newFilledSquares))
					col += 1
			# Down-Right
			row = self.oLoc[0]
			col = self.oLoc[1]
			while row < 8 and col < 8:
				if (row+1, col+1) in self.filledSquares or (row+1, col+1) == self.xLoc:
					break
				else:
					newFilledSquares = list(self.filledSquares)
					newFilledSquares.append((self.oLoc))
					validMoves.append(Node(self.xLoc, (row+1, col+1), newFilledSquares))
					row += 1
					col += 1
			# Down
			row = self.oLoc[0]
			col = self.oLoc[1]
			while row < 8:
				if (row+1, col) in self.filledSquares or (row+1, col) == self.xLoc:
					break
				else:
					newFilledSquares = list(self.filledSquares)
					newFilledSquares.append((self.oLoc))
					validMoves.append(Node(self.xLoc, (row+1, col), newFilledSquares))
					row += 1
			# Down-Left
			row = self.oLoc[0]
			col = self.oLoc[1]
			while row < 8 and col > 1:
				if (row+1, col-1) in self.filledSquares or (row+1, col-1) == self.xLoc:
					break
				else:
					newFilledSquares = list(self.filledSquares)
					newFilledSquares.append((self.oLoc))
					validMoves.append(Node(self.xLoc, (row+1, col-1), newFilledSquares))
					row += 1
					col -= 1
			# Left
			row = self.oLoc[0]
			col = self.oLoc[1]
			while col > 1:
				if (row, col-1) in self.filledSquares or (row, col-1) == self.xLoc:
					break
				else:
					newFilledSquares = list(self.filledSquares)
					newFilledSquares.append((self.oLoc))
					validMoves.append(Node(self.xLoc, (row, col-1), newFilledSquares))
					col -= 1
			# Up-Left
			row = self.oLoc[0]
			col = self.oLoc[1]
			while row > 1 and col > 1:
				if (row-1, col-1) in self.filledSquares or (row-1, col-1) == self.xLoc:
					break
				else:
					newFilledSquares = list(self.filledSquares)
					newFilledSquares.append((self.oLoc))
					validMoves.append(Node(self.xLoc, (row-1, col-1), newFilledSquares))
					row -= 1
					col -= 1

		return validMoves

	# Heuristic value of node
	def getValue(self, player):

		# Value of win/loss states
		if player == 'x':
			if not self.getValidMoves('x'):
				return -99999
			if not self.getValidMoves('o'):
				return 99999
		else:
			if not self.getValidMoves('o'):
				return -99999
			if not self.getValidMoves('x'):
				return 99999
		
		# Number of valid moves
		numValidMoves = len(self.getValidMoves(player))
		
		# Average distance from all occupied squares
		totalDistance = 0
		if player == 'x':
			for square in self.filledSquares:
				totalDistance = totalDistance + fabs(square[0] - self.xLoc[0]) + fabs(square[1] - self.xLoc[1])
			totalDistance = totalDistance + fabs(self.oLoc[0] - self.xLoc[0]) + fabs(self.oLoc[1] - self.xLoc[1])
		else:
			for square in self.filledSquares:
				totalDistance = totalDistance + fabs(square[0] - self.oLoc[0]) + fabs(square[1] - self.oLoc[1])
			totalDistance = totalDistance + fabs(self.xLoc[0] - self.oLoc[0]) + fabs(self.xLoc[1] - self.oLoc[1])
		avgDistance = totalDistance / (len(self.filledSquares) + 1)

		# Weighted heuristic value
		weightedValue = numValidMoves + (2.25 * avgDistance)
		return weightedValue