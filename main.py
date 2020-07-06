# import data
import display
from copy import deepcopy

numberSet = [1,2,3,4,5,6,7,8,9]

gridList = [
	[[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]],
	[[0, 3], [0, 4], [0, 5], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5]],
	[[0, 6], [0, 7], [0, 8], [1, 6], [1, 7], [1, 8], [2, 6], [2, 7], [2, 8]],
	[[3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2], [5, 0], [5, 1], [5, 2]],
	[[3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4], [5, 5]],
	[[3, 6], [3, 7], [3, 8], [4, 6], [4, 7], [4, 8], [5, 6], [5, 7], [5, 8]],
	[[6, 0], [6, 1], [6, 2], [7, 0], [7, 1], [7, 2], [8, 0], [8, 1], [8, 2]],
	[[6, 3], [6, 4], [6, 5], [7, 3], [7, 4], [7, 5], [8, 3], [8, 4], [8, 5]],
	[[6, 6], [6, 7], [6, 8], [7, 6], [7, 7], [7, 8], [8, 6], [8, 7], [8, 8]]
]

def __cleanUpEachGrid(_grid):
	for grid in gridList:
		numbers = []
		for index in grid:
			if type(_grid[index[0]][index[1]]) is int:
				numbers.append(_grid[index[0]][index[1]])
		# print "Grid", offset, n, numbers
		for index in grid:
			if type(_grid[index[0]][index[1]]) is list:
				for n in numbers:
					if _grid[index[0]][index[1]].count(n) > 0:
						_grid[index[0]][index[1]].remove(n)
	return _grid

# get the horizontal set of missing numbers
def __findMissingValuesAtEachCell(_grid):
	numberGrid = deepcopy(_grid)
	for rowIndex in range(9):
		row = _grid[rowIndex][:]
		missing = []
		for i in numberSet:
			if(row.count(i) == 0 ):
				missing.append(i)
		for colIndex in range(9):
			if(numberGrid[rowIndex][colIndex] == 0 ):
				numberGrid[rowIndex][colIndex] = missing[:]
	__cleanUpEachGrid(numberGrid)
	return numberGrid

# get the vertical set of numbers
def __columnScanAndCleanData(_grid):
	colValues = []
	for rowIndex in range(9):
		colValues.append([])
		for colIndex in range(9):
			if(type(_grid[colIndex][rowIndex]) is int):
				colValues[rowIndex].append(_grid[colIndex][rowIndex])
	return colValues

def __hasUnresolvedValues(_numberGrid):
	for row in _numberGrid:
		for col in row:
			if(type(col) is list):
				return 1
	return 0

def __hasSingleLengthListsAsMembers(_numberGrid):
	for row in _numberGrid:
		for col in row:
			if(type(col) is list and len(col) == 1):
				return 1
	return 0

def __cleanUpNumberGridUsingColValues(_numberGrid, _colValues):
	for row in range(9):
		for col in range(9):
			if(type(_numberGrid[row][col]) is list):
				for number in _colValues[col]:
					if(type(_numberGrid[row][col]) is list):
						if(_numberGrid[row][col].count(number) != 0):
							_numberGrid[row][col].remove(number)

def __cleanUpNumberGridUsingRowValues(_numberGrid):
	for row in range(9):
		singleNumberList = []
		for col in range(9):
			if(type(_numberGrid[row][col]) is int):
				singleNumberList.append(_numberGrid[row][col])
		for singleNumber in singleNumberList:
			for col in range(9):
				if(type(_numberGrid[row][col]) is list and _numberGrid[row][col].count(singleNumber) != 0):
							_numberGrid[row][col].remove(singleNumber)

def __cleanUpNumberGrid(_numberGrid):
	for row in range(9):
		for col in range(9):
			if(type(_numberGrid[row][col]) is list and len(_numberGrid[row][col]) == 1):
				_numberGrid[row][col] = _numberGrid[row][col][0]
				for r1 in range(9):
					if(type(_numberGrid[r1][col]) is list and _numberGrid[r1][col].count(_numberGrid[row][col]) != 0):
						_numberGrid[r1][col].remove(_numberGrid[row][col])
	if(__hasSingleLengthListsAsMembers(_numberGrid)):
		__cleanUpNumberGrid(_numberGrid)

def __cleanUpUsingFrequencyDistribution(_numberGrid):
	for grid in gridList:
		numberFrequency = [0,0,0,0,0,0,0,0,0]
		for index in grid:
			if type(_numberGrid[index[0]][index[1]]) is list:
				for n in _numberGrid[index[0]][index[1]]:
					numberFrequency[n-1] += 1
		# print(numberFrequency)
		for num, val in enumerate(numberFrequency, start=1):
			if(val==1):
				for index in grid:
					if(type(_numberGrid[index[0]][index[1]]) is list and _numberGrid[index[0]][index[1]].count(num) == 1):
						_numberGrid[index[0]][index[1]] = [num]

def scanAndClean(_numberGrid):
	colValues = __columnScanAndCleanData(_numberGrid)
	__cleanUpNumberGridUsingColValues(_numberGrid, colValues)
	__cleanUpNumberGridUsingRowValues(_numberGrid)
	__cleanUpEachGrid(_numberGrid)
	__cleanUpUsingFrequencyDistribution(_numberGrid)
	__cleanUpNumberGrid(_numberGrid)
	# display.displayGridLineByLine(_numberGrid)
	return __hasUnresolvedValues(_numberGrid)

def sudoku(_grid):
	# display.displayGrid(_grid)
	# display.displayLineByLine(_grid)
	numberGrid = __findMissingValuesAtEachCell(_grid)
	while(True):
		if(scanAndClean(numberGrid) == 0):
			break
	# display.displayGrid(numberGrid)
	return numberGrid
