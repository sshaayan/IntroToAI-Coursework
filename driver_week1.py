import time
import resource
from Queue import PriorityQueue
import sys

class board:
	@staticmethod
	def copy(boardArray):
		copy = list(boardArray)
		return copy

	@staticmethod
	def moveUp(boardArray):
		newBoard = board.copy(boardArray)
		position = newBoard.index(0)

		for x in range(0, 3):
			if x == position:
				return None

		temp = newBoard[position - 3]
		newBoard[position - 3] = newBoard[position]
		newBoard[position] = temp
		return newBoard

	@staticmethod
	def moveDown(boardArray):
		newBoard = board.copy(boardArray)
		position = newBoard.index(0)

		for x in range(6, 9):
			if x == position:
				return None

		temp = newBoard[position + 3]
		newBoard[position + 3] = newBoard[position]
		newBoard[position] = temp
		return newBoard

	@staticmethod
	def moveLeft(boardArray):
		newBoard = board.copy(boardArray)
		position = newBoard.index(0)

		if position == 0 or position == 3 or position == 6:
			return None

		temp = newBoard[position - 1]
		newBoard[position - 1] = newBoard[position]
		newBoard[position] = temp
		return newBoard

	@staticmethod
	def moveRight(boardArray):
		newBoard = board.copy(boardArray)
		position = newBoard.index(0)

		if position == 2 or position == 5 or position == 8:
			return None

		temp = newBoard[position + 1]
		newBoard[position + 1] = newBoard[position]
		newBoard[position] = temp
		return newBoard


class state:
	def __init__(self, current, parent, moveMade, depth):
		self.data = current
		self.parentNode = parent
		self.prevMove = moveMade
		self.nodeDepth = depth

	@staticmethod
	def generateChildren(parent):
		nextChildren = []
		nextChildren.append(state(board.moveUp(parent.data), parent, 'Up', parent.nodeDepth + 1))
		nextChildren.append(state(board.moveDown(parent.data), parent, 'Down', parent.nodeDepth + 1))
		nextChildren.append(state(board.moveLeft(parent.data), parent, 'Left', parent.nodeDepth + 1))
		nextChildren.append(state(board.moveRight(parent.data), parent, 'Right', parent.nodeDepth + 1))
		return nextChildren


def convertToInt(value):
	intValue = 0
	mult = 100000000
	for x in value:
		intValue += x * mult
		mult /= 10

	return intValue


GOAL_STATE = state([0, 1, 2, 3, 4, 5, 6, 7, 8], None, None, 0)
NODES_EXPANDED = 0
MAX_SEARCH_DEPTH = 0

def bfs_solver(boardState):
	global MAX_SEARCH_DEPTH
	global NODES_EXPANDED
	MAX_SEARCH_DEPTH = 0
	NODES_EXPANDED = 0

	initState = state(boardState, None, None, 0)
	frontier = [initState]
	searchFrontier = {convertToInt(initState.data) : initState}
	explored = {}

	while len(frontier) != 0:
		currentState = frontier.pop()
		del searchFrontier[convertToInt(currentState.data)]
		explored[convertToInt(currentState.data)] = currentState

		if currentState.data == GOAL_STATE.data:
			return currentState

		childArray = state.generateChildren(currentState)
		NODES_EXPANDED += 1
		for newState in childArray:
			if newState.data == None:
				continue

			inFrontier = False
			inExplored = explored.has_key(convertToInt(newState.data))
			if inExplored == False:
				inFrontier = searchFrontier.has_key(convertToInt(newState.data))

			if inFrontier == False and inExplored == False:
				frontier.insert(0, newState)
				searchFrontier[convertToInt(newState.data)] = newState
				if newState.nodeDepth > MAX_SEARCH_DEPTH:
					MAX_SEARCH_DEPTH = newState.nodeDepth

	return False


def bfs(boardState):
	startTime = time.time()

	goalData = bfs_solver(boardState)

	if goalData == False:
		print("An error has occurred")
		return

	output(goalData, startTime)


def dfs_solver(boardState):
	global MAX_SEARCH_DEPTH
	global NODES_EXPANDED
	MAX_SEARCH_DEPTH = 0
	NODES_EXPANDED = 0

	initState = state(boardState, None, None, 0)
	frontier = [initState]
	searchFrontier = {convertToInt(initState.data) : initState}
	explored = {}

	while len(frontier) != 0:
		currentState = frontier.pop()
		del searchFrontier[convertToInt(currentState.data)]
		explored[convertToInt(currentState.data)] = currentState

		if currentState.data == GOAL_STATE.data:
			return currentState

		childArray = state.generateChildren(currentState)
		NODES_EXPANDED += 1
		for newState in reversed(childArray):
			if newState.data == None:
				continue

			inFrontier = False
			inExplored = explored.has_key(convertToInt(newState.data))
			if inExplored == False:
				inFrontier = searchFrontier.has_key(convertToInt(newState.data))

			if inFrontier == False and inExplored == False:
				frontier.append(newState)
				searchFrontier[convertToInt(newState.data)] = newState
				if newState.nodeDepth > MAX_SEARCH_DEPTH:
					MAX_SEARCH_DEPTH = newState.nodeDepth

	return False


def dfs(boardState):
	startTime = time.time()

	goalData = dfs_solver(boardState)

	if goalData == False:
		print("An error has occurred")
		return

	output(goalData, startTime)


H_FUNCTION = [[1, 0, 1, 2, 1, 2, 3, 2, 3], [2, 1, 0, 3, 2, 1, 4, 3, 2], [1, 2, 3, 0, 1, 2, 1, 2, 3], [2, 1, 2, 1, 0, 1, 2, 1, 2], [3, 2, 1, 2, 1, 0, 3, 2, 1], [2, 3, 4, 1, 2, 3, 0, 1, 2], [3, 2, 3, 2, 1, 2, 1, 0, 1], [4, 3, 2, 3, 2, 1, 2, 1, 0]]

def estCost(boardState):
	global H_FUNCTION
	gCost = boardState.nodeDepth
	hCost = 0
	for i in range(0, 9):
		if boardState.data[i] == 0:
			continue

		hCost += H_FUNCTION[boardState.data[i] - 1][i]

	fCost = hCost + gCost
	fCost *= 10
	if boardState.prevMove == 'Up':
		fCost += 1
	elif boardState.prevMove == 'Down':
		fCost += 2
	elif boardState.prevMove == 'Left':
		fCost += 3
	else:
		fCost += 4

	return fCost


def ast_solver(boardState):
	global MAX_SEARCH_DEPTH
	global NODES_EXPANDED
	MAX_SEARCH_DEPTH = 0
	NODES_EXPANDED = 0

	initState = state(boardState, None, None, 0)
	frontier = PriorityQueue()
	frontier.put((estCost(initState), initState))
	searchFrontier = {convertToInt(initState.data) : initState}
	explored = {}

	while bool(frontier):
		currentState = frontier.get()[1]
		del searchFrontier[convertToInt(currentState.data)]
		explored[convertToInt(currentState.data)] = currentState

		if currentState.data == GOAL_STATE.data:
			return currentState

		childArray = state.generateChildren(currentState)
		NODES_EXPANDED += 1
		for newState in childArray:
			if newState.data == None:
				continue

			searchKey = convertToInt(newState.data)
			inFrontier = searchFrontier.has_key(searchKey)
			inExplored = explored.has_key(searchKey)

			if inFrontier == False and inExplored == False:
				frontier.put((estCost(newState), newState))
				searchFrontier[convertToInt(newState.data)] = newState
				if newState.nodeDepth > MAX_SEARCH_DEPTH:
					MAX_SEARCH_DEPTH = newState.nodeDepth

	return False


def ast(boardState):
	startTime = time.time()

	goalData = ast_solver(boardState)

	if goalData == False:
		print("An error has occurred")
		return

	output(goalData, startTime)


def output(goalData, startTime):
	pathToGoal = []
	currState = goalData
	while currState.prevMove != None:
		pathToGoal.insert(0, currState.prevMove)
		currState = currState.parentNode

	costOfPath = len(pathToGoal)
	numNodes = NODES_EXPANDED
	searchDepth = goalData.nodeDepth
	maxSearchDepth = MAX_SEARCH_DEPTH
	runTime = "%.8f" % round(time.time() - startTime, 8)
	maxRAMUsage = "%.8f" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 100000000.0)
	
	path = "["
	lastMove = pathToGoal[len(pathToGoal) - 1]
	del pathToGoal[len(pathToGoal) - 1]
	for x in pathToGoal:
		path += "'" + x + "', "
	path += "'" + lastMove + "']"

	output = "path_to_goal: " + path + "\ncost_of_path: " + str(costOfPath) + "\nnodes_expanded: " + str(numNodes) + "\nsearch_depth: " + str(searchDepth) + "\nmax_search_depth: " + str(maxSearchDepth) + "\nrunning_time: " + str(runTime) + "\nmax_ram_usage: " + str(maxRAMUsage) + "\n\n"

	file = open('output.txt', 'a')
	file.write(output)
	file.close()
	print(output)



dispatcher = {'bfs' : bfs, 'dfs' : dfs, 'ast' : ast}

method = sys.argv[1]
rawBoard = list(sys.argv[2])
length = len(rawBoard)
boardArray = []
for x in range(0, length):
	if x % 2 == 0:
		boardArray.append(int(rawBoard[x]))

dispatcher[method](boardArray)