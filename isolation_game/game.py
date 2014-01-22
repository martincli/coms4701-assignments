from node import Node
import time

# Alpha-beta algorithm
def alpha_beta(node, depth, myBest, oppBest, isXTurn, startTime, timeLimit):
	if isXTurn:
		player = 'x'
	else:
		player = 'o'
	
	if depth == 0:
		return (node.getValue(player), None)

	moveList = node.getValidMoves(player)
	bestVal = myBest
	bestMove = None

	# If time limit is up, return best move so far
	if time.time() - timeLimit > startTime:
		return (bestVal, bestMove)

	for move in moveList:
		tryVal = -alpha_beta(move, depth-1, -oppBest, -bestVal, not isXTurn, startTime, timeLimit)[0]

		if tryVal > bestVal:
			bestVal = tryVal
			bestMove = move

		if bestVal > oppBest:
			return (bestVal, bestMove)

	return (bestVal, bestMove)

if __name__ == '__main__':
	# Initial board state
	game = Node((1,1),(8,8),[])

	# Set time limit
	print
	timeLimit = input('Set time limit per move (seconds): ')

	# Set ply (search tree depth limit)
	ply = input('Set ply (depth limit): ')

	# Player initiation
	while True:
		playerInit = raw_input('Is this player x or o? ')
		if playerInit == 'x':
			# Set player to x
			isX = True

			# Determine first move with alpha-beta
			print '\nFirst move:',
			timer = time.time()
			firstMove = alpha_beta(game, ply, -99999, 99999, True, timer, timeLimit)[1].xLoc

			# Make first move
			print firstMove
			game.filledSquares.append(game.xLoc)
			game.xLoc = firstMove
			game.printState()
			print
			break
		elif playerInit == 'o':
			# Set player to o
			isX = False
			print
			break
		print 'ERROR: Please enter "x" or "o"\n'

	# Loop for moves
	while True:
		moveInput = raw_input('Enter opponent\'s move: ')
		if isX:
			# Make opponent's move
			oppMove = eval(moveInput)
			game.filledSquares.append(game.oLoc)
			game.oLoc = oppMove
			game.printState()

			# Determine next move with alpha-beta
			print '\nMy move:',
			timer = time.time()
			(myVal, myMove) = alpha_beta(game, ply, -99999, 99999, True, timer, timeLimit)
			
			# Make my move
			if myMove:
				print myMove.xLoc
				game.filledSquares.append(game.xLoc)
				game.xLoc = myMove.xLoc
				game.printState()
				print
			else:
				print "GAME OVER. I lose :("
				print
		else:
			# Make opponent's move
			oppMove = eval(moveInput)
			game.filledSquares.append(game.xLoc)
			game.xLoc = oppMove
			game.printState()

			# Determine next move with alpha-beta
			print '\nMy move:',
			timer = time.time()
			(myVal, myMove) = alpha_beta(game, ply, -99999, 99999, False, timer, timeLimit)

			# Make my move
			if myMove:
				print myMove.oLoc
				game.filledSquares.append(game.oLoc)
				game.oLoc = myMove.oLoc
				game.printState()
				print
			else:
				print "GAME OVER. I lose :("
				print