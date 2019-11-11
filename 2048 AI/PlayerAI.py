from random import randint
from BaseAI import BaseAI
import time
from random import shuffle
import math

startTime = 0

class PlayerAI(BaseAI):
	def getMove(self, grid):
		global startTime
		startTime = time.clock()

		nextMove = PlayerAI.maximize(grid, float("-inf"), float("inf"), 0)[0]

		return nextMove

	@staticmethod
	def maximize(currGrid, alpha, beta, depth):
		global startTime

		if ((time.clock() - startTime) > 0.10) or depth > 5:
			return None, PlayerAI.heuristic(currGrid)

		(maxMove, maxUtility) = (None, float("-inf"))
		moves = currGrid.getAvailableMoves()
		for x in moves:
			nextGrid = currGrid.clone()
			nextGrid.move(x)

			utility = PlayerAI.minimize(nextGrid, alpha, beta, depth + 1)[1]

			if utility > maxUtility:
				(maxMove, maxUtility) = (x, utility)

			if maxUtility >= beta:
				break

			if maxUtility > alpha:
				alpha = maxUtility

		return (maxMove, maxUtility)

	@staticmethod
	def minimize(currGrid, alpha, beta, depth):
		global startTime

		if ((time.clock() - startTime) > 0.10) or depth > 5:
			return None, PlayerAI.heuristic(currGrid)

		(minMove, minUtility) = (None, float("inf"))
		moves = currGrid.getAvailableMoves()
		for x in moves:
			nextGrid = currGrid.clone()
			nextGrid.move(x)

			utility = PlayerAI.maximize(nextGrid, alpha, beta, depth + 1)[1]

			if utility < minUtility:
				(minMove, minUtility) = (x, utility)

			if minUtility <= alpha:
				break

			if minUtility < beta:
				beta = minUtility

		return (minMove, minUtility)

	@staticmethod
	def heuristic(currGrid):
		util = (1500 * len(currGrid.getAvailableCells())) + (10 * PlayerAI.calcCorners(currGrid)) + (1 * PlayerAI.calcSnake(currGrid)) + (2 * currGrid.getMaxTile())
		return util

	@staticmethod
	def calcCorners(currGrid):
		cornerWeight = currGrid.getCellValue((0, 2)) + (2 * currGrid.getCellValue((0, 1))) + (4 * currGrid.getCellValue((0, 0))) + (-1 * currGrid.getCellValue((1, 3))) + currGrid.getCellValue((1, 1)) + (2 * currGrid.getCellValue((1, 0))) + (-2 * currGrid.getCellValue((2, 3))) + (-1 * currGrid.getCellValue((2, 2))) + currGrid.getCellValue((2, 0)) + (-4 * currGrid.getCellValue((3, 3))) + (-2 * currGrid.getCellValue((3, 2))) + (-1 * currGrid.getCellValue((3, 1)))

		return cornerWeight

	@staticmethod
	def calcSnake(currGrid):
		firstWeight = (32768 * currGrid.getCellValue((0, 0))) + (16384 * currGrid.getCellValue((0, 1))) + (8192 * currGrid.getCellValue((0, 2))) + (4096 * currGrid.getCellValue((0, 3))) + (2048 * currGrid.getCellValue((1, 3))) + (1024 * currGrid.getCellValue((1, 2))) + (512 * currGrid.getCellValue((1, 1))) + (256 * currGrid.getCellValue((1, 0))) + (128 * currGrid.getCellValue((2, 0))) + (64 * currGrid.getCellValue((2, 1))) + (32 * currGrid.getCellValue((2, 2))) + (16 * currGrid.getCellValue((2, 3))) + (8 * currGrid.getCellValue((3, 3))) + (4 * currGrid.getCellValue((3, 2))) + (2 * currGrid.getCellValue((3, 1))) + currGrid.getCellValue((3, 0))

		secondWeight = (32768 * currGrid.getCellValue((0, 0))) + (16384 * currGrid.getCellValue((1, 0))) + (8192 * currGrid.getCellValue((2, 0))) + (4096 * currGrid.getCellValue((3, 0))) + (2048 * currGrid.getCellValue((3, 1))) + (1024 * currGrid.getCellValue((2, 1))) + (512 * currGrid.getCellValue((1, 1))) + (256 * currGrid.getCellValue((0, 1))) + (128 * currGrid.getCellValue((0, 2))) + (64 * currGrid.getCellValue((1, 2))) + (32 * currGrid.getCellValue((2, 2))) + (16 * currGrid.getCellValue((3, 2))) + (8 * currGrid.getCellValue((3, 3))) + (4 * currGrid.getCellValue((2, 3))) + (2 * currGrid.getCellValue((1, 3))) + currGrid.getCellValue((0, 3))

		weights = [firstWeight, secondWeight]
		maxWeight = max(weights)
		maxWeight /= 8192

		return maxWeight
