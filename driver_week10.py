import copy
import sys


#creates a dictionary for the sudoku table from a string of numbers
def create_sudoku_table(dataString):
	newTable = {}

	for x in range(0, len(dataString)):
		num = int(dataString[x])

		index = x
		while index / 9 > 0:
			index = index - 9

		index = index + 1

		row = "A"

		if x / 9 == 1:
			row = "B"
		elif x / 9 == 2:
			row = "C"
		elif x / 9 == 3:
			row = "D"
		elif x / 9 == 4:
			row = "E"
		elif x / 9 == 5:
			row = "F"
		elif x / 9 == 6:
			row = "G"
		elif x / 9 == 7:
			row = "H"
		elif x / 9 == 8:
			row = "I"

		dictIndex = row + str(index)
		newTable[dictIndex] = dataString[x]

	return newTable


unit_1 = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
unit_2 = ["A4", "A5", "A6", "B4", "B5", "B6", "C4", "C5", "C6"]
unit_3 = ["A7", "A8", "A9", "B7", "B8", "B9", "C7", "C8", "C9"]
unit_4 = ["D1", "D2", "D3", "E1", "E2", "E3", "F1", "F2", "F3"]
unit_5 = ["D4", "D5", "D6", "E4", "E5", "E6", "F4", "F5", "F6"]
unit_6 = ["D7", "D8", "D9", "E7", "E8", "E9", "F7", "F8", "F9"]
unit_7 = ["G1", "G2", "G3", "H1", "H2", "H3", "I1", "I2", "I3"]
unit_8 = ["G4", "G5", "G6", "H4", "H5", "H6", "I4", "I5", "I6"]
unit_9 = ["G7", "G8", "G9", "H7", "H8", "H9", "I7", "I8", "I9"]


#gets the unit in which the position is located
def getUnit(row, column):
	unit = 0
	if row == 'A' or row == 'B' or row == 'C':
		intColumn = int(column)
		if intColumn < 4:
			unit = 1
		elif intColumn < 7:
			unit = 2
		elif intColumn < 10:
			unit = 3
	elif row == 'D' or row == 'E' or row == 'F':
		intColumn = int(column)
		if intColumn < 4:
			unit = 4
		elif intColumn < 7:
			unit = 5
		elif intColumn < 10:
			unit = 6
	elif row == 'G' or row == 'H' or row == 'I':
		intColumn = int(column)
		if intColumn < 4:
			unit = 7
		elif intColumn < 7:
			unit = 8
		elif intColumn < 10:
			unit = 9

	return unit


#gets the domain of a position in the sudoku table
def getDomain(table, key):
	domain = []
	possibleDomain = {'1': False, '2': False, '3': False,'4': False, '5': False, '6': False, '7': False, '8': False, '9': False}

	row = key[0]
	column = key[1]

	for x in range(1, 10):
		checkKey = row + str(x)
		possibleDomain[table[checkKey]] = True

	allRows = "ABCDEFGHI"

	for letter in allRows:
		checkKey = letter + column
		possibleDomain[table[checkKey]] = True

	unit = getUnit(row, column)

	if unit == 1:
		for index in unit_1:
			possibleDomain[table[index]] = True
	elif unit == 2:
		for index in unit_2:
			possibleDomain[table[index]] = True
	elif unit == 3:
		for index in unit_3:
			possibleDomain[table[index]] = True
	elif unit == 4:
		for index in unit_4:
			possibleDomain[table[index]] = True
	elif unit == 5:
		for index in unit_5:
			possibleDomain[table[index]] = True
	elif unit == 6:
		for index in unit_6:
			possibleDomain[table[index]] = True
	elif unit == 7:
		for index in unit_7:
			possibleDomain[table[index]] = True
	elif unit == 8:
		for index in unit_8:
			possibleDomain[table[index]] = True
	elif unit == 9:
		for index in unit_9:
			possibleDomain[table[index]] = True

	for x in range(1, 10):
		if possibleDomain[str(x)] == False:
			domain.append(str(x))

	return domain


#returns all the empty spaces in the sudoku table
def getVariables(table):
	variables = []

	for position in sorted(table):
		if int(table[position]) == 0:
			variables.append(position)

	return variables


#gets the related neighbors for a position in a sudoku table
def getNeighbors(table, key, variables):
	neighbors = []

	row = key[0]
	column = key[1]

	for position in variables:
		if position[0] == row and position != key:
			neighbors.append(position)
		if position[1] == column and position != key:
			neighbors.append(position)

	unit = getUnit(row, column)

	if unit == 1:
		for position in variables:
			for unitPosition in unit_1:
				if position == unitPosition and position != key:
					neighbors.append(position)
	elif unit == 2:
		for position in variables:
			for unitPosition in unit_2:
				if position == unitPosition and position != key:
					neighbors.append(position)
	elif unit == 3:
		for position in variables:
			for unitPosition in unit_3:
				if position == unitPosition and position != key:
					neighbors.append(position)
	elif unit == 4:
		for position in variables:
			for unitPosition in unit_4:
				if position == unitPosition and position != key:
					neighbors.append(position)
	elif unit == 5:
		for position in variables:
			for unitPosition in unit_5:
				if position == unitPosition and position != key:
					neighbors.append(position)
	elif unit == 6:
		for position in variables:
			for unitPosition in unit_6:
				if position == unitPosition and position != key:
					neighbors.append(position)
	elif unit == 7:
		for position in variables:
			for unitPosition in unit_7:
				if position == unitPosition and position != key:
					neighbors.append(position)
	elif unit == 8:
		for position in variables:
			for unitPosition in unit_8:
				if position == unitPosition and position != key:
					neighbors.append(position)
	elif unit == 9:
		for position in variables:
			for unitPosition in unit_9:
				if position == unitPosition and position != key:
					neighbors.append(position)

	return neighbors


#returns all the possible arcs for the sudoku table
def getArcs(table, variables):
	arcs = []

	for position in variables:
		neighbors = getNeighbors(table, position, variables)

		for neighbor in neighbors:
			if neighbor != position:
				arcs.append((position, neighbor))

	return arcs


#used by AC3 algorithm
def revise(table, firstDomain, secondDomain):
	revised = False
	for x in firstDomain:
		satisfied = False
		for y in secondDomain:
			if x != y:
				satisfied = True

		if not satisfied:
			firstDomain.remove(x)
			revised = True

	return revised, firstDomain


#the AC-3 algorithm for the sudoku table
def AC3_search(table):
	tableDict = create_sudoku_table(table)
	variables = getVariables(tableDict)
	arcs = getArcs(tableDict, variables)

	domainDict = {}

	while arcs:
		(firstPos, secondPos) = arcs[0]
		arcs.remove((firstPos, secondPos))

		firstDomain = []
		if firstPos not in domainDict:
			firstDomain = getDomain(tableDict, firstPos)
		else:
			firstDomain = domainDict[firstPos]

		secondDomain = []
		if secondPos not in domainDict:
			secondDomain = getDomain(tableDict, secondPos)
		else:
			secondDomain = domainDict[secondPos]

		revised, firstDomain = revise(tableDict, firstDomain, secondDomain)
		domainDict[firstPos] = firstDomain

		if revised:
			if len(firstDomain) == 0:
				print "ok"
				return {}

			neighbors = getNeighbors(table, firstPos, variables)
			for position in neighbors:
				if position != secondPos:
					arcs.append((position, firstPos))

	return domainDict


#solves the sudoku table using the AC3 algorithm
def AC3(table):
	domains = AC3_search(table)

	for domain in domains:
		if len(domains[domain]) > 1:
			return False

	oldTable = create_sudoku_table(table)

	for position in domains:
		oldTable[position] = domains[position][0]

	newTable = ""
	key = 0
	for position in sorted(oldTable):
		newTable += str(oldTable[position])

	return newTable


#the BTS algorithm for the sudoku table
def BTS_search(table):
	if solved(table):
		return table

	var, domain = getLowestDomain(table)

	for value in domain:
		if checkValue(value, var, table):
			table[var] = value
			result = BTS_search(table)
			if result != False:
				return result

			table[var] = '0'

	return False


#checks if a value is valid in the sudoku table:
def checkValue(value, var, table):
	copyTable = dict(table)

	copyTable[var] = value

	for key in copyTable:
		if copyTable[key] == '0':
			if len(getDomain(copyTable, key)) == 0:
				return False

	return True


#returns the variable with the lowest number of values in the domain
def getLowestDomain(table):
	lowestDomainVar = ("A1", [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

	for position in table:
		if table[position] == '0':
			newDomain = getDomain(table, position)

			if len(newDomain) < len(lowestDomainVar[1]):
				lowestDomainVar = (position, newDomain)

	return lowestDomainVar


#solves the sudoku table using the BTS algorithm
def BTS(table):
	tableDict = create_sudoku_table(table)

	newAssignment = BTS_search(tableDict)

	if newAssignment == False:
		return False

	newTable = ""
	key = 0
	for position in sorted(newAssignment):
		newTable += str(newAssignment[position])

	return newTable


#checks if the sudoku table is solved
def solved(table):
	for position in table:
		if table[position] == '0':
			return False

	return True



#the main method
table = sys.argv[1]
output = AC3(table)
if output:
	output += " AC3"
else:
	output = BTS(table) + " BTS"

file = open('output.txt', 'w')
file.write(output)
file.close()
