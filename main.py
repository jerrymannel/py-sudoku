# import data
import display
from copy import deepcopy

numberSet = [1,2,3,4,5,6,7,8,9]

def __cleanUpEachGrid(_grid):
	for offset in range(0, 7 , 3):
		for n in range(0, 7 , 3):
			grid = []
			for r in range (0 + offset, 3 + offset):
				for c in range (0 + n , 3 + n):
					grid.append([r, c])
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
def __findMissingValues(_grid):
	print("Inside __findMissingValues()")
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
	print("Inside __columnScanAndCleanData()")
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
	print("Inside __cleanUpNumberGridUsingColValues()")
	for row in range(9):
		for col in range(9):
			if(type(_numberGrid[row][col]) is list):
				for number in _colValues[col]:
					if(type(_numberGrid[row][col]) is list):
						if(_numberGrid[row][col].count(number) != 0):
							_numberGrid[row][col].remove(number)

def __cleanUpNumberGrid(_numberGrid):
	print("Inside __cleanUpNumberGrid()")
	for row in range(9):
		for col in range(9):
			if(type(_numberGrid[row][col]) is list and len(_numberGrid[row][col]) == 1):
				# print(row, col, _numberGrid[row][col])
				_numberGrid[row][col] = _numberGrid[row][col][0]
				for r1 in range(9):
					# print(">", r1, col, _numberGrid[r1][col])
					if(type(_numberGrid[r1][col]) is list and _numberGrid[r1][col].count(_numberGrid[row][col]) != 0):
						_numberGrid[r1][col].remove(_numberGrid[row][col])
				# for r1 in range(9):
					# print(">", ">", r1, col, _numberGrid[r1][col])
	if(__hasSingleLengthListsAsMembers(_numberGrid)):
		__cleanUpNumberGrid(_numberGrid)

def sudoku(_grid):
	display.displayGrid(_grid)
	numberGrid = __findMissingValues(_grid)
	display.displayGridLineByLine(numberGrid)
	colValues = __columnScanAndCleanData(numberGrid)
	display.displayLineByLine(colValues)
	__cleanUpNumberGridUsingColValues(numberGrid, colValues)
	__cleanUpNumberGrid(numberGrid)
	display.displayGridLineByLine(numberGrid)
	# display.displayGrid(numberGrid)















